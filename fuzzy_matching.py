import pandas as pd
#from fuzzywuzzy import fuzz
import re
from rapidfuzz import fuzz

# Load the datasets with low_memory=False
google_df = pd.read_csv('NEWDATASET/google_duplicates.csv', on_bad_lines='skip', encoding='utf-8', low_memory=False)
facebook_df = pd.read_csv('NEWDATASET/facebook_duplicates.csv', on_bad_lines='skip', low_memory=False)
website_df = pd.read_csv('NEWDATASET/website_duplicates_modified.csv', on_bad_lines='skip', low_memory=False)

# Ensure phone numbers are treated as strings and remove any non-numeric characters
facebook_df['Phone'] = facebook_df['Phone'].astype(str).str.replace(r'[^\d]', '', regex=True)
google_df['Phone'] = google_df['Phone'].astype(str).str.replace(r'[^\d]', '', regex=True)
website_df['Phone'] = website_df['Phone'].astype(str).str.replace(r'[^\d]', '', regex=True)


# Function to check if two rows are similar based on fuzzy matching
def is_similar(row1, row2, threshold=50):
    # Fuzzy matching on 'Company Name'
    name_similarity = fuzz.token_sort_ratio(row1['Company Name'], row2['Company Name'])

    # Fuzzy matching on 'Phone' (if both are not NaN)
    if pd.notna(row1['Phone']) and pd.notna(row2['Phone']):
        phone_similarity = fuzz.token_sort_ratio(str(row1['Phone']), str(row2['Phone']))
    else:
        phone_similarity = 100 if pd.isna(row1['Phone']) and pd.isna(row2['Phone']) else 0

    # Fuzzy matching on 'Category' (if both are not NaN)
    if pd.notna(row1['Category']) and pd.notna(row2['Category']):
        category_similarity = fuzz.token_sort_ratio(row1['Category'], row2['Category'])
    else:
        category_similarity = 100 if pd.isna(row1['Category']) and pd.isna(row2['Category']) else 0

    # Check if all fields have 80% or more similarity
    return name_similarity >= threshold and phone_similarity >= threshold and category_similarity >= threshold


# Remove fuzzy duplicates based on 'Company Name', 'Phone', and 'Category'
def remove_fuzzy_duplicates(df, threshold=50):
    to_drop = []  # List to store indices of rows to drop

    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            if j in to_drop:  # Skip rows already marked for dropping
                continue

            # Check if rows are similar
            if is_similar(df.iloc[i], df.iloc[j], threshold=threshold):
                to_drop.append(j)  # Mark duplicate-like rows for dropping

    # Drop duplicate-like rows
    df_cleaned = df.drop(to_drop).reset_index(drop=True)
    return df_cleaned


# Clean combined dataframe by removing fuzzy duplicates
google_df = remove_fuzzy_duplicates(google_df)
facebook_df = remove_fuzzy_duplicates(facebook_df)
website_df = remove_fuzzy_duplicates(website_df)

# save the cleaned dataset to a new CSV file
google_df.to_csv('FUZZYMATCHING/fuzzy_google_dataset.csv', index=False)
facebook_df.to_csv('FUZZYMATCHING/fuzzy_facebook_dataset.csv', index=False)
website_df.to_csv('FUZZYMATCHING/fuzzy_website_dataset.csv', index=False)
