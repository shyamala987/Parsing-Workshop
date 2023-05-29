#!/bin/bash

LOGFILE='/Users/svenkata/Projects/Parsing-Workshop/exercises/analyzing_apache-logs/apache_logs.txt'
echo "Percentage of individual status codes\n-----------------------------\n"
awk '{x[$9]+=1; y++}; END{print "Percentage of each response code : "; for(i in x){print i, " : ", x[i]*100/y}}' $LOGFILE 

echo "List of browsers\n-----------------------------\n"
awk 'BEGIN{FS="\""};{print $6}' $LOGFILE

echo "Average requests per day\n---------------------\n"
awk '{print $4}' analyzing_apache-logs/apache_logs.txt | awk 'BEGIN{FS="["};{print $2}' | awk 'BEGIN{FS=":"};{print $1}' | awk '{x[$0]+=1;y++}; END{print "Avg requests on day : "; for(i in x) {print i," : ", x[i], y}}'


