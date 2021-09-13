#StopWatch In Python

import time
print("Press Enter to Begin")
print("Press Ctrl+C to End")

while True:
    try:
        input()
        starttime=time.time()
        print("Started")

    except KeyboardInterrupt:
        print("Stopped")
        endtime=time.time()
        print("Total Time: ", round(endtime - starttime,2),"Secs")
        break
