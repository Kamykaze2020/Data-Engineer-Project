import pandas as pd
import unidecode
import re

# Load the datasets with low_memory=False
google_df = pd.read_csv('FINAL/new_google_dataset.csv', on_bad_lines='skip', low_memory=False)
facebook_df = pd.read_csv('FINAL/new_facebook_dataset.csv', on_bad_lines='skip', low_memory=False)
website_df = pd.read_csv('FINAL/new_website_dataset.csv', on_bad_lines='skip', low_memory=False)


merged_df = pd.merge(facebook_df, google_df, on='Company Name', how='outer', suffixes=('_facebook', '_google'))
#merged_df = pd.merge(facebook_df, google_df, how='outer', suffixes=('_facebook', '_google'))

print("\n")
print(merged_df)

merged_df = pd.merge(merged_df, website_df, on='Company Name', how='outer', suffixes=('', '_website'))
#merged_df = pd.merge(merged_df, website_df, how='outer')

merged_df.to_csv('FINAL/final_merged.csv', index=False)