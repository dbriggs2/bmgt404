# Creating the SQLite database

If you haven't already, download and install [sqlite3](https://www.sqlite.org/download.html). This is what we will be using to locally run our database. You'll also need the Python [sqlite3 module](https://docs.python.org/2/library/sqlite3.html) which should come installed with Python automatically.

1. Download the `create.sql` file and save it to the folder where your code is stored.

2. From the command line, navigate to the directory where the `create.sql` file exists and run the following command: 

    `sqlite3 schedule.db < create.sql`

3. This will create a file called `schedule.db`. This file has the database that you will connect to with Python. Use the Python SQLite tutorial to learn how to connect to a SQLite database with Python.