 # SMS Spam Detection System

This project is a machine learning-based SMS spam detection system that classifies messages as spam or not spam (ham). It uses natural language processing techniques to preprocess text and a trained classification model for prediction.

## Features

- Classifies SMS messages as spam or ham
- Uses text preprocessing for cleaning input data
- Machine learning model trained on labeled SMS dataset
- Simple and interactive interface (if integrated with Flask/UI)

## Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- Natural Language Processing (NLP)
- Flask (if web interface is included)

## Dataset

The model is trained on a custom SMS dataset containing approximately 20,000 messages. The dataset includes both spam and ham (non-spam) messages and is specifically collected and structured for this project.

The dataset is based on Pakistani SMS patterns, making it more relevant for local language and regional texting behavior compared to generic global datasets.

## Model Details

- Text vectorization using TF-IDF
- Classification model (Logistic Regression / Naive Bayes)
- Trained on labeled SMS dataset containing spam and ham messages

## How It Works

1. User inputs an SMS message
2. Text is cleaned and preprocessed
3. TF-IDF vectorizer converts text into numerical features
4. Trained model predicts whether the message is spam or not
5. Result is displayed to the user

## Installation

```bash
pip install -r requirements.txt
```

## Run The Project
```
python app.py
```

## Notes
Model performance depends on dataset quality and preprocessing steps
Can be improved using advanced NLP models like BERT or transformer-based approaches

## Author

Sana Fatima
