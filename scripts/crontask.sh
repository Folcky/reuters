#write out current crontab
#crontab -l > mycron
#Hourly
echo "00 * * * * python get_data.py;python save_data.py" >> mycron
#install new cron file
crontab mycron
rm mycron



#* * * * * "command to be executed"
#- - - - -
#| | | | |
#| | | | ----- Day of week (0 - 7) (Sunday=0 or 7)
#| | | ------- Month (1 - 12)
#| | --------- Day of month (1 - 31)
#| ----------- Hour (0 - 23)
#------------- Minute (0 - 59)
