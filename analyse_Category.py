import pandas as pd
import re

# Load the datasets with low_memory=False
google_df = pd.read_csv('datasets/google_dataset.csv', on_bad_lines='skip', encoding='utf-8', low_memory=False)
facebook_df = pd.read_csv('datasets/facebook_dataset.csv', on_bad_lines='skip', low_memory=False)
website_df = pd.read_csv('datasets/website_dataset_2.csv', on_bad_lines='skip', low_memory=False)
website_df = website_df.loc[:, ~website_df.columns.str.contains('^Unnamed')]

# Print columns to debug
print("Google Columns:", google_df.columns.tolist())
print("Facebook Columns:", facebook_df.columns.tolist())
print("Website Columns:", website_df.columns.tolist())


# Define new names based on categories
google_rename_map = {
    'category': 'Category',
    'address': 'Address',
    'city': 'City',
    'region_name': 'Region',
    'country_name': 'Country',
    'phone': 'Phone',
    'name': 'Company Name',
    'domain': 'Domain'
}

facebook_rename_map = {
    'categories': 'Category',
    'address': 'Address',
    'city': 'City',
    'region_name': 'Region',
    'country_name': 'Country',
    'phone': 'Phone',
    'name': 'Company Name',
    'domain': 'Domain'
}

website_rename_map = {
    'site_name': 'Company Name',
    'main_city': 'City',
    'main_region': 'Region',
    'main_country': 'Country',
    'phone': 'Phone',
    'root_domain': 'Domain',
    's_category': 'Category'
}

# Rename columns
google_df.rename(columns=google_rename_map, inplace=True)
facebook_df.rename(columns=facebook_rename_map, inplace=True)
website_df.rename(columns=website_rename_map, inplace=True)

# Print renamed columns to verify
print("\n")
print("Renamed Google Columns:", google_df.columns.tolist())
print("Renamed Facebook Columns:", facebook_df.columns.tolist())
print("Renamed Website Columns:", website_df.columns.tolist())

# Convert category to lowercase in all dataframes
google_df['Category'] = google_df['Category'].str.lower()
facebook_df['Category'] = facebook_df['Category'].str.lower()
website_df['Category'] = website_df['Category'].str.lower()

# Get total number of rows in each dataset
google_total_rows = len(google_df)
facebook_total_rows = len(facebook_df)
website_total_rows = len(website_df)

# Check for duplicates in each dataset

# Calculate the percentage of NaN values in 'Category' column
google_duplicates_percentage = (google_df['Category'].duplicated().sum() / google_total_rows) * 100
facebook_duplicates_percentage = (facebook_df['Category'].duplicated().sum() / facebook_total_rows) * 100
website_duplicates_percentage = (website_df['Category'].duplicated().sum() / website_total_rows) * 100

# Print the results
print("\nDuplicate values in 'Category' column:")
print(f"Google: {google_df['Category'].duplicated().sum()} duplicates, {google_duplicates_percentage:.2f}% of total rows")
print(f"Facebook: {facebook_df['Category'].duplicated().sum()} duplicates, {facebook_duplicates_percentage:.2f}% of total rows")
print(f"Website: {website_df['Category'].duplicated().sum()} duplicates, {website_duplicates_percentage:.2f}% of total rows")



# Count the number of NaN values in the 'Category' column
google_nan_count = google_df['Category'].isna().sum()
facebook_nan_count = facebook_df['Category'].isna().sum()
website_nan_count = website_df['Category'].isna().sum()

# Calculate the percentage of NaN values in 'Category' column
google_nan_percentage = (google_nan_count / google_total_rows) * 100
facebook_nan_percentage = (facebook_nan_count / facebook_total_rows) * 100
website_nan_percentage = (website_nan_count / website_total_rows) * 100

# Print the results
print("\nNaN values in 'Category' column:")
print(f"Google: {google_nan_count} NaNs, {google_nan_percentage:.2f}% of total rows")
print(f"Facebook: {facebook_nan_count} NaNs, {facebook_nan_percentage:.2f}% of total rows")
print(f"Website: {website_nan_count} NaNs, {website_nan_percentage:.2f}% of total rows")

# Detect strange characters using regex on Category column

# Step 1: Define a function to detect non-ASCII characters in a string
def contains_non_ascii(text):
    if pd.isna(text):
        return False
    # Regex to match non-ASCII characters (characters outside the range of 0-127)
    return bool(re.search(r'[^\x00-\x7F]', text))

# Step 2: Apply this function to detect strange characters in the 'Category' column for each dataset
google_strange = google_df['Category'].apply(contains_non_ascii)
facebook_strange = facebook_df['Category'].apply(contains_non_ascii)
website_strange = website_df['Category'].apply(contains_non_ascii)

# Step 3: Count how many rows contain strange characters
google_strange_count = google_strange.sum()
facebook_strange_count = facebook_strange.sum()
website_strange_count = website_strange.sum()

# Step 4: Calculate the percentage of rows with strange characters
google_strange_percentage = (google_strange_count / google_total_rows) * 100
facebook_strange_percentage = (facebook_strange_count / facebook_total_rows) * 100
website_strange_percentage = (website_strange_count / website_total_rows) * 100

# Step 5: Print the results
print("\nNon-ascii characters in 'Category' column:")
print(f"Google: {google_strange_count} rows, {google_strange_percentage:.2f}% of total rows")
print(f"Facebook: {facebook_strange_count} rows, {facebook_strange_percentage:.2f}% of total rows")
print(f"Website: {website_strange_count} rows, {website_strange_percentage:.2f}% of total rows")