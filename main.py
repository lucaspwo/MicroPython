import machine, neopixel, time
np = neopixel.NeoPixel(machine.Pin(4), 10)
n = np.n

while True:
    try:
        for i in range(45, 256):
            for j in range(n):
                np[j] = (i,0,0)
            np.write()
            time.sleep_ms(20)
        for i in range(255, 45 ,-1):
            for j in range(n):
                np[j] = (i,0,0)
            np.write()
            time.sleep_ms(20)
    finally:
        for i in range(n):
            np[i] = (0, 0, 0)
        np.write()
