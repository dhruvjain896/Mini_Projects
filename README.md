# Mini_Projects

## FIR Application System

Frontend: Tkinter
Backend: Sqlite3

FIR Application System is a python based project. I have developed this application using Tkinter and Sqlite3. The main modules available in this project are pythonfile.py which is the landing page, front.py is used as an interface for lodging FIR, view FIR, update FIR, withdraw FIR, back.py is used as backend for managing the database, password_generator.py is used for generating the login password for the user.

MODULES
Pythonfile.py – Asks for a valid phone number to access the FIR lodging system. 

front.py – Let the user to lodge an FIR after all the details are entered successfully the user can lodge the FIR and the randomly generated user ID and password is provided to the user so that he/she can view, update or withdraw his FIR. The user can view his FIR through a message box using the credentials given after he lodged the FIR. The user can withdraw his FIR and it will be deleted from the database and the credentials will become invalid. The user can update his previously lodged FIR using update FIR button and it will be updated in database.
 
back.py – All the operations going on in the frontend will be managed by the backend file in the fir database. 

password_generator.py – This module creates a random password for the user.

Please Note that no two users can have same user ID and Password.
