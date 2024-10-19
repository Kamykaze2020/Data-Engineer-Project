import pandas as pd
import re

# Load the datasets with low_memory=False
google_cleaned = pd.read_csv('FUZZYMATCHING/fuzzy_google_dataset.csv', on_bad_lines='skip', low_memory=False)
facebook_cleaned = pd.read_csv('FUZZYMATCHING/fuzzy_facebook_dataset.csv', on_bad_lines='skip', low_memory=False)
website_cleaned = pd.read_csv('FUZZYMATCHING/fuzzy_website_dataset.csv', on_bad_lines='skip', low_memory=False)

# Reorder the cleaned data to match the original CSV columns
google_cleaned = google_cleaned[google_cleaned.columns]
facebook_cleaned = facebook_cleaned[facebook_cleaned.columns]
website_cleaned = website_cleaned[website_cleaned.columns]

# Append the cleaned data to the original CSV files
google_cleaned.to_csv('CLEANED/google_cleaned.csv', mode='a', index=False, header=False)
facebook_cleaned.to_csv('CLEANED/facebook_cleaned.csv', mode='a', index=False, header=False)
website_cleaned.to_csv('CLEANED/website_cleaned.csv', mode='a', index=False, header=False)