from datetime import datetime

import pytz

now = datetime.now()

livetime = pytz.timezone('America/New_York')
t = datetime.now(livetime)

print("New York: ", t.strftime("%I:%M:%S %p"))