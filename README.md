# How to run the program
 NOTE: A well knowlege of python and SQL required to be able to run this code
##### Step one: prepare the software
* install vagrant last version
* install virtual box
* install python
* up the machine into vagrant
* import all the necessary libraries
##### Step two: Download the data
* download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
* To run the python file, `cd` into the `vagrant` and login to your vm ( `vagrant up`; `vagrant ssh`) :
 and use the command:
`python newsdata.py`.
##### If you want to : Explore the data
Once you have the data loaded into your database, connect to your database using `psql -d news` and explore the tables using the `\dt` and `\d` table commands and select statements.

`\dt` ? display tables ? lists the tables that are available in the database.
`\d table` ? (replace table with the name of a table) ? shows the database schema for that particular table.
# description of the program's design
This program is designed using the mentioned softwares in the previous section step one 
By: Aya Muhammad.
following the Udacity's instructions mentioned in Full stack web development nd.
for more information about the design email me at: Ayaengineera2015@gmail.com
