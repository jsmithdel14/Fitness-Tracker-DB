# SQL Database - Fitness Tracker


The software I wrote is a python program that incorporate sql to create a table for a database, as well as querying or searching through the table and data. The program has a few main features, the first is to allow myself to store personal workout progress by being able to add to the database my daily workouts, time, as well as adding things like how much sleep and calories I am getting every day. There is the ability to look at past days, add days, update any past days, delete past days, and even a simple function that allows the user what workout they should do that day based on the results they have entered. In order to look at what the user should do for the day you can just simply hit the "Tell Me What To Do Today" command and then enter your name and the data base will sort through the table and return the users results, aswell as returning the workout they should do. The program will tell you what workout to do based on which workout has the lowest count, which will automatically be sorted to the top of the list.  

### Purpose of writing this program

The purpose for writing this software aside from having a personal fitness tracker I can use was to gain a better understanding on creating databases, and then using that database to make a table. I wanted to expand on my very little sql knowledge by learning how to use mainly sql commands to query data. Another goal of this project was to learn how I can make a function that uses sql and implement that into a project. Learning how to add, update and delete things from a database using sql was a great result of this project. I also wanted to get a better understanding of using groupby's in sql and aggregate functions like the count() or min() functions in sql. 

# Demo

[Software Demo Video](https://youtu.be/DCB5uuuwEX8)

# Relational Database

### Relational database and structure of the database created

The relational database I am using is just a standard database.

There is only one table in the relational database that I created. The table is called "fitness" and this table is created only if the table does not already exists that way it doesn't run into errors anytime the program is ran and the table will only be created once. The table has 6 columns: name (text), date(text), time(real), workout(text), calories(integer), and sleep(real). The user inserts something for each of these columns when added a row or new input into the table. 

# Development Environment

### Tools used to develop software:

I used replit and visual studio code to develope the software. I found that replit made it easier to work on multiple devices so I did the majority of the project on replit.

### Programming langauge and libraries:

Python and SQL were the main programming languages

sqlite3 had to imported as a library to use SQL commands.

# Useful Websites

* [Python sqlite3](https://docs.python.org/3.8/library/sqlite3.html)
* [Relational Databases - Wikipedia](https://en.wikipedia.org/wiki/Relational_database)
* [w3schools](https://www.w3schools.com/sql/)

# Future Work

* I need to fix how the program finds the user, right now it finds the user by name but if more people were using this software anyone with the same name would run into a problem, and have inaccurate data as the results would be the results of anyone with that name. To fix this I will need to have the users have a unique username that I can use to query only their workout results.
* Because the goal of this project was to really focus on using on SQL commands I spent the most time working on my get_workout function where I planned on using the most sql commands and aggregate functions, so other functions I hard coded fast and copy pasted a lot of code that could be cleaned up to reduce the amount of times I reuse long lines of code.
* I also think that by adding more functionality to my program would make it vastly better right now it has a very limited capacity of what it can do. 
* The general logic of the program could be improved upon for better workout recommendations.
