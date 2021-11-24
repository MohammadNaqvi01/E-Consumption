import requests
import time
init=0
URL=f"http://127.0.0.1:8000/energy?timein={init}"
print("In development Mode Default appliance is TV with avg. 150w \n")
requests.get(url=URL)
time1=time.time()
input("Press Enter When you want to calculate Your Energy Consumption\n")

time2=time.time()
time2=int(time2)
s=requests.get(url=f"http://127.0.0.1:8000/energy?cooky={time2}")
r=s.json()

timing=time2-time1
timing=int(timing)
print(r)
print(f"{timing} secs")
timing=timing/3600
Energy=(150*(timing/1000))
print(f"Your Appliance has consumed {Energy}kwh of energy")