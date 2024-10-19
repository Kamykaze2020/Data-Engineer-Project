import pandas as pd
import re

# Load the datasets with low_memory=False
google_df = pd.read_csv('NEWDATASET/new_google_dataset.csv', on_bad_lines='skip', encoding='utf-8', low_memory=False)
facebook_df = pd.read_csv('NEWDATASET/new_facebook_dataset.csv', on_bad_lines='skip', low_memory=False)
website_df = pd.read_csv('NEWDATASET/new_website_dataset.csv', on_bad_lines='skip', low_memory=False)

# Get total number of rows in each dataset
google_total_rows = len(google_df)
facebook_total_rows = len(facebook_df)
website_total_rows = len(website_df)

# Identify and save duplicates from each dataset
google_duplicates = google_df[google_df['Company Name'].duplicated(keep=False)]
facebook_duplicates = facebook_df[facebook_df['Company Name'].duplicated(keep=False)]
website_duplicates = website_df[website_df['Company Name'].duplicated(keep=False)]

# Print the number of duplicate rows found in each dataset
print("\nDuplicate values kept from 'Company Name' column:")
print(f"Google: {len(google_duplicates)} duplicates saved")
print(f"Facebook: {len(facebook_duplicates)} duplicates saved")
print(f"Website: {len(website_duplicates)} duplicates saved")

# Replace empty spaces in 'Company Name' with values from 'legal_name'
# Delete this to show the empty rows
# website_duplicates['Company Name'] = website_duplicates['Company Name'].replace('', pd.NA)  # Convert empty strings to NaN
# website_duplicates['Company Name'].fillna(website_duplicates['legal_name'], inplace=True)

# Save the duplicate rows to new CSV files
google_duplicates.to_csv('NEWDATASET/google_duplicates.csv', index=False)
facebook_duplicates.to_csv('NEWDATASET/facebook_duplicates.csv', index=False)
website_duplicates.to_csv('NEWDATASET/website_duplicates.csv', index=False)

# Remove the duplicates from the original datasets
google_cleaned = google_df.drop_duplicates(subset='Company Name', keep=False)
facebook_cleaned = facebook_df.drop_duplicates(subset='Company Name', keep=False)
website_cleaned = website_df.drop_duplicates(subset='Company Name', keep=False)

# Print the number of rows remaining after removing duplicates
print("\nRows remaining after removing duplicates:")
print(f"Google: {len(google_cleaned)} rows remaining")
print(f"Facebook: {len(facebook_cleaned)} rows remaining")
print(f"Website: {len(website_cleaned)} rows remaining")

# Save the cleaned datasets (without duplicates) to new CSV files
google_cleaned.to_csv('CLEANED/google_cleaned.csv', index=False)
facebook_cleaned.to_csv('CLEANED/facebook_cleaned.csv', index=False)
website_cleaned.to_csv('CLEANED/website_cleaned.csv', index=False)

