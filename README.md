# Flight_deals
What it does:
This project will help you find plane tickets according to criteria such as: departure and arrival cities, departure date, maximum number of transfers. The data will be saved to an Excel file and shown to the user.


The program is made using Pyhton. 

The user inputs flight data in the GUI (it is made using tkinter library), then it gets sent to the FlightData class (flight_data.py) which gets IATA codes of cities through "tequilla api" (request library is used). 
IATA codes then get sent to FLightSearch class (flight_search.py). This class searches for flights by using "kiwi api" and returns the information in str format. A "json" library is used in order to convert returned str into json. 
All data then gets sent to DataManager class which selects needed data and writes it to the excel file. "openpyxl" library is used in order to manipulate excel file. 
At the end "os" library is used in order to open the excel file with flights data.
