#Problema 1

from datetime import datetime
s = datetime.strptime("23:45:20", "%H:%M:%S") #strptime() method creates a datetime object from the given string
print(s.strftime("%r"))
















