# nasa-eonet-webscrapping

The pymongo package allows access to my local instance of a new database the database db.events. The client section calls the local port of the database instance.

The requests package in Python is used to pull from the https://eonet.sci.gsfc.nasa.gov/api/v2.1/categories in order to ensure that the right data is pulled the api documentation on categories was inspected to find the distinct ids for Severe storms, Wildfires and Landslides. These were found to be 8, 10 and 16.

The id's are then stored in a list which will be looped through to form the webpage https://eonet.sci.gsfc.nasa.gov/api/v2.1/categories/{id}. This should then allow for each of the respective events to be obtained. Within the body of the loop after the url variable there is a payload variable which will restrict the api to pull results from the prior 31 days.

The requests json command is then used as the output from the api is in json format. This is then inserted into my events database by the insert_one command.

The database is then queried using the find_one limiting to the fields event.id, geometries.date and geometries.coordinates.

The csv package is then used to write the data to an excel format. This is achieved by looping through any of the dictionaires within the query to produce an output with sequential columns. This relies upon putting parts of the query into a list which will allow it to then be written into the respective columns within the csv.

The last part of the script deals with sending an email using the user details. This has been left to fill in for the relevant emails/

# Considerations and Improvements

1) The database was considered to be put into the cloud which would allow it be scaled more easily for a larger project
2) The email script could be generalised to allow for any email or client to be reached
3) In this case I allowed MongoDB to create an id field but potentially it may have been better to use the id within events as the database id
4) The email could be encapsulated within a function and as with the get_events() function be run afterwards.
