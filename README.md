WELCOME to the amazing project! HOW IS VIOLENCE RELATED TO SUBSTANCE ABUSE?

------------------------------------------------------------------------------------------------------------------------------

Our group consists of Mauricio López Méndez, Syed Taha Mashood and Marie-Noelle Steinig.

------------------------------------------------------------------------------------------------------------------------------

LAUNCHING INSTRUCTIONS:
Hi Jamie! We hope that these instructions are understandable and not like an IKEA manual on how to put the pieces of furniture together.

1. Open your MacBook (well, done that obviously...).
2. Open your Terminal with Bash.
3. Go into our github directory and clone the Project directory into a place on your MacBook that you want to launch it from.
4. In Bash: cd into the following directory Project/Project Dynamic Websites (the "Project Dynamic Websites" opens after clicking on the "Project" folder).
5. In Bash use the following command: python manage.py runserver.
6. In Safari/Internet Explorer/Chrome: type in this URL "localhost:8000/myapp/home/".
7. Enjoy our website and click through the different tabs and dropdowns.
8. From your Finder: explore the directory. Below we have indicated what you can find in the directory.
9. Thank you for introducing us to Programming and understanding the world a bit better!

------------------------------------------------------------------------------------------------------------------------------

THE IDEA:
Living in Chicago, we always were concerned about crime. In numerous courses we were confronted with the statistical finding that crime rates highly correlate with the temperature. This correlation seems weird at first sight, but makes quite a lot of sense, if you consider moderator and or mediator variables.
One such variable could potentially be the use of substances that might increase during summers for numerous reasons.
Our group therefore wants to find out, whether homicide rates correlate with substance abuse, in particular the consumption of Marijuana. We planned to do it for Chicago and San Francisco. We have selected San Fran as a kind of control, since the variation in weather in almost non-existent in San Fran, so that we should get an unbiased estimator. Due to time constraints, we were only able to finalize the project for San Fran, but we will try to finalize Chicago after the deadline, as this is a pretty awesome project!

------------------------------------------------------------------------------------------------------------------------------

DATA ANALYSIS GENERAL GOAL:
For figuring this out, we rely on the good old laws of supply and demand.
The price should therefore be a good indicator of the consumption of a substance abuse.
We therefore would like to regress the daily price of medium quality Marijuana per ounce on the daily homicide rate.
In order to control for weather, we selected two cities for our analysis. First Chicago, in which you have four clearly meteorologically differentiated seasons and then San Francisco in which we have basically no seasons and a more or less steady temperature. Note: the daily price of Marijuana is given for the entire State of California.

------------------------------------------------------------------------------------------------------------------------------

DESCRIPTION OF ANALYSIS:
Analysis1: We focus on this analysis on the relationship between weed prices in the State of California and observed number of crimes in San Francisco. We will explore variation of this variable within the year 2014:

1.1 How does this variables behave from month to month within the city.
We then looked at two variables of crime in relation to weed prices: i) number of homicides per month, and ii) number of drug related detentions per month. Only i) was included and relevant for the website. The other graphs can be found as pictures under /Project/Project Dynamic Websites/Graphs. Note that the ones we used for the website are also in the static folder.
1.2 Is there a statistical association in the variation of number of crime incidents and weed prices within each city and  on the aggregate?

------------------------------------------------------------------------------------------------------------------------------

METHODS:
               Analysis 1.1 : a) plot # number of crime incidents versus months within city and overall
                              b) plot weed prices versus months within State
               Analysis 1.2 : a) OLS regression weed prices (month average) on number of crime incidents (count on months) for each city + regplot for each city
                              b) OLS regression "..." for aggregated data on crime + regplot for aggregated dat on crime

------------------------------------------------------------------------------------------------------------------------------

DATA SOURCES:
a)Weed Prices Dataset: For the daily price of Marijuana, we found a raw database on github (https://github.com/frankbi/price-of-weed/tree/master/data), which represents  cumulative results of a website called http://www.priceofweed.com/. We contacted the person who created the database with some clarification questions concerning the units. He then explained to us that there are three different qualities of weed in every table and that the price depicted for every qualitative classification is the price per ounce.
As the 2016 is not over yet and the data for 2015 is not complete, we concentrated on the data of the year 2014.

b) SF Crime Dataset: We use data from https://data.sfgov.org/Public-Safety/Map-Crime-Incidents-from-1-Jan-2003/gxxq-x39z. We downloaded crime data for each day in 2014. We are using the following variables: date, incident number (unique crime identifier) and descript)

In the directory we have included a folder called FULL PROCESSED DATA (/Project/Project Dynamic Websites/FULL PROCESSED DATA).
In this folder you can find a folder for Chicago (empty) and a folder for San Francisco. You will then find two cleaned tables, one for the weed prices in California and the other one for San Francisco crimes. Additionally there is another folder including the merged dataset for homicides in San Francisco and weed prices in California per day.

------------------------------------------------------------------------------------------------------------------------------

DATA CLEANING:
The cleaning scripts can be found in the repository under Project/Project Dynamic Websites/DATA CLEANING FILES. Thereby there are two folders, one for Chicago (empty) and one for San Francisco. In these folders you will see two files, one for the weed prices and one for the homicide rate. The names are (San Francisco/California):

Weed prices (California): cleaningweedprices.py
Crime data SF: FP_merge&clean_dfs&plots_v1.py (this also contains the graphs and regression commands)

------------------------------------------------------------------------------------------------------------------------------

WEBSITE DESIGN:
We have developed four different websites which are all linked through a header. The first website is the home site. From there the reader as three different possibilities on where to go: dataset, regression, graphs.
The dynamic part of our application are mainly the individual websites can be accessed through different urls. In a different step one could imagine some drop down menus displaying different months and the corresponding values of each day during the month

Repository Structure:

FP_Intro_Programming			
		Website				
			myapp/
      static/			
      mysite/		
			db.sqlite3						
			manage.py			

		Data
      Weed
        CAL
            Raw.csv
						Clean.py
						Final.csv
						Graphs/

				IL
            Raw.csv
						Clean.py
						Final.csv
						Graphs/
			Crime			
				SF
            Raw.csv
						Clean.py
						Final.csv
					  Graphs/

				CHI
            Raw.csv
						Clean.py
						Final.csv
						Graphs/

			Weed on Crime		

				SF
          	Final.csv
						DFs_plots.py
						Graphs/
						OLS/

			CHI
            Final.csv
						DFs_plots.py
						Graphs/
						OLS/
# FProject_INTROP
