import pandas as pd
import re

# Load the datasets with low_memory=False
website_duplicates = pd.read_csv('NEWDATASET/website_duplicates.csv', on_bad_lines='skip', low_memory=False)

# Replace empty spaces in 'Company Name' with NaN
website_duplicates['Company Name'] = website_duplicates['Company Name'].replace('', pd.NA)  # Convert empty strings to NaN

# Fill NaN values in 'Company Name' with corresponding values from 'legal_name'
website_duplicates['Company Name'] = website_duplicates['Company Name'].fillna(website_duplicates['legal_name'])

# Function to extract the name part of a domain (remove suffix like '.com', '.org', etc.)
def extract_domain_name(domain):
    if pd.isna(domain):
        return domain
    return re.sub(r'\.\w{2,}', '', domain.split('.')[0])

# Fill NaN values in 'Company Name' with corresponding values from 'Domain', extracting only the main part of the domain
website_duplicates['Company Name'] = website_duplicates['Company Name'].fillna(website_duplicates['Domain'].apply(extract_domain_name))

# Convert company names to lowercase in all dataframes
website_duplicates['Company Name'] = website_duplicates['Company Name'].str.lower()

# Save the modified duplicates to a new CSV file
website_duplicates.to_csv('NEWDATASET/website_duplicates_modified.csv', index=False)