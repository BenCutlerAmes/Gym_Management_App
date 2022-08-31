# Gym Project

This project represents the end of 4 weeks of study at CodeClan.

It was a solo project making a full-stack application.

## Given MVP

    The app should allow the gym to create and edit Members
    The app should allow the gym to create and edit Classes
    The app should allow the gym to book members on specific classes
    The app should show a list of all upcoming classes
    The app should show all members that are booked in for a particular class
    
 ## Prerequisites
 - Flask
 - Psycopg2
 
 ## Initialisation
 #### Note: the following uses a database titled 'gym_management'. If you already have a database with that name, you can change the name in the gym_managament.sql file and adapt the following code.
 
 
### Run the following code from a terminal in the 'gym_management' folder
 ```
 dropdb gym_management
 createdp -d gym_management -f db/gym_management.sql
 flask run
 ```
 Optional - populate the database with mock data to show functionality
 ```
 python3 console.py
 ```



