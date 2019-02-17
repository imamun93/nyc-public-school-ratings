NYC Public School Rating and Student Performance
============================================================

We wanted to check if there was a relationship between New York City Public High School rating, given by the Department of Education and the school's student attendance and SAT score performance. All our data came from the New York City Open Data source.

Source
-----------
Please click on the following to visit the raw data:
[Rating](https://data.cityofnewyork.us/Education/2005-2017-School-Quality-Review-Ratings/9n9z-hh9p), 
[School Attendance](https://data.cityofnewyork.us/Education/2012-2017-Historical-Monthly-Grade-Level-Attendanc/wed3-5i35), 
[SAT Scores](https://data.cityofnewyork.us/Education/2012-SAT-Results/f9bf-2cp4)

Problems 
------------
We noticed that our files had multiple erroneous data, either missing information or input was incorrect. We had to standardized everything. This took us the longest amounts of time as we had to create multiple different sets of nested dictionaries and from that create a massive list that will contain all our necessary information.
After cleaning and aggregating all data into one mega list (mega_data), we started to seed and graph.

What did the Data say
--------------
**Rating color breakdown:**
>Red= School rated as 1, lowest rating possible (graph interchange between 0 and 1)

>Blue= School rated as 2, second lowest rating possible

>Purple= School rated as 3, middle ground of ratings

>Green= School rated as 4, considered high rating

>Orange= School rated as 5, highest possible rating 

*Notice we have a red with an absent ratio above 1 which is not possible. This is most likely due to clerical error from the original data source, where the wrong information of absents and presents for that school was input into the original database*


<img src="https://user-images.githubusercontent.com/41834786/48682919-94367580-eb78-11e8-92b6-9707c7ed05dc.png" width="90%">

This graph is showing the average math SAT scores of New York City public high schools. 

<img src="https://user-images.githubusercontent.com/41834786/48683363-bd580580-eb7a-11e8-9667-271fe2a0d9c1.png" width="90%"></img> 

This graph is showing the average reading SAT scores of New York City public high schools. 

We noticed that there is indeed a relationship between a school's official rating and it's student performance. Although most of the schools were indeed clustered around the 350-400 SAT school range, schools that were rated 4 or higher (out of 5) had a lower absent to present ratio and are generally found in the higher SAT score than school with lower ratings. Schools with rating of 2 and 3 were similar and more clustered together to the mid-range SAT scores while also having a higher absent to present ratio compared to 4 and 5. Ratings 1 had by far the highest absent to present ratio while also having low to mid range SAT scores.

Result
---------------
Our data shows that there is a positive correlation between a school's official rating from the Department of Education and how well the students of said school performs.

Future Work
---------------------
We were only able to get information for one year of school, school year 2012-2013. We requested a freedom of information from NYC DOE and if that goes through we will have more data to work with. Then we can compare a school's change in rating over the course of several years and student performance for better validation of our results.

We also would like to perform a T-test with ANOVA and compare it to Critical Value to see if there is a significant relationship between school ratings and student performance.
