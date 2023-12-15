![mega-creator (11)](https://github.com/social-shield/.github/assets/79012314/dbf41541-d159-4022-bc34-04d6185d27e2)

<h1 align="center">social-shield</h1>

SocialShield is a Python library designed to empower developers in the analysis and processing of social media data. Whether you're working with diverse datasets or need robust text preprocessing pipelines, SocialShield has you covered.

```
social-shield
 |-- datasets
 |  |-- load_scams
 |  |-- BiNetwork50
 |  |-- UniNetwork150
 |-- preprocess
 |  |-- negative=True
 |  |-- negative=False
 |-- show_network
```

## Features

### 1. Diverse Dataset Support

SocialShield supports various types of datasets, making it versatile for different social media platforms. Whether you're dealing with tweets, Facebook posts, or Instagram comments, SocialShield can seamlessly handle different data structures.

### 2. Built-in Text Preprocessing Pipelines

SocialShield comes with built-in text preprocessing pipelines to streamline your data cleaning and analysis tasks. From handling special characters to normalizing text, our preprocessing tools make it easy to prepare your data for further analysis.

## Datasets
### 1. scams.csv

The dataset consists of text samples, each labeled either "yes" or "no" to indicate whether the content is indicative of a scam. The text samples cover a range of topics, with those labeled "yes" likely representing scam-related content, and those labeled "no" representing non-scam content. It's tailored exclusively for binary classification, distinguishing between scam-related and non-scam-related text samples.
### 2. BiNetwork50.json

The dataset is a compilation of social media profiles, each identified by a unique node ("1," "2," etc.), featuring corresponding tweets and connections. With a total of 50 nodes, the dataset provides insights into individuals' tweets and their connections with other users on the platform. The tweets encompass a variety of content, ranging from personal updates and interests to potential instances of spam or scam-related information. The connections within the dataset denote relationships between users, suggesting friendships or other forms of interaction within the social media environment.

```
social-shield
|-- datasets
|   |-- scams.csv
|   |   |-- Here is a great investment opportunity! Click here to learn more: [link]  ,  yes
|   |   |-- I'm giving away a free car! All you have to do is retweet this post and follow me ,  yes
|   |   |-- You've won a prize! Click here to claim your prize: [link]    yes
|   |   |-- Access to quality healthcare is a fundamental right for every individual. #HealthcareForAll,	no
|   |   |-- Preventive care is key to maintaining a healthy nation. #PublicHealth	,no
|   |   |-- The pandemic has highlighted the importance of a strong healthcare system. #COVID19	,no
|   |   |-- ... (remaining dataset content)
|   |-- BiNetwork50
|   |   |-- 1
|   |   |   |-- Tweets
|   |   |   |   |--Saw a beautiful sunset today.
|   |   |   |   |--Invest today and work towards your financial goals!
|   |   |   |   |-- ... (remaining dataset content)
|   |   |   |-- Connections
|   |   |   |   |-- 2
|   |   |   |   |-- 4
|   |   |   |   |-- 7
```

## Getting Started

### Installation

You can install SocialShield using pip:

```bash
pip install socialshield
