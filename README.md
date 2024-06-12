# statesdatabase
Project Information:

I created a Python script that downloads csv files which are used to read specific columns to insert into a database. Another Python script is created to search the database without going into the mySQL database. 

Initialize Project Steps:

First, download all of the files and put them in the same folder. Open your preferred IDE and open the folder that has all of the files stored. 

The requirements.txt file has the libraries and versions that are used. The setup.sh bash file will download the libraries that are in the requirements.txt file.

Running setup.sh:

To run the setup.sh file, make sure you are in the folder with all of the files and type "./setup.sh" (without the quotation marks) in the terminal. A log file will be created that has the installation results. 

Running statecsv.py:

This is the file that deletes and inserts the data into the database from the csv files. To run this file, type "python statecsv.py" in the terminal. Make sure you are in the correct folder. You will have to input the database information.

Running search_database.py: 

This is the file that allows the user to search within the database using a python script. To run this file, type "python search_database.py" in the terminal. Make sure you are in the correct folder. You will have to input the database information.
