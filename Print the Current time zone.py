import pytz #Python time zone
from datetime import datetime
a=pytz.timezone('Europe/paris')
b=datetime.now(a)
print(b)


