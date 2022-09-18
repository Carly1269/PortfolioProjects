README

# Introduction
The Cyclistic Case Study project is based on one of the Case Studies provided for students of the Google Data Analytics Professional Certificate. 
You can learn more about this Case Study [here](Cycyclistic_Case_Study/Cyclistic_Case_Study.pdf).

For the purposes of this project, we will use a modification of the original Case Study. We will be using PostgreSQL for importing and manipulating the Data. 
We will then transfer the data to Rstudio for analysis.

# ASK
The questions that will guide our analysis are:
1. How do annual members and casual riders use Cyclistic bikes differently?
2. Why would casual riders buy Cyclistic annual memberships?
3. How can Cyclistic use digital media to influence casual riders to become members?

# PREPARE
We will first need to download the data. The data is sourced from [here](https://divvy-tripdata.s3.amazonaws.com/index.html)

Note:  This data source contains the data from June 2020 to present. The data used for this analysis was from June 2021 to May 2022

# PROCESS
To process our data, we will be using SQL for cleaning and analysis as well as RStudio for Visualization
The first step is to create our table in SQL:
--First we need to create the tripdata table in SQL. We do this by executing the following query

## SQL
```sql
CREATE TABLE tripdata (ride_id VARCHAR(16) PRIMARY KEY,
                      rideable_type VARCHAR(255),
                      started_at TIMESTAMP,
                      ended_at TIMESTAMP,
                      start_station_name VARCHAR(255),
                      start_station_id VARCHAR(255),
                      end_station_name VARCHAR(255),
                      end_station_id VARCHAR(255),
                      start_lat FLOAT,
                      start_lng FLOAT,
                      end_lat FLOAT,
                      end_lng FLOAT,
                      member_casual VARCHAR(255))
```                     

The second step is importing the data into our newly created table. We do this using this isntructions
[this instructions](https://www.postgresqltutorial.com/postgresql-tutorial/import-csv-file-into-posgresql-table/)

We now have our data ready for cleanup and analysis

# ANALYZE
With our data imported into SQL we are ready for analysis. Our Analysis will be based on the guide questions in the ASK section of this document:

## SQL
```sql
/*We Want to know which day of the week has the most ammount of activity with usage. For that we will
need to calculate the length of each ride. We also want to know which day of the week has the most usage
Finally we want to categorize this data by member/casual*/  

SELECT (ended_at - started_at) AS ride_length,
CASE WHEN EXTRACT(dow FROM started_at) =0 THEN 'Monday'
WHEN EXTRACT(dow FROM ended_at) =1 THEN 'Tuesday'
WHEN EXTRACT(dow FROM ended_at) =2 THEN 'Wednesday'
WHEN EXTRACT(dow FROM ended_at) =3 THEN 'Thursday'
WHEN EXTRACT(dow FROM ended_at) =4 THEN 'Friday'
WHEN EXTRACT(dow FROM ended_at) =5 THEN 'Saturday'
ELSE 'Sunday' END AS day_of_the_week,
member_casual
FROM tripdata;

/*We now want to calculate sumary of statistics for the data such as max,minimum,mean values 
per user type: member/casual. For this we create a temporary table with the previous query 
results and take the values from it*/  

WITH ride_information AS (SELECT (ended_at - started_at) AS ride_length,
CASE WHEN EXTRACT(dow FROM started_at) =0 THEN 'Monday'
WHEN EXTRACT(dow FROM ended_at) =1 THEN 'Tuesday'
WHEN EXTRACT(dow FROM ended_at) =2 THEN 'Wednesday'
WHEN EXTRACT(dow FROM ended_at) =3 THEN 'Thursday'
WHEN EXTRACT(dow FROM ended_at) =4 THEN 'Friday'
WHEN EXTRACT(dow FROM ended_at) =5 THEN 'Saturday'
ELSE 'Sunday' END AS day_of_the_week,
member_casual
FROM tripdata)


SELECT MIN(ride_length),
MAX(ride_length), 
AVG(ride_length), 
member_casual 
FROM ride_information 
group by member_casual;

/*This query calculates the days with the most number of rides regardless of the user type*/  

SELECT COUNT(day_of_the_week),
day_of_the_week
FROM ride_information 
group by day_of_the_week
order by COUNT(day_of_the_week)

/*This query calculates the days with the most number of rides divided by user type: member/casual*/  

SELECT COUNT(day_of_the_week),
day_of_the_week,
member_casual 
FROM ride_information 
group by day_of_the_week, member_casual
order by COUNT(day_of_the_week)
```

We have completed our analysis on SQL we will export the data we calculated in SQL for further analysis on Rstudio:

## SQL
```sql
/*We Want to export the data output from the queries into a CSV 
file for analyzing and creating reports. We do this using the COPY command.*/  

COPY(SELECT (ended_at - started_at) AS ride_length,
CASE WHEN EXTRACT(dow FROM started_at) =0 THEN 'Monday'
WHEN EXTRACT(dow FROM ended_at) =1 THEN 'Tuesday'
WHEN EXTRACT(dow FROM ended_at) =2 THEN 'Wednesday'
WHEN EXTRACT(dow FROM ended_at) =3 THEN 'Thursday'
WHEN EXTRACT(dow FROM ended_at) =4 THEN 'Friday'
WHEN EXTRACT(dow FROM ended_at) =5 THEN 'Saturday'
ELSE 'Sunday' END AS day_of_the_week,
member_casual
FROM tripdata) TO 'C:\Users\Public\ride_information.csv' CSV HEADER;

--

COPY (WITH ride_information AS (SELECT (ended_at - started_at) AS ride_length,
CASE WHEN EXTRACT(dow FROM started_at) =0 THEN 'Monday'
WHEN EXTRACT(dow FROM ended_at) =1 THEN 'Tuesday'
WHEN EXTRACT(dow FROM ended_at) =2 THEN 'Wednesday'
WHEN EXTRACT(dow FROM ended_at) =3 THEN 'Thursday'
WHEN EXTRACT(dow FROM ended_at) =4 THEN 'Friday'
WHEN EXTRACT(dow FROM ended_at) =5 THEN 'Saturday'
ELSE 'Sunday' END AS day_of_the_week,
member_casual
FROM tripdata)


SELECT MIN(ride_length),
MAX(ride_length), 
AVG(ride_length), 
member_casual 
FROM ride_information 
group by member_casual) 
TO 'C:\Users\Public\ride_information_statistics.csv' CSV HEADER;


--

COPY (WITH ride_information AS (SELECT (ended_at - started_at) AS ride_length,
CASE WHEN EXTRACT(dow FROM started_at) =0 THEN 'Monday'
WHEN EXTRACT(dow FROM ended_at) =1 THEN 'Tuesday'
WHEN EXTRACT(dow FROM ended_at) =2 THEN 'Wednesday'
WHEN EXTRACT(dow FROM ended_at) =3 THEN 'Thursday'
WHEN EXTRACT(dow FROM ended_at) =4 THEN 'Friday'
WHEN EXTRACT(dow FROM ended_at) =5 THEN 'Saturday'
ELSE 'Sunday' END AS day_of_the_week,
member_casual
FROM tripdata)
      
SELECT COUNT(day_of_the_week),
day_of_the_week
FROM ride_information 
group by day_of_the_week
order by COUNT(day_of_the_week))
TO 'C:\Users\Public\ride_information_per_day.csv' CSV HEADER

--

COPY (WITH ride_information AS (SELECT (ended_at - started_at) AS ride_length,
CASE WHEN EXTRACT(dow FROM started_at) =0 THEN 'Monday'
WHEN EXTRACT(dow FROM ended_at) =1 THEN 'Tuesday'
WHEN EXTRACT(dow FROM ended_at) =2 THEN 'Wednesday'
WHEN EXTRACT(dow FROM ended_at) =3 THEN 'Thursday'
WHEN EXTRACT(dow FROM ended_at) =4 THEN 'Friday'
WHEN EXTRACT(dow FROM ended_at) =5 THEN 'Saturday'
ELSE 'Sunday' END AS day_of_the_week,
member_casual
FROM tripdata)
      
SELECT COUNT(day_of_the_week),
day_of_the_week,
member_casual 
FROM ride_information 
group by day_of_the_week, member_casual
order by COUNT(day_of_the_week))
TO 'C:\Users\Public\ride_information_per_user_per_day.csv' CSV HEADER

```
## RStudio
The Analysis on Rstudio can be seen on the [UFO_RMD](Cycyclistic_Case_Study/RStudio/Cyclist_RMD.pdf) file

# SHARE
Coming soon
# ACT
Coming soon


