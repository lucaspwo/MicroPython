# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import machine
import conectar
import time
import os
import webrepl
webrepl.start()
gc.collect()

# if conectar.conectar():#
#     onboardled = machine.PWM(machine.Pin(2), freq=500, duty=1000)#
#     time.sleep(1)#
#     for i in range(1001, 1024):#
#         onboardled.duty(i)#
#         time.sleep_ms(50)#
# else:#
#     onboardled = machine.PWM(machine.Pin(2), freq=500, duty=0)#
#     time.sleep(1)#
#     onboardled.duty(1023)#
#     time.sleep(1)#
#     onboardled.duty(0)#
#     time.sleep(1)#
#     onboardled.duty(1023)#
#     time.sleep(1)#
#     onboardled.duty(0)# 
#     time.sleep(1)#
#     onboardled.duty(1023)