# CTC_API ReadMe

# What is the CTC Report API

The CTC_Report_API is a new development in the HIVE Product line

#### The API allows connection to, and extraction of:

- (Current) CMS Data
- (Future) Users and Group Data
- (future) Project Activity Data
- (Future) License Usage Data

This access replaces the need to download the Excel files on some interval
Instead, it is now possible to directly connect to the data and either efficient, or ineficently access the resulting data

#### Common access includes:

- (Lest efficient) Direct Connection through PowerBI or Tableau
- (More efficient) Data Extraction into JSON files
  - Reviewing those files in the BI tool of choice
- (Most efficient) Extract/Transform/Load the API data and load into a database of choice
  - Update data (Without the need to fetch everything)
  - Review data in BI tool of choice connecting to 'internal' database

# Who wants to use the API

Companies who have a dedicated or experienced Data Analyst/Scientist may benefit most from the new CTC Report API
Though companies without a dedicated or experienced team, may still greatly benefit from direct access to their CTC Data

# How do you get started

A base understanding of a BI tool is recommended as reviewing the raw data can be quite tedious
BI tools often rely heavily on JSON data structure format, so an understanding in basic JSON is recommended
This sample project relies heavily on Python, but any language is capable of obtaining the data from the CTC Reporting API
Additionally, for the most efficient implementation it is recommended that SQL Server, hosted locally or on Azure be leveraged
It is possible to leverage this with SQL Server Express, mySQL, PostrgreSQL, and may other database hosts
  It is likely that significant code updates will be required in your fork for other databases

# Using this python code

While certainly not a complete guide, this section will assist in the implementation of the sample code
I certainly do not want you to have to dig for every reference and workflow
I also want to be very clear about the following:

- CTC does support their API
- CTC does NOT support code in this git repository
  - this sample code is provided without support
  - this code is to be used at your own risk
  - this code may be updated over time and may not function exactly as demonstrated in recorded webinars
  - this code is likely not free of bugs
  - please let the owner of this repo know if their code includes bugs, but do not reach out to CTC support as they will have no clue how to assist

## Includes leveraged

The list below will only include imports that need to be installed as they may not included in the default install of python

- json
- pyodbc

## Updating the settings file

The settings file is located at Files\SupportFiles\Settings.json
The file controls many of the primary options throughout the app
Be sure to obtain your company reportsKey from CTC software directly and update the settings file with your key

- info@ctcsoftware.com

Also, it is recommended that if you are leveraging the JsonCacheFiles portion that you update:

- files:storageCachePath

## Json File Pull

The Json files can be quite large and take up quite a lot of disk space if the file properties are included in the data pull
It is recommended that you begin with a small dataset to see how large your early file-set may be
Most pulls of files will take an hour or more for an established company using HIVE CMS for a year+

## SQL Server Connection

The connection to SQL server is the most efficient data storage option long term as the refreshing can be done for the delta data
It is also convenient as it can be run in the background and your BI tool does not have to take the load of the data pull
BI data and relationships can be read directly from the SQL server, saving time in managing the BI data structure
Python also can get all of the deep data by ID, and then selectively store it in the database, minimizing the number of times data is fetched from the reporting API
