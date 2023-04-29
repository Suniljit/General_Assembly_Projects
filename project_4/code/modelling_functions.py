# Import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV, PredefinedSplit
from scipy.stats import randint
import random


def series_to_window(data, var_list=None, n_in=1, n_out=1, dropnan=True):
    '''
    Function that transform a time series dataset into a lagged supervised learning dataset
    
    Parameters:
    -----------
    data: pandas DataFrame
        times series to be transformed, the index should be datetime
    
    var_list: list of str
        list of variables to be lagged, these should be columns in data, else there will be an error
        default = None, which means all variables in data will be lagged based on n_in and n_out
        
    n_in: int
        number of lags to be introduced
        default = 1
        
    n_out: int
        number of leads to be introduced
        default = 1, i.e. will include current term
        
    dropnan: bool
        whether to drop nan rows that appear after lagging
        default = True, to drop any rows with nan values
        
    Returns:
    --------
    pandas DataFrame
        sliding window based on arguments given and includes existing index
        
    '''
    
    # isolate selected variables
    if var_list is None:
        temp = data.copy()
    elif type(var_list) is list:
        temp = data[var_list].copy()
    else:
        temp = data[[var_list]].copy()
    
    df = pd.DataFrame(index=data.index)
    
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols = temp.shift(i)
        cols.columns = [f'{name}_lag_{i}' for name in cols.columns]
        df = pd.concat([df, cols], axis=1)
    
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols = temp.shift(-i)
        if not i == 0:
            cols.columns = [f'{name}_lead_{i}' for name in cols.columns]
        df = pd.concat([df, cols], axis=1)
    
    # combine shifted and non-shifted data
    if var_list is None:
        return df
    else:
        df = pd.concat([data.drop(columns=var_list), df], axis=1)
    
    # drop rows with NaN values
    if dropnan:
        df.dropna(inplace=True)
    
    return df


def train_test_split(data, year=2021):
    '''
    Function that splits the time series into train and test sets
    
    Parameters:
    -----------
    data: pandas DataFrame
        data to be split, index should be datetime
        
    year: int
        the year from which the train dataset ends
        default = 2021, the train dataset is defined as all the data from the set of the dataframe to the end of year 2021
        
    Returns:
    --------
    pandas DataFrame, train
        train is the train dataset
        
    pandas DataFrame, test
        test is the test dataset
        
    '''
    index_indicated = (data.index.year <= year).sum()
    
    # Train data will cover 2018 to 2021
    train = data.iloc[:index_indicated]

    # Test data will cover 2022 to March 2023
    test = data.iloc[index_indicated:]
    
    return train, test


# Time series plot of the train and test data
def train_test_plot(train, test, pred=None, title=None):
    '''
    Function that plots the time series
    
    Parameters:
    -----------
    train: pandas DataFrame
        train dataset, index should be datetime
        
    test: pandas DataFrame or pandas Series
        test dataset, index should be datetime
        
    preds: pandas DataFrame or pandas Series
        predicted dataset, index should be datetime and same as test dataset
        default = None, i.e. will not be plotted
        
    title: str
        title of the plot
        default = None
        
    Returns:
    --------
    None
    
    '''
    
    plt.figure(figsize=(15, 5))
    
    plt.plot(train[['dengue_cases']], c='blue')
    plt.plot(test[['dengue_cases']], c='orange')
    
    if isinstance(pred, pd.DataFrame) or isinstance(pred, pd.Series):
        plt.plot(pred, c='green')
        plt.legend(['train', 'test', 'predicted'])
    else:
        plt.legend(['train', 'test'])
    
    if not (title == None):
        plt.title(title)
    
    plt.ylabel('Number of dengue cases (weekly)')
    
    plt.show()
    

def fit_rf_model(X, y, rf_params):
    '''
    Function that fits a random forest regressor based on the dataset and hyperparameters given

    Parameters:
    -----------
    X: pandas DataFrame
        predictor variables dataset
        
    y: pandas Series
        outcome variable dataset
        
    rf_params: dict
        dictionary of parameters for random forest model
    
    Returns:
    --------
    RandomForestRegressor object
        fitted model
    
    '''
    # instantiate model
    model = RandomForestRegressor(**rf_params)
    
    # fit model
    model.fit(X, y)
    
    return model    
    

