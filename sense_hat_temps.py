import os
from sense_hat import SenseHat
sense = SenseHat()
def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=","").replace("'C\n",""))
    return(t)

T1 = sense.get_temperature_from_humidity()
T2 = sense.get_temperature_from_pressure()
T1inF = T1 * (9/5) + 32
T2inF = T2 * (9/5) + 32
t_cpu = get_cpu_temp()
t1_corr = T1 - ((t_cpu-T1)/1.5)
t1_corrF = t1_corr * (9/5) + 32
t2_corr = T2 - ((t_cpu-T2)/1.5)
t2_corrF = t2_corr * (9/5) + 32

print("The T1 temp is " + str(T1) + " in Celsius.")
print("The CPU temp is " + str(t_cpu) + " in Celsius.")
print("The corrected T1 temp is " + str(t1_corrF) + " in Fahrenheit.")
print("The T2 temp is " + str(T2) + " in Celsius.")
print("The corrected T2 temp is " + str(t2_corrF) + " in Fahrenheit.")



