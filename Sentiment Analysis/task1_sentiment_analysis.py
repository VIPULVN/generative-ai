"""
Sentiment Analysis Pipeline using Hugging Face Transformers.

This script demonstrates how to use the high-level `pipeline` API from the 
transformers library to perform sentiment analysis on text.
It covers single string inputs as well as batch processing of lists.
"""

# Import the pipeline module from the transformers library
from transformers import pipeline

# Initialize the sentiment-analysis pipeline.
# Note: If you don't specify a model, it automatically defaults to:
# 'distilbert/distilbert-base-uncased-finetuned-sst-2-english'
# This will download the model weights the first time you run it.
print("Initializing the classifier model...\n")
classifier = pipeline("sentiment-analysis")


# ==========================================
# EXAMPLE 1: Single Positive Review
# ==========================================
print("--- Example 1: Single Positive Review ---")
review_positive = "I love this movie!"

# Pass the string to the classifier
result_positive = classifier(review_positive)

print(result_positive)
# Expected Output:
# [{'label': 'POSITIVE', 'score': 0.9998656511306763}]
print("\n")


# ==========================================
# EXAMPLE 2: Single Negative Review
# ==========================================
print("--- Example 2: Single Negative Review ---")
review_negative = "This film was a waste of time"

# Pass the string to the classifier
result_negative = classifier(review_negative)

print(result_negative)
# Expected Output:
# [{'label': 'NEGATIVE', 'score': 0.9998158812522888}]
print("\n")


# ==========================================
# EXAMPLE 3: Batch Processing (List of Reviews)
# ==========================================
print("--- Example 3: Batch Processing ---")
# You can pass a list of strings to process multiple reviews efficiently in one go
reviews_list = [
    "This film was a waste of time",
    "This film was very nice"
]

# The classifier returns a list of dictionaries corresponding to the input list
results_list = classifier(reviews_list)

print(results_list)
# Expected Output: 
# [{'label': 'NEGATIVE', 'score': 0.9998158812522888}, {'label': 'POSITIVE', 'score': 0.9998468160629272}]
print("\n")


# ==========================================
# EXAMPLE 4: Formatting the Output cleanly
# ==========================================
print("--- Example 4: Formatted Output ---")
# Using the built-in zip() function, we can iterate through both our input list 
# and our results list simultaneously to print a nicely formatted summary.

for review, result in zip(reviews_list, results_list):
    # We access the 'label' and 'score' keys from the result dictionary
    print(f"Review: {review} | Sentiment: {result['label']} | Score: {result['score']:.4f}")
    
# Expected Output:
# Review: This film was a waste of time | Sentiment: NEGATIVE | Score: 0.9998
# Review: This film was very nice | Sentiment: POSITIVE | Score: 0.9998