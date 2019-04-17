# Assignment1
Logs Analysis

# Connecting to the database and importing news database 
1. You can connect to the database named "new", to check its existence by typing 
``` psql news```
2. If not present, you can create the news database by typing
``` create database news```
3. Once  psql -d news -f newsdata.sqlyou have the databse you can insert the news data by using below command
``` psql -d news -f newsdata.sql ```  
This will copy the news data sql into your database and now we are all set for our assignment.


# Creating a sql view for the first two questions of the assignent.
Please run the below sql in your news db database which creates a view named _mainview_

```
create view mainview as select authors.name as name, articles.slug as articletitle, log.path as articlepath,log.status as status, log.time as time from authors,articles,log where articles.author = authors.id and log.path = concat('/article/',articles.slug);
```
This view contains 5 columns - author name, article title, path of that article , status in accessing that article(which will be 200 in this view as we are always considering valid path), and the time at which that article is accessed. 

## Running the program
 Usercan run the program as shown below and see the output in console
 
 ```
 python Assignment1.py
 
 ```
 1. The program does not expect any user input. 
 2. It expects a valid news database to be present and the _mainview_ mentioned in previous section to be present.
 
 
