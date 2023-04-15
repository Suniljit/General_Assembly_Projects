# Capstone Project - Video Classification of Exercises

## Problem Statement

With many people staying home due to the pandemic, more and more people are using online fitness videos to follow along to get their exercise in. This has created a large following for fitness influencers who post workout videos online (e.g. Chloe Ting with 24 mil subscribers, Pamela Reif with 9 mil subscribers, AthleanX). The most popular platform to host these fitness videos for free is YouTube.  

YouTube's timeline scrubber now has chapters, where you can detail what activity/task is being performed during a timeframe.

However, the information such as chapter title and timeframes has to be manually input by the content creators. Because it's rather tedious to do this, many videos are currently lacking this. By training a model that uses video classification to identify which exercise is currently being done, the scrubber bar's information can be generated automatically. 

**Business Case for Exercise Video Classification:**<br>
Auto-generate the title and timestamps for the YouTube Scrubber bar

**Other Business Cases:**<br>
1. Auto-captioning in exercise videos. The video creator does not need to manually put a caption for each exercise
2. Auto-generate hash tags for social media (e.g. #PushUps, #Squats)

**Project Scoping**<br>
There will be two main aspects to building this product:<br>
1. Back-end: A video classification model will be trained to classify exercise videos. By feeding an exercise video, e.g. someone doing pushups, the model will be able to identify the activity as pushups
2. Front-end: Integrate the model to platforms like YouTube to auto-generate the title and timestamps **(Not in the scope of this Capstone Project)**

## Proposed Methods and Models

**Models**

For preprocessing:
1. cv2 (OpenCV) - for video processing

Pre-Trained Models to consider:<br>
1. VideoMAE (Hugging Face) 
2. VGG16 (keras)
3. ResNet
4. MoViNet (tensorflow)

## Dataset

The dataset is being sourced from two locations:<br>
1. Kaggle datasets for exercise videos
2. Downloaded from YouTube

Due to a limitation in computing resources available, the scope of the dataset will be limited to:<br>
1. Three exercises to show that the model is able to classify multiple exercise types (e.g. Pushups, Squats, Jumping Jacks)
2. Approx. 50 videos per exercise will be downloaded 

## Challenges

1. Videos require a lot of computing power: leverage on google collab
2. Long training duration
3. Limited training data due to computing needs, which could result in low accuracy
4. Classification flickering: apply rolling predictional averaging

## Roadmap

The schedule to complete the project is detailed below:<br>

**Week 1: 16 April - 22 April**
* Continue research of modelling method and select models to train
* Download the dataset

**Week 2: 23 April - 29 April**
* Research and setup cloud tool (e.g. AWS or Google Colab) to use to train the model
* Process the dataset

**Week 3: 30 April - 6 May**
* Perform EDA
* Train the model

**Week 4: 7 May - 13 May**
* Fine-tune the model
* Perform evaluation of the model

**Week 5: 14 May - 20 May**
* Prepare presentation slides