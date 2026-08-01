from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

# Sample paragraph
paragraph = "The cat sat on the mat. The dog sat on the log."

# Create the vectorizer
vectorizer = CountVectorizer()

# Transform the paragraph into a vector
vector = vectorizer.fit_transform([paragraph])

# Convert to array for easier viewing
vector_array = vector.toarray()

# Get the feature names (vocabulary)
feature_names = vectorizer.get_feature_names_out()

# Create a pandas DataFrame for better visualization
df = pd.DataFrame(vector_array, columns=feature_names)

print("Vocabulary:")
print(feature_names)
print("\nVector representation:")
print(df)
print("\nRaw vector array:")
print(vector_array)