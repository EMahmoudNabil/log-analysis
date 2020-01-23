# Log Analysis Project

## Description
A reporting tool that prints out reports (in plain text) based on the data in a newspaper log database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

### How to Run the Program

#### Requirements
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup Project:
  1. Install Vagrant and VirtualBox, Please check [instructions to install the virtual machine](https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
  2. Download or Clone this repository in the /vagrant directory **You must finish step 1 first**.
  #### Prepare the Software and Data
 1. The virtual machine from step 1
 
       If you need to bring the virtual machine back online with `$ vagrant up`. Then log into it with `$ vagrant ssh`
 2. Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
    1. Unzip this file after downloading it. The file inside is called newsdata.sql.
    2. To run the reporting tool, you'll need to load the site's data into your local database. To load the data, use the command 
        ```
        psql -d news -f newsdata.sql
        ```
    3. The database includes three tables:
        - The `authors` table includes information about the authors of articles.
        - The `articles` table includes the articles themselves.
        - The `log` table includes one entry for each time a user has accessed the site.
 3. Creating Views:
    1. Use `psql -d news` to connect to database.
    2. create view `top_articles` using:
        ```sql
        CREATE VIEW top_articles AS
          SELECT b.title,
                 count (*),
               
                 
          FROM  articles AS b
          JOIN log AS c
                ON substring(path,10,length(path)) = b.slug
          GROUP BY b.title
          ORDER BY count(*) DESC
LIMIT 3;;
#### Run the Tool :boom:
1. From the vagrant directory inside the virtual machine, run `loganalysis.py` using: 
    ```
    $ python3 loganalysis.py
    ```
2. Check the output file for the results `output.txt`

##### For more understanding please check the [PostgreSQL documentation](https://www.postgresql.org/docs/current/static/index.html)
- [The select statement](https://www.postgresql.org/docs/9.5/static/sql-select.html)
- [SQL string functions](https://www.postgresql.org/docs/9.5/static/functions-string.html)
- [Aggregate functions](https://www.postgresql.org/docs/9.5/static/functions-aggregate.html)
- [CREATE CAST](https://www.postgresql.org/docs/9.5/static/sql-createcast.html)
- [Data Type Formatting Functions](https://www.postgresql.org/docs/9.5/static/functions-formatting.html)

  


Questions answered by the program:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Files
- loganalysis.py
- readme.md
- sample_output.txt

## Usage
Run the `python loganalysis.py` file within a python shell, which will print the analysis out to the command line

## Links

### License
MIT License

### Author
Chris Baines
