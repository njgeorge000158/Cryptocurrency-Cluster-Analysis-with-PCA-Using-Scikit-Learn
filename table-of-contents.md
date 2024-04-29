# UK-Food-Magazine-Restaurant-Analysis-using-NoSQL-and-MongoDB

----

## Table of Contents (mongodb_setup.ipynb)

----

# <br><br>  **Section 1: Database Connection**
> ## <br> **1.1: MongoDB Client**
> ## <br> **1.2: MongoDB Database**
> ## <br> **1.3: MongoDB Collection**
> ## <br> **1.4: Populate MongoDB Collection**
> ## <br> **1.5: MongoDB Database Confirmation**
> ## <br> **1.6: MongoDB Collection Confirmation**
> ## <br> **1.7: Establishments Collection Document Review**
# <br><br> **Section 2: Update the Database**
> ## <br> **2.1 — An exciting new halal restaurant just opened in Greenwich, but hasn't been rated yet. The magazine has asked you to include it in your analysis. Add the following restaurant "Penang Flavours" to the database.**
>> ### **New Restaurant Dictionary**
>> ### **Insert New Restaurant Dictionary into MongoDB Collection**
>> ### **New Restaurant Document Confirmation**
> ## <br> **2.2 — Find the BusinessTypeID for "Restaurant/Cafe/Canteen" and return only the `BusinessTypeID` and `BusinessType` fields.**
>> ### **Query Results**
> ## <br> **2.3 — Update the new restaurant with the `BusinessTypeID` you found.**
>> ### **Correct BusinessTypeID Update**
>> ### **Correct BusinessTypeID Confirmation**
> ## <br> **2.4 — The magazine is not interested in any establishments in Dover, so check how many documents contain the Dover Local Authority. Then, remove any establishments within the Dover Local Authority from the database, and check the number of documents to ensure they were deleted.**
>> ### **Number of Documents with `LocalAuthorityName` as 'Dover’**
>> ### **Delete Documents with Dover as `LocalAuthorityName`**
>> ### **Deletion Confirmation**
>> ### **PyMongo Function, `find_one`, Checks For Other Documents**
> ## **2.5 — Some of the number values are stored as strings, when they should be stored as numbers.**
>> ### **PyMongo Subroutine, `update_many`, Converts `latitude` And `longitude` To Numbers.**
>> ### **PyMongo Subroutine,  `update_many`, Converts `RatingValue` To Integer Numbers**
>> ### **Data Conversion Check**
>> ### **`latitude` Data Conversion Check**
>> ### **`longitude` Data Conversion Check**
>> ### **`RatingValue` Data Conversion Check**

----

## Table of Contents (restaurant_analysis.ipynb)

----

# <br><br> **Section 1: Database Connection**
> ## <br> **1.1: MongoDB Client**
> ## <br> **1.2: MongoDB Database Confirmation**
> ## <br> **1.3: MongoDB Database**
> ## <br> **1.4: MongoDB Collection Confirmation**
> ## <br> **1.5: MongoDB Collection**
# <br><br> **Section 2: Exploratory Analysis**
> ## <br> **2.1 — Which establishments have a hygiene score equal to 20 (the worst possible rating)?**
>> ### **Number of Establishments from `count_documents`**
>> ### **Display First Document**
>> ### **Worst Hygiene Establishments Data Set**
>> ### **Number of Rows in Worst Hygiene Establishments Data Set**
>> ### **Worst Hygiene Establishments' Locations Data Set**
>> ### **Display Worst Hygiene Establishments**
>> ### **Display Worst Hygiene Establishments' Locations**
> ## <br> **2.2 — Which establishments in London have a high rating value greater than or equal to 4 (1-5)?**
>> ### **Number of Establishments from `count_documents`**
>> ### **Display First Document**
>> ### **High Rating Value, London Establishments Data Set**
>> ### **Number of Rows in High Rating Value, London Data Set**
>> ### **High Rating Value, London Establishments' Locations Data Set**
>> ### **Display High Rating Value, London Establishments**
>> ### **Display High Rating Value, London Establishments' Locations**
> ## <br> **2.3 — What are the top 5 establishments with a rating value of 5, sorted by best hygiene score, nearest to the new restaurant added, "Penang Flavours?**
>> ### **Penang Flavours' Latitude and Longitude**
>> ### **Query Search Range Variables**
>> ### **Query Results**
>> ### **Number of Establishments from `count_documents`**
>> ### **Display All Documents**
>> ### **Highest Rating, Best Hygiene Establishments Data Set**
>> ### **Number of Rows in Highest Rating, Best Hygiene Establishments Data Set**
>> ### **Highest Rating, Best Hygiene Establishments' Locations Data Set**
>> ### **Display Highest Rating, Best Hygiene Establishments**
>> ### **Display Highest Rating, Best Hygiene Establishments' Locations**
> ## <br> **2.4 — How many establishments in each Local Authority area have a hygiene score of 0 (the best possible rating)? Sort the number of establishments from highest to lowest, and print out the top ten local authority areas.**
>> ### **Aggregation Query Parameters**
>> ### **Aggregation Query Results**
>> ### **Number of Authorities and Establishments from Aggregation Query Results**
>> ### **Number of Authorities and Establishments from `count_documents`**
>> ### **Display Documents**
>> ### **Highest Hygiene Establishments Data Set**
>> ### **Number of Rows in Highest Hygiene Establishments Data Set**
>> ### **Display Highest Hygiene Establishments**

----

## Copyright

Nicholas J. George © 2023. All Rights Reserved.
