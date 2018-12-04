# Secure-Strolls
Database Systems Final Project

## DESCRIPTION

Our web application, Secure Strolls, finds the safest route for the user between a given start and end location using our safety score algorithm. We find the possible paths between the two points using the Google Maps API and for each path, we assign all the streets a score based on the crimes that happened in those locations. The score is based on different factors like the type of crime. The safest path, that is the one with the best score, is then displayed to the user.

## USEFULNESS

A lot of students at UIUC spend late nights studying at the library or at other university buildings and walk home alone. With a high crime rate prevalent in Urbana-Champaign, we wanted to help make students feel safer and by providing safer routes, help decrease the chance of crimes. Safewalk apps that are currently available on the market only either let your friends know about your location in real-time or call the university police. Our app provides users with the option of finding a safer route based on real crime data we collect from the Champaign-Urbana area.

## THE DATABASE 

We have 6 tables in our database: CRIME, INCIDENT, LOCATION, USER, SAVED_ROUTES, and USERS_PROFILE. 
- The CRIME table describes the kinds of crimes in our database and has a base score out of 5 for each kind of crime. For instance, ‘trespass’ has a low score of 1, whereas ‘murder’ has a higher score of 5. 
- INCIDENT has all the instances of crimes that have occured in Urbana-Champaign. Each incident has the fields incident_id, which is the primary key, a date, time, description, crime_type, which is a foreign key and is the primary key of the CRIME table, and address. 
- The LOCATION table has the fields location_id, which is the primary key, the address, and the latitude and longitude of the location which we get from the Google Maps API using the address. We need the latitude and longitude of the locations so we can easily pass the data to the Google Maps API. 
- The USER table stores the information of all the users who have signed up. The fields are User_ID (primary key), first_name, last_name, email, password, userName, last_login and is_superuser (admin is super user). 
- The USERS_PROFILE table stores the image of the user along with the user_id which is the primary key of the USER table and the secondary key of this table. The SAVED_ROUTES table stores the start and end locations saved by the user and has the foreign key of user_id to associate the route with the user who saved it.

## ER Diagram
**Schema:**

Crime(CrimeType, Score)

Incident(Incident_ID, Description, Time, Date, Address, CrimeType)

Location(Location_ID, Latitude, Longitude, Address)

User(User_ID, first_name, last_name, email, password, is_superuser, user_name, last_login)

Saved_Routes(Route_ID, User_ID, Saved, start_location, end_location, date_searched)

Users_profile(Profile_ID, User_ID, Image)

<em>We collected the crime data from crimemapping.com and have real user data in the database from 10 developed accounts.
  
## FUNCTIONALITY
Our basic functionality will show the safest route on the map based on users' input of start location and destination by assigning each possible route a score using our safety algorithm. Our advanced functionality allows 1) the user to create an account and log in to save and view their favorite or most used locations and 2) instead of looking at a particular point of location to calculate the score, we look at a section of the street around a radius and calculate the score accordingly.

<br>
One basic function we have is inserting a route that a logged in user searched for and marked as “save”. This allows us to display a logged in user’s saved routes so they have a reference for their start and end location parameters when they want to search that route again.
