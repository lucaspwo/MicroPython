<<<<<<< HEAD
import machine, neopixel, time
np = neopixel.NeoPixel(machine.Pin(4), 10)
n = np.n

while True:
    for i in range(40, 255):
        for l in range(n):
            #np[l] = (i,0,k-i)
            np[l] = (i,0,0)
        np.write()
        #print(i)
        time.sleep_ms(15)
    for i in range(255, 40, -1):
        for l in range(n):
            #np[l] = (i,0,k-i)
            np[l] = (i,0,0)
        np.write()
        #print(i)
        time.sleep_ms(15)
=======
import machine, neopixel, timenp = neopixel.NeoPixel(machine.Pin(4), 10)n = np.n
while True:    for i in range(40, 255):        for l in range(n):            #np[l] = (i,0,k-i)            np[l] = (i,0,0)        np.write()        #print(i)        time.sleep_ms(15)    for i in range(255, 40, -1):        for l in range(n):            #np[l] = (i,0,k-i)            np[l] = (i,0,0)        np.write()        #print(i)        time.sleep_ms(15)
>>>>>>> origin/master
