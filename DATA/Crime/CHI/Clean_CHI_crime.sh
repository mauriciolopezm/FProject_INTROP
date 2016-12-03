cat Raw_CHI_Crime_2014.csv| cut -f1 -f2 -f5 -d, | sed 's/ /,/g' | cut -f1 -f2 -f5 -d, > CHI_Crime_2014.csv
head CHI_Crime_2014.csv
 #note that column titles are not right and need to be renamed on the df
 
