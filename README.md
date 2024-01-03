#Setup
* Fork repo
* clone the repo
* make sure you have mysql server installed (workbench or xampp)
* open project in your preferred IDE
* navigate to Database/database.py
* change the test123$ in the line of code ```create_engine('mysql://root:test123$@localhost/transport', echo=False)``` to your password of you own server
* save the changes
* GO to your mysql server and create a database schema called *transport* use the comand ```create schema transport```
* Come back to our IDE and run the widget.py file
