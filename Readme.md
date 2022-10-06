# Gym Project

This project represents the end of 4 weeks of study at CodeClan.

It was a solo project making a full-stack application and represents 6 days of work.

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
 ## Screenshots
 ![image](https://user-images.githubusercontent.com/93072051/194393666-a4e00028-bf17-4eea-82e4-c7de48043678.png)
<img width="1373" alt="Screenshot 2022-09-12 at 22 44 26" src="https://user-images.githubusercontent.com/93072051/194393690-7370d076-9506-492b-9940-9834d6ff0d7e.png">
<img width="1371" alt="Screenshot 2022-09-12 at 22 44 42" src="https://user-images.githubusercontent.com/93072051/194393705-e37cf413-02a4-4687-a37e-78a52e1350f1.png">




