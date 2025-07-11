#training naive_bayes classifer for detecting email priority (eg.High, Normal, Loe)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Step 1: Create or load labeled data
data = pd.DataFrame({
    "email_text": [
        "Please respond ASAP to the legal department",
        "Reminder: tomorrow is team lunch",
        "Critical update from the CEO",
        "Holiday party invitation",
        "Quarterly earnings report attached"
    ],
    "priority": [
        "high",
        "low",
        "high",
        "low",
        "medium"
    ]
})

# Step 2: Create pipeline with vectorizer + classifier
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())  # Fast, light, and explainable
])

# Step 3: Train model
model.fit(data['email_text'], data['priority'])

# Step 4: Save model to file
joblib.dump(model, 'models/classifier.pkl')
print("Model saved to models/classifier.pkl")
