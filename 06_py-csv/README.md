# Trio of Success: Raymond Yeung, Annabel Zhang, Thomas Yu
# SoftDev
# Explanation of K06
# 2021-09-29
---

### CSV Input and Output
* A CSV file separates values of individual columns by commas, and organizes data into a table/spreadsheet
* In a text editor the file will have commas to separate the data in each row
* Each line of the file represents a row in the spreadsheet/table
* Commas not within quotations determine when one data value ends and the next in the row starts
* Commas within quotations don’t separate the line as they are part of the string
* The first row is usually a table heading

### Dictionary
* An object that allows the user to store data in key:value pairs
* Keys cannot be changed once set and there can only be one in the dictionary while values can be altered
* It allows you to return back a value based on the stored key
* Can store different types of data.
* It will keep the order in which the key:value pairs are added to the dictionary

### List
* An ordered collection of data values
* Can hold data values of different types
* It can refer to each element via a number index that corresponds to its location in the list
* Each element of the list can be gotten, removed, or altered
* It doesn't require prior declaration

### Github-Flavored Markdown
* Learn by example
* [This may be useful.](https://guides.github.com/features/mastering-markdown/)

### Weighted Randomized Selection
* Weighted Randomized Selection
* The percentages add up to a total of 99.8, so we generated a random float between 0 (inclusive) and 99.8 (exclusive)
* By creating intervals, we created sets of values that each refer to a different job. When the randomly generated float is within the interval, it will return the corresponding job.
* By changing the size of these intervals, we can alter the probability of that job being returned.
* The size of each interval would be the Percentage that corresponds to the Job Class.
* With variables for the lower and upper bounds of the intervals, we can keep updating the interval and checking whether the random float falls within the interval.
* By the time we reach the end of the dictionary (Total : 99.8) a job will have been printed.
