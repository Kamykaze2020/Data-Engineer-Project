# Data-Engineer-Project

### The assignment

The input for this assignment is an archive (download [**here**](https://drive.google.com/file/d/1jF7lnMUffCX8U252MoY7jowb7VedFOp8/view?usp=sharing)) containing 3 datasets with data about the same companies from 3 different sources: 

1. Facebook (facebook dataset.csv)
2. Google (google dataset.csv)
3. Company Website (website dataset.csv)

The final purpose of this exercise is to create a 4th dataset that contains the other 3 and, by joining them, we should reach a better accuracy on common columns. The columns that interest us the most are Category, Address (country, region...), Phone, Company names.

## The solution

Firstly we will analyse the data to see how many rows are that have **duplicate names, special characters nan values**, or other problems that may make our data create more rows after we will make an outer join. We will use an outer join because we don’t want to lose data.

We need to clean the data from all the files to be able to make a merger.  We will look for **duplicate names, special characters, nan values**, or other problems that may make our data create more rows after we will make an outer join.

The comlumns that interest us most are **Category**, **Address (country, region...)**, **Phone**, **Company names**. So we will go through each one to to make procentages to show us how many rows with **duplicate names, special characters(non-ascii characters), NaN values** are on each column.

I prioritized looking into the columns for the merger as follows: **‘Company Name’ > ‘Phone’ > ‘Category’ > ‘Address(country, region…)’**, because I belive in the ‘Company Name’ and ‘Phone’ categories there appear the least typo errors when people insert data into a table.

<br/><br/>
### Company Name column

![image](https://github.com/user-attachments/assets/576bb4a1-923f-4251-9b9f-f35dd4945dd7)

I changed all the rows to lowercase to prevent cases where data has wrong uppercase characters. 

We see a pretty low percentage for duplicate values, the highest being in the Website dataset and occuping a percentag of 10.37% of the total rows.

The NaN values have an even lower number, the highest occuping a percentage of 8.84% of total rows from the Website dataset.

Non-ascii characters occupy a small percentage of the datasets, the highest beeing in the Website dataset, occuping 7.66% of total rows, but they need to be corected so that when we make the outer join there won’t appear more rows.


<br/><br/>
### Phone column

![image](https://github.com/user-attachments/assets/534a2443-fd12-4ba6-9e3f-f7474dbecfa7)

I’ve ensured that all the phone numbers are treated as stirngs and removed any non-numeric characters that may appear.

There is a high percentage of duplicates in the ‘Phone’ column, the highest beeing 37.79% of the total rows in the Facebook dataset.

There are no NaN values or Non-ascii characters which is very good.


<br/><br/>
### Category column

![image](https://github.com/user-attachments/assets/4c325285-599f-4b05-9534-092d84baa676)

I’ve converted all rows to lowecase to prevent cases where data has wrong uppercase characters.
In this column we see an extremely big percentage of duplicates in the Google dataset and Website dataset with a percentage of 99.86%, respectively 99.22%. Which will heavely affect our data when we make an outer join based on this column.
The NaN values are not as much present but still occupy a large enough amount, the highest beeing in the Facebook dataset, representing a 23.29% of all the total rows.
I can’t find Non-ascii characters in this column.

The conclusion I can deduce is that the ‘Company Name’ column is the best column on wich we can make an outer join between the datasets.

<br/><br/>
## Processing the duplicates


We should try to remove the duplicates, but we should be careful not to lose data, for that I consider that a Fuzzy Matching for Duplicate-Like Entries should work alright, when we find a row where data matches with a threshold of a 80% similarity we should keep the first row and discard the other. We will use th fuzzywuzzy library in Python.

Initialy I tried, to make a Fuzzy Matching for Duplicate-Like Entries, but considering there are as high as 300.000 rows in the datasets, even if we try to use the RapidFuzz it would still take days to finish because of the sheer number of comparisons involved. A newarest neightbors(ann) solution creates the same issue. I tried to do a batch processing, but the solution still takes to much time.

Given the fact that I only need to work with the duplicates I decided to extract them in a separate dataset and delete them from the original so that after I clean the duplicates I can add them again in the dataset.

![image](https://github.com/user-attachments/assets/5d355f78-8d3e-4429-a2f0-03ce987cff36)

![image](https://github.com/user-attachments/assets/39c269c2-b97b-45d8-aba3-6660ffe34ac0)

We saved the datasets, now I need to clean the duplicates. In the website dataset, there are a lot of empty fields in the ‘Company Name’ but there is a separate column named ‘leagal_name’ that can be used as a replacement, so I wrote a code to replace the empty spaces with the name from the ‘legal_name’ column.

![image](https://github.com/user-attachments/assets/e5b12813-884d-4420-8b8a-d8b9bdf8f30a)

There still remain a lot of empty rows that only have ‘Domain’ and ‘Category’ but there is not really a lot of information to fill the gaps inside the dataset. Rather than eliminate those rows I decided to use the name of the domain from the ‘Domain’ column to replace the empty spaces on the ‘Company Name’ row because most of the time the domain name is similar, if not the same, with the Company Name.

![image](https://github.com/user-attachments/assets/e42ec784-c674-4519-af43-15f19e398b8c)

I analyse the datasets with the duplicate entries. We see that we have a good result for the empty spaces inside the dataset.

![image](https://github.com/user-attachments/assets/295e9a58-1353-47ef-ab77-265edd81d499)

So that I don’t lose important data I decided to make a Fuzzy Matching for Duplicate-Like Entries on 3 columns: ‘Company Name’, ‘Phone’ and ‘Category’, when we find a row where data matches with a threshold of a 80% similarity on all colums we keep the first row and discard the other. We can play with this values to obtain a better result, we can lower the similarity percentage for different results.


After Fuzzy(80% similarity)|  Before Fuzzy
:-------------------------:|:-------------------------:
![image](https://github.com/user-attachments/assets/396f4b3e-db56-4346-8d16-c4e9b2c044ba)  |  ![image](https://github.com/user-attachments/assets/0a1a3c75-ca79-426f-8cc0-831937533dc5)


After the algorithm with a 80% similarity is implemented we see a reduction in the number of duplicate rows inside the duplicate dataset with a reduction varying between 2.3% - 8.78%, which is not a very high reduction.

I run the algorithm again with a 70% similarity and we obtain the results below.


After Fuzzy(70% similarity)|  Before Fuzzy
:-------------------------:|:-------------------------:
![image](https://github.com/user-attachments/assets/1cba64ee-d4c1-466d-b440-72b6b80bbfe6)  |  ![image](https://github.com/user-attachments/assets/0a1a3c75-ca79-426f-8cc0-831937533dc5)

I run the algorithm again with a 60% similarity and we obtain the results below.

After Fuzzy(60% similarity)|  Before Fuzzy
:-------------------------:|:-------------------------:
![15](https://github.com/user-attachments/assets/1f6dc8e3-1b44-4cac-b3c3-41ed3c8ba065)    |  ![image](https://github.com/user-attachments/assets/0a1a3c75-ca79-426f-8cc0-831937533dc5)

With a 60% similarity we can see a reduction as high as 24.48% within the dataset.

Next we will append the cleaned data to our original dataset. The results after the append are shown in the image below.

![image](https://github.com/user-attachments/assets/fd129c23-7c91-4538-9a83-b3c71b8757ef)

Now we should replace non-ascii characters. We can use the unicode library to replace special characters with their ASCII equivalents.

![image](https://github.com/user-attachments/assets/07075b30-e74f-4cab-b932-5f9a6f2982cb)

![image](https://github.com/user-attachments/assets/4716c6ad-66b2-4dd4-b495-d2a266c68722)


Now that I cleaned the data I will make on outer join with all the datasets.

The final data is stored in the file **‘final_merged.csv’**. Due to the file size beeing more than 25mb I stored it on drive, you can access it by following this link: https://drive.google.com/file/d/141HgbEtGxoCs8XRdFD9IwqMyP46oxa5l/view?usp=drive_link




