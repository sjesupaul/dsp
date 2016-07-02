# Hint:  use Google to find python function

from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
print('Number of days between', date_start, '&', date_stop, ':',
      (datetime.strptime(date_stop, "%m-%d-%Y") -
       datetime.strptime(date_start, "%m-%d-%Y")).days)
       
####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_start = datetime(int(date_start[4:8]), int(date_start[0:2]), int(date_start[2:4]))
date_stop = datetime(int(date_stop[4:8]), int(date_stop[0:2]), int(date_stop[2:4]))

print('Number of days between', date_start.date(), '&', date_stop.date(), ':',
      (date_stop - date_start).days)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
start = (date_start.split("-"))
stop = (date_stop.split("-"))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for i, m in enumerate(months):
    if start[1] == m:
        start[1] = i+1
    if stop[1] == m:
        stop[1] = i+1

date_start = datetime(int(start[2]), int(start[1]), int(start[0]))
date_stop = datetime(int(stop[2]), int(stop[1]), int(stop[0]))

print('Number of days between', date_start.date(), '&', date_stop.date(), ':',
      (date_stop-date_start).days)

