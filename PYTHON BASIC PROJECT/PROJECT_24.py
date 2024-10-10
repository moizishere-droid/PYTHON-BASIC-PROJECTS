# basic aralam clock

import datetime as dt
import time as t

set_aralam1 = (input("Enter the time in HR (00 to 23): "))
set_aralam2 = (input("Enter the time in MI (00 to 59): "))
concat = f"{set_aralam1}:{set_aralam2}"



while(True):
    current_time = dt.datetime.now().strftime("%H:%M")
    print(current_time)
    if(current_time==concat):
        print("wake up")
        break
    t.sleep(60)