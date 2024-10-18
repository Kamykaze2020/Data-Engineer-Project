# Data-Engineer-Project

### The assignment

The input for this assignment is an archive (download [**here**](https://drive.google.com/file/d/1jF7lnMUffCX8U252MoY7jowb7VedFOp8/view?usp=sharing)) containing 3 datasets with data about the same companies from 3 different sources: 

1. Facebook (facebook dataset.csv)
2. Google (google dataset.csv)
3. Company Website (website dataset.csv)

The final purpose of this exercise is to create a 4th dataset that contains the other 3 and, by joining them, we should reach a better accuracy on common columns. The columns that interest us the most are Category, Address (country, region...), Phone, Company names.

## The solution

Firstly we will analyse the data to see how many rows are that have duplicate names, special characters nan values, or other problems that may make our data create more rows after we will make an outer join. We will use an outer join because we don’t want to lose data.

We need to clean the data from all the files to be able to make a merger.  We will look for duplicate names, special characters, nan values, or other problems that may make our data create more rows after we will make an outer join.

The comlumns that interest us most are Category, Address (country, region...), Phone, Company names. So we will go through each one to to make procentages to show us how many rows with duplicate names, special characters(non-ascii characters), NaN values are on each column.

I prioritized looking into the columns for the merger as follows: ‘Company Name’ > ‘Phone’ > ‘Category’ > ‘Address(country, region…)’, because I belive in the ‘Company Name’ and ‘Phone’ categories there appear the least typo errors when people insert data into a table.


### Company Name column

I changed all the rows to lowercase to prevent cases where data has wrong uppercase characters. 

We see a pretty low percentage for duplicate values, the highest being in the Website dataset and occuping a percentag of 10.37% of the total rows.

The NaN values have an even lower number, the highest occuping a percentage of 8.84% of total rows from the Website dataset.

Non-ascii characters occupy a small percentage of the datasets, the highest beeing in the Website dataset, occuping 7.66% of total rows, but they need to be corected so that when we make the outer join there won’t appear more rows.
