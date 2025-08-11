from datetime import date
from datetime import datetime
import time

current_time = time.localtime()
print(time.strftime("%I:%M:%S", current_time))


print("Current time is:", time.strftime("%I:%M:%S", current_time))