def get_random_params(params_dist):
    '''
    Function that outputs a random set of parameters based on the limits set in params_dist
    
    Parameters:
    -----------
    params_dist: dict
        dictionary of distributions of parameters for random forest
    
    Returns:
    --------
    dict
        randomised parameter set
        
    ''' 
    
    params = {}
    
    params['n_estimators'] = random.choice(params_dist['n_estimators'])
    params['max_features'] = random.choice(params_dist['max_features'])
    params['max_depth'] = random.choice(params_dist['max_depth'])
    params['min_samples_split'] = params_dist['min_samples_split'].rvs()
    params['min_samples_leaf'] = params_dist['min_samples_leaf'].rvs()
    
    return params


def test_rf_model(data, test_year, vars_lag, num_lag, rf_params, y_var='dengue_cases', tune=False, max_iter=100):
    '''
    Function to lag the data and split the train, test datasets and test out a random forest model
    
    Paramters:
    ----------
    data: pandas DataFrame
        full time dataset, index should be datetime
        
    test_year: int
        the year from which the test dataset is

    vars_lag: list of str
        variables that need to be lagged
        
    num_lag: int
        number of lags to introduce
        
    rf_params: dict
        either the parameters for random forest regressor (if tune==False)
        or the distribution of parameters (if tune==True)
        
    y_var: str
        name of the outcome variable in the dataset
        default = dengue_cases
    
    tune: bool
        setting to decide whether to tune the parameters
        default = False, only given set of parameters will be run
        
    max_iter: int
        number of iterations to tune, only if tune==True
        default = 100 iterations
        
    Returns:
    --------
    dict
        model: RandomForestRegressor
            best model fitted
        preds_train: pandas DataFrame
            predicted outcome variable on the train dataset
        preds_test: pandas DataFrame
            predicted outcome variable on the test dataset
        rmse_train: float
            RMSE of train dataset
        rmse_test: float
            RMSE of test dataset
        mape_train: float
            MAPE of train dataset
        mape_test: float
            MAPE of test dataset
            
    '''
    
    # lag dataset
    data = series_to_window(data, var_list=vars_lag, n_in=num_lag)
    
    # split into train and test datasets
    train, test = train_test_split(data, test_year-1)
    
    # for fixed hyperparameters
    if tune == False:
        model = fit_rf_model(train.drop(columns=y_var), train[y_var], rf_params)
        
    else:
        for trial in range(max_iter):
            params = get_random_params(rf_params)
        
            # instantiate model
            model_trial = RandomForestRegressor(**params)
        
            # test fit model
            model_trial.fit(train.drop(columns=y_var), train[y_var])
            
            rmse_trial = mean_squared_error(test[y_var], model_trial.predict(test.drop(columns=y_var)), squared=False)
            
            if trial == 0:
                model = model_trial
                rmse = rmse_trial
            
            if rmse_trial < rmse:
                model = model_trial
                rmse = rmse_trial
        
    # run the predictions
    preds_train = model.predict(train.drop(columns=y_var))
    preds_test = model.predict(test.drop(columns=y_var))
    
    # compute metrics
    results = dict()
    results['model'] = model
    results['preds_train'] = pd.DataFrame(preds_train, index=train.index)
    results['preds_test'] = pd.DataFrame(preds_test, index=test.index)
    results['rmse_train'] = mean_squared_error(train[y_var], preds_train, squared=False)
    results['rmse_test'] = mean_squared_error(test[y_var], preds_test, squared=False)
    results['mape_train'] = mean_absolute_percentage_error(train[y_var], preds_train)
    results['mape_test'] = mean_absolute_percentage_error(test[y_var], preds_test)
    
    return results


def test_rf_model_defunc(data, test_year, vars_lag, num_lag, rf_params, y_var='dengue_cases', tune=False, max_iter=100):
# function to lag the data and split the train, test datasets and test out a random forest model
    
    # lag dataset
    data = series_to_window(data, var_list=vars_lag, n_in=num_lag)
    
    # split into train and test datasets
    train, test = train_test_split(data, test_year-1)
    
    # for fixed hyperparameters
    if tune == False:
        model = fit_rf_model(train.drop(columns=y_var), train[y_var], rf_params)
        
    else:
        # reset index of data for fixed train and cross-validation setting for RandomizedSearchCV (weird issue: it cannot handle datetime dtype index)
        data_idx = data.index
        data.reset_index(inplace=True)
        data.drop(columns='time', inplace=True)
        
        # create fixed indices for train and cross-validation sets
        train_idx = list(range((data_idx.year < 2022).sum()))
        val_idx = list(range((data_idx.year < 2022).sum(), len(data_idx)))
        
        # instantiate model
        model = RandomForestRegressor()
        
        # tune hyperparameters
        model_search = RandomizedSearchCV(estimator=model, param_distributions=rf_params, 
                                          scoring='neg_root_mean_squared_error',
                                          n_iter=max_iter, cv=[(train_idx, val_idx)], n_jobs=-1,
                                          error_score='raise', verbose=3
                                         )
        model_search.fit(data.drop(columns=y_var), data[y_var])
        
        # retrain only best model
        model = fit_rf_model(train.drop(columns=y_var), train[y_var], model_search.best_params_)
        
    # run the predictions
    preds_train = model.predict(train.drop(columns=y_var))
    preds_test = model.predict(test.drop(columns=y_var))
    
    # compute metrics
    results = dict()
    results['model'] = model
    results['preds_train'] = pd.DataFrame(preds_train, index=train.index)
    results['preds_test'] = pd.DataFrame(preds_test, index=test.index)
    results['rmse_train'] = mean_squared_error(train[y_var], preds_train, squared=False)
    results['rmse_test'] = mean_squared_error(test[y_var], preds_test, squared=False)
    results['mape_train'] = mean_absolute_percentage_error(train[y_var], preds_train)
    results['mape_test'] = mean_absolute_percentage_error(test[y_var], preds_test)
    
    return results

def evaluate_model(y_real, y_pred):
    '''
    Function that returns the root mean squared error of the model with other statistics
    
    Paramters:
    ----------
    y_real: pandas DataFrame or pandas Series
        real dengue cases
        
    y_pred: pandas DataFrame or pandas Series
        predicted dengue cases
        
    Returns:
    --------
    float
        rmse
        
    '''
    # compute rmse
    error = mean_squared_error(y_real, y_pred, squared=False)
    
    print(f'RMSE: {error}\n')
    print(f'Minimum Dengue Cases: {round(y_real.min(),0)}')
    print(f'Maximum Dengue Cases: {round(y_real.max(),0)}')

    print(f'RMSE relative to minimum values in dengue cases: {round(error / y_real.min(),2)}.')
    print(f'RMSE relative to maximum values in dengue cases: {round(error / y_real.max(),2)}.')
    
    return error

def plot_residuals(y_real, y_pred, title=None):
    '''
    Function that plots the residuals of the model
    
    Paramters:
    ----------
    y_real: pandas DataFrame or pandas Series
        real dengue cases
        
    y_pred: pandas DataFrame or pandas Series
        predicted dengue cases
        
    title: str
        title of the plot
        default = None
        
    Returns:
    --------
    pandas Series
        residual values
        
    '''
    # Calculate residuals.
    resids = pd.Series(y_real.values - y_pred.values, index=y_real.index)
    
    # scatterplot of residuals
    plt.figure(figsize=(15,5))
    plt.scatter(resids.index, resids, c='red')
    plt.hlines(y=0,
               xmin=y_real.index.min(),
               xmax=y_real.index.max(),
               linestyles='--'
              )
    plt.xticks(fontsize=14)
    plt.xlim(y_real.index.min(), y_real.index.max())
    plt.yticks(fontsize=14)
    plt.ylabel('Residuals', fontsize=14)
    
    if not (title == None):
        plt.title(title, fontsize=20)
        
    return resids


def lead_data(data, y_var='dengue_cases', weeks=0):
    '''
    Function that leads the outcome variable by the specific number of weeks and removes the NA rows
    
    Parameters:
    -----------
    data: pandas DataFrame
        data to be processed, make sure y_var is a column in data
        
    y_var: str
        column to be led
        default = dengue_cases
        
    weeks: int
        number of weeks to be led
        default = 0, i.e. data will not be led
        
    Returns:
    --------
    pandas DataFrame
        a copy of the original DataFrame with the y_var led
        
    '''
    
    # copy data
    output = data.copy()
    
    # lead the required variable
    output[y_var] = output[y_var].shift(-1*weeks)
    
    # remove NAs
    output.dropna(inplace=True)
    
    return output


def get_date_index(week, year):
    '''
    Function that obtains the date index of the x-th week of the y-th year as defined by the user
    '''
    from datetime import datetime
    
    return datetime.strptime(str(year) + '-' + str(week) + '-0', '%Y-%U-%w')