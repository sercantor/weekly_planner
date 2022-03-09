from datetime import datetime
from datetime import timedelta
import time
import os
from enum import Enum

d = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
d_values = list(d.values())

print("""1: 'Monday'\n2: 'Tuesday'\n3: 'Wednesday'\n4: 'Thursday'\n5: 'Friday'\n6: 'Saturday'\n7: 'Sunday'""")
days = int(input('How many weeks?\n'))
start_day = int(input('What is your start day? Monday is 1, Sunday is 7\n'))
end_day = int(input('What is your end day? Monday is 1, Sunday is 7\n'))
todo_number = int(input('How many tasks on average do you need for a day?\n'))

start_day_value = d[start_day]
end_day_value = d[end_day]
timestr = time.strftime("%d-%b-%Y")
todos = todo_number *  "- [ ]\n"

content = """"""
file = open("{}.md".format(timestr), "w+")

for i in range(days*7 -2):
	timediff = (datetime.now() + timedelta(days=i) ).strftime('%B %d - %A')
	if end_day_value not in timediff:
		if d[end_day + 1] in timediff or d[end_day + 2] in timediff:
			continue
		content += """## {}
{}
""".format(timediff, todos)
	else:	
		if d[end_day + 1] in timediff or d[end_day + 2] in timediff:
			continue
		content += """
## {}
{}
---
""".format(timediff, todos)
	

file.write(content)

file.close() 

