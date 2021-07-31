#4. Stopwatch

import time

def countdown(timer):

    while timer:

        mins, secs = divmod(timer, 60)

        timeformat = '{:02d}:{:02d}'.format(mins, secs)

        print(timeformat)

        time.sleep(1)

        timer -= 1
    print("stop1")

countdown(10)