from copy import deepcopy
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV

class DengueModel():
    '''
    Class to construct dengue forecasting model
    
    '''
    
    def __init__(self, models, searchgrid=None, weeks=1):
        '''
        Method to instantiate object
        
        Parameters:
        -----------
        self: object
            The object itself
            
        models: dict
            Dictionary of sklearn ensemble objects, keys should be the name of each model and values should be the ensemble object
            
        weeks: int
            Number of weeks this model will forecast
            default = 1, i.e. model will always return 1-week ahead forecast as a default
        
        Returns:
        --------
        DengueModel object
        
        '''
        # store a list of models that will be fitted for each week forecast
        self.model_list = models
        
        # set default value of tuning to False
        self.tuning = False
        
        # check if searchgrid is filled, if it is, active hyperparameter tuning
        if not (searchgrid == None):
            self.searchgrid = searchgrid
            self.tuning = True
        
        # create dictionary of selected models for each week forecast
        model_keys = ['model_'+str(i)+'w' for i in range(1, weeks+1)]
        self.models = dict(zip(model_keys, [None]*len(model_keys)))
        
        # store the number of weeks ahead
        self.weeks = weeks
        
        
    def fit(self, X, y, test_year=2022):
        '''
        Method to fit the models to X and y, and choose the best model based on RMSE
        NOTE: X and y should include both the train and test datasets for the fitting to work properly
        '''
        # for each week ahead, we fit a model
        for week, model in enumerate(self.models, start=1):
            # print some nonsense to note that we are moving!
            print(f'Fitting model for week {week}...', end='\r')
            
            # lead the data accordingly
            data_week = pd.concat([X, y], axis=1)
            data_week = self.lead_data(data_week, y_var='dengue_cases', weeks=week)
            #print(data_week.head()['dengue_cases'])
            #X_week = X[:-1*week].dropna()
            #y_week = self.lead_data(y, weeks=week)
            
            train, test = self.train_test_split(data_week, year=test_year-1)
            X_train = train.drop(columns='dengue_cases')
            y_train = train['dengue_cases']
            X_test = test.drop(columns='dengue_cases')
            y_test = test['dengue_cases']
            #print(f'{week}: {X_train["Mean Temperature (°C)"].head()}')
            #X_train, X_test = self.train_test_split(X_week, year=test_year-1)
            #y_train, y_test = self.train_test_split(y_week, year=test_year-1)
            
            # for each model in model_list, fit and get rmse
            rmse_best = 1e10
            #model_best = None
            for model_trial, param_grid in zip(self.model_list.values(), self.searchgrid.values()):
                # check if tuning is true, if so, run GridSearchCV
                if self.tuning == True:
                    # reset index of data for fixed train and cross-validation setting for RandomizedSearchCV (weird issue: it cannot handle datetime dtype index)
                    data_temp = data_week.copy()
                    data_idx = data_temp.index
                    data_temp.reset_index(inplace=True)
                    data_temp.drop(columns='time', inplace=True)

                    # create fixed indices for train and cross-validation sets
                    train_idx = list(range((data_idx.year < test_year).sum()))
                    val_idx = list(range((data_idx.year < test_year).sum(), len(data_idx)))
                    
                    # define and fit model
                    grid_search = GridSearchCV(model_trial, param_grid, cv=[(train_idx, val_idx)], scoring='neg_root_mean_squared_error', n_jobs=-1)
                    grid_search.fit(data_temp.drop(columns='dengue_cases'), data_temp['dengue_cases'])
                    
                    model_trial = grid_search.best_estimator_
                else:
                    model_trial.fit(X_train, y_train)
                    
                rmse = mean_squared_error(y_test, model_trial.predict(X_test), squared=False)
                
                if rmse < rmse_best:
                    rmse_best = rmse
                    self.models[model] = deepcopy(model_trial)
            
            # print some statements to make it clear we are progressing hurhurhur
            print(f'Successfully fitted model for week {week}.')
        
    def predict(self, X):
        '''
        Method to predict outcome variable given X
        '''
        
        # create the prediction DataFrame
        pred = pd.DataFrame()
        
        # for each week ahead, we use the specific model to predict
        for week, model in enumerate(self.models.values(), start=1):
            # lead the data accordingly
            #X_week = X[:-1*week].dropna()
            X_week = X.dropna()
            #if week == 1:
            #    index_indices = X_week.index
            
            y_pred = pd.DataFrame(model.predict(X_week), index=X_week.index)
            #print(model)
            #print(y_pred.tail())
            
            if week == 1:
                pred = y_pred
            else:
                pred = pd.concat([pred, y_pred], axis=1, sort=False)
            
        # properly put in index
        #pred.index = index_indices

        # properly name the columns
        pred.columns = ['week'+str(i) for i in range(1, self.weeks+1)]

        # remove the NA rows at the end
        pred.dropna(inplace=True)
            
        return pred
            
    
    def score(self, X, y, sample_weight=None):
        '''
        Method that computes the root mean squared error of the predictions
        '''
        
        # predictions
        pred = self.predict(X[:-self.weeks])
        
        # convert y into sliding windows to calculate score
        ytrue = self.series_to_window(y.to_frame(), n_in=0, n_out=self.weeks+1)
        ytrue = ytrue.drop(columns='dengue_cases')
        # drop the last 'self.weeks' rows that contain nan
        ytrue.dropna(inplace=True)
        
        # calculate score
        return mean_squared_error(ytrue, pred, squared=False)
        
        
    def lead_data(self, data, y_var=None, weeks=0):
        '''
        Method that leads the y_var by weeks, and drops NA

        Parameters:
        -----------
        X: pandas DataFrame
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
        if y_var == None:
            # if no variable specified, the entire DataFrame/Series is led
            output = output.shift(-1*weeks)
        else:
            output[y_var] = output[y_var].shift(-1*weeks)
            #print(output.head()['dengue_cases'])

        # remove NAs
        output.dropna(inplace=True)

        return output
    
    
    def train_test_split(self, data, year=2021):
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

    
    def series_to_window(self, data, var_list=None, n_in=1, n_out=1, dropnan=True):
        '''
        Method that transform a time series dataset into a lagged supervised learning dataset

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