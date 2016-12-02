import machine, neopixel, time
np = neopixel.NeoPixel(machine.Pin(4), 10)
n = np.n

while True:
    for i in range(128):
        for l in range(n):
            #np[l] = (i,0,k-i)
            np[l] = (128-i,i,0)
        np.write()
        #print(i)
        time.sleep_ms(30)
    for j in range(128):
        for l in range(n):
            #np[l] = (i-j,j,0)
            np[l] = (0,128-j,j)
        np.write()
        #print(j)
        time.sleep_ms(30)
    for k in range(128):
        for l in range(n):
            #np[l] = (0,k-j,k)
            np[l] = (k,0,128-k)
        np.write()
        #print(k)
        time.sleep_ms(30)