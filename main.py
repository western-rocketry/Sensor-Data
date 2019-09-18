from random import randrange
import pandas as pd
data = []
#| Time | Temperature (celsius) | Pressure (kpa) | Acceleration (m/s^2) | 
data.append([0,30,101.25,0])
flight_time = 30
for time in range(flight_time):
    for mili in range(100):
        previous =  data[len(data)-1] 
        temp = previous[1] - 0.002 * randrange(10)
        press = previous[2] - 0.0065 * randrange(10)
        accl = previous[3]
        if time < flight_time / 4:
            accl = accl + (mili * randrange(10) * 0.00025)
        elif time > flight_time / 4 and time < flight_time /2:
            accl = accl - (mili * randrange(10) * 0.00025)
        else:
            accl = accl - (mili * randrange(10) * 0.000015)


        data.append([time,temp,press,accl])
df = pd.DataFrame(data)
df.columns = ["Time", "Temperature", "Pressure", "Acceleration"]
df.to_csv('data.csv', encoding='utf-8')