def init():
    import machine, neopixel, time, urandom
    np = neopixel.NeoPixel(machine.Pin(4), 23)
    n = np.n

    while True:

        for i in range(127):
            for j in range(0,4):
                np[j] = (0,i,0)
            for j in range(4,10):
                np[j] = (i,0,0)
            for j in range(10,18):
                np[j] = (0,i,0)
            for j in range(18,23):
                np[j] = (i,0,0)
            np.write()
            time.sleep_ms(15)
            
        for i in range(127, 0, -1):
            for j in range(0,4):
                np[j] = (0,i,0)
            for j in range(4,10):
                np[j] = (i,0,0)
            for j in range(10,18):
                np[j] = (0,i,0)
            for j in range(18,23):
                np[j] = (i,0,0)
            np.write()
            time.sleep_ms(15)