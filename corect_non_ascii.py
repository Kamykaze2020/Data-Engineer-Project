import pandas as pd
import unidecode
import re

# Load the datasets with low_memory=False
google_df = pd.read_csv('CLEANED/google_cleaned.csv', on_bad_lines='skip', low_memory=False)
facebook_df = pd.read_csv('CLEANED/facebook_cleaned.csv', on_bad_lines='skip', low_memory=False)
website_df = pd.read_csv('CLEANED/website_cleaned.csv', on_bad_lines='skip', low_memory=False)

# Function to replace special characters with ASCII equivalents
def replace_special_chars(text):
    if pd.isna(text):
        return text
    return unidecode.unidecode(text)

# Apply the function to the 'Company Name' column in each dataset
google_df['Company Name'] = google_df['Company Name'].apply(replace_special_chars)
facebook_df['Company Name'] = facebook_df['Company Name'].apply(replace_special_chars)
website_df['Company Name'] = website_df['Company Name'].apply(replace_special_chars)




# Get total number of rows in each dataset
google_total_rows = len(google_df)
facebook_total_rows = len(facebook_df)
website_total_rows = len(website_df)

# Check for duplicates in each dataset

# Calculate the percentage of NaN values in 'Company Name' column
google_duplicates_percentage = (google_df['Company Name'].duplicated().sum() / google_total_rows) * 100
facebook_duplicates_percentage = (facebook_df['Company Name'].duplicated().sum() / facebook_total_rows) * 100
website_duplicates_percentage = (website_df['Company Name'].duplicated().sum() / website_total_rows) * 100

# Print the results
print("\nDuplicate values in 'Company Name' column:")
print(f"Google: {google_df['Company Name'].duplicated().sum()} duplicates, {google_duplicates_percentage:.2f}% of total rows")
print(f"Facebook: {facebook_df['Company Name'].duplicated().sum()} duplicates, {facebook_duplicates_percentage:.2f}% of total rows")
print(f"Website: {website_df['Company Name'].duplicated().sum()} duplicates, {website_duplicates_percentage:.2f}% of total rows")



# Count the number of NaN values in the 'Company Name' column
google_nan_count = google_df['Company Name'].isna().sum()
facebook_nan_count = facebook_df['Company Name'].isna().sum()
website_nan_count = website_df['Company Name'].isna().sum()

# Calculate the percentage of NaN values in 'Company Name' column
google_nan_percentage = (google_nan_count / google_total_rows) * 100
facebook_nan_percentage = (facebook_nan_count / facebook_total_rows) * 100
website_nan_percentage = (website_nan_count / website_total_rows) * 100

# Print the results
print("\nNaN values in 'Company Name' column:")
print(f"Google: {google_nan_count} NaNs, {google_nan_percentage:.2f}% of total rows")
print(f"Facebook: {facebook_nan_count} NaNs, {facebook_nan_percentage:.2f}% of total rows")
print(f"Website: {website_nan_count} NaNs, {website_nan_percentage:.2f}% of total rows")

# Detect strange characters using regex on Company Name column

# Step 1: Define a function to detect non-ASCII characters in a string
def contains_non_ascii(text):
    if pd.isna(text):
        return False
    # Regex to match non-ASCII characters (characters outside the range of 0-127)
    return bool(re.search(r'[^\x00-\x7F]', text))

# Step 2: Apply this function to detect strange characters in the 'Company Name' column for each dataset
google_strange = google_df['Company Name'].apply(contains_non_ascii)
facebook_strange = facebook_df['Company Name'].apply(contains_non_ascii)
website_strange = website_df['Company Name'].apply(contains_non_ascii)

# Step 3: Count how many rows contain strange characters
google_strange_count = google_strange.sum()
facebook_strange_count = facebook_strange.sum()
website_strange_count = website_strange.sum()

# Step 4: Calculate the percentage of rows with strange characters
google_strange_percentage = (google_strange_count / google_total_rows) * 100
facebook_strange_percentage = (facebook_strange_count / facebook_total_rows) * 100
website_strange_percentage = (website_strange_count / website_total_rows) * 100

# Step 5: Print the results
print("\nNon-ascii characters in 'Company Name' column:")
print(f"Google: {google_strange_count} rows, {google_strange_percentage:.2f}% of total rows")
print(f"Facebook: {facebook_strange_count} rows, {facebook_strange_percentage:.2f}% of total rows")
print(f"Website: {website_strange_count} rows, {website_strange_percentage:.2f}% of total rows")

# save the cleaned dataset to a new CSV file
google_df.to_csv('FINAL/new_google_dataset.csv', index=False)
facebook_df.to_csv('FINAL/new_facebook_dataset.csv', index=False)
website_df.to_csv('FINAL/new_website_dataset.csv', index=False)