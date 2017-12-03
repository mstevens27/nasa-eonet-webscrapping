# nasa-eonet-webscrapping

The pymomngo package allows access to my cloud instance of a new database the database client.events. The client section calls the local port of the database instance.

The requests package in Python is used to pull from the https://eonet.sci.gsfc.nasa.gov/api/v2.1/categories in order to ensure that the right data is pulled the api documentation on categories was inspected to find the distinct ids for Severe storms, Wildfires and Landslides. These were found to be 8, 10 and 16.

The id's are then stored in a list which will be looped through to form the webpage https://eonet.sci.gsfc.nasa.gov/api/v2.1/categories/{id}. This should then allow for each of the respective events to be obtained. Within the body of the loop after the url variable there is a payload variable which will restrict the api to pull results from the prior 31 days.

The Beautiful Soup package is then used to parse the xml to then pymongos inset command is used to insert into the collection. A further command is then used to export into a csv.
