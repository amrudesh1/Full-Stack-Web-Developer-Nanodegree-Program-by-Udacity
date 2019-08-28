1. Project description
	
	You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
he database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

2. List of dependencies
	
	1.PostgreSQL
	2.Python
	3.Windows/Linux Machine

3. For accessing the database you need to run the queries inside the SQL file it can be done using the following command 
	1.psql -d news -f newsdata.sql

4. The SQL is included in this project in a Zip File Please download it and extract it.

5. For importing the data to PostgreSQL as mentioned above use the following command Please make sure that the database is created while exporting the data 
  	1.psql -d news -f newsdata.sql

6. The Database consist of 3 tables as following:
    1. The authors table includes information about the authors of articles.
    2. The articles table includes the articles.
    3. The log table includes one entry for each time a user has accessed the site indicates whether the request succeeded or failed.

7. The project consist of 3 main functions as following:
   1. The get_top_articiles_fromDB to get the top 3 articles in number of views.
   2. The get_popular_article_authors_fromDB to get the authors ordered by the number of the views of their articles.
   3. The get_fail_days_fromDB to get the days on which the requests lead to more than 1% errors.

8. How to run the project:
  1. You should have the Postgresql installed on your machine download it from [here](https://www.postgresql.org/download/).
  2. You need to create a database and the 3 tables and the view download this [archieve](https://github.com/amrudesh1/Full-Stack-Web-Developer-Nanodegree-Program-by-Udacity/blob/master/Project%201/newsdata.zip) extract the sql file which contains the statements for creating the tables then execute the create view statement.
  3. You need to have python 3 installed download from [here](https://www.python.org/downloads/).
  4. From the command line cd to the project location and run "python3 query.py".