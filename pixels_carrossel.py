import machine, neopixel, time
np = neopixel.NeoPixel(machine.Pin(4), 10)
n = np.n

def Wheel (WheelPos):
    WheelPos = 255 - WheelPos
    if(WheelPos < 85):
        cores = (255 - WheelPos * 3, 0, WheelPos * 3)
        return cores

    if(WheelPos < 170):
        WheelPos -= 85
        cores = (0, WheelPos * 3, 255 - WheelPos * 3)
        return cores

    WheelPos -= 170
    cores = (WheelPos * 3, 255 - WheelPos * 3, 0)
    return cores


while True:

    for j in range(0, 256):     # cycle all 256 colors in the wheel
        for q in range(0, 3):
            for i in range(0, np.n, 3):
                np[i+q] = Wheel((i+j) % 255)
                #strip.setPixelColor(i+q, Wheel( (i+j) % 255));    #turn every third pixel on
            np.write();

            time.sleep_ms(250);

            for i in range(0, np.n, 3):
                n[i+q] = (0, 0, 0)
                #strip.setPixelColor(i+q, 0);        #turn every third pixel off

    # r = 0
    # g = 0
    # b = 0
    # while r < 256:
    #     for z in range(n):
    #         r = r + 1
    #         np[z] = (255-r, r, 0)
    #         np.write()
    #     time.sleep_ms(250)
    # while g < 256:
    #     for z in range(n):
    #         g = g + 1
    #         np[z] = (0, 255-g, g)
    #         np.write()
    #     time.sleep_ms(250)
    # while b < 256:
    #     for z in range(n):
    #         b = b + 1
    #         np[z] = (b, 0, 255-b)
    #         np.write()
    #     time.sleep_ms(250)

    # for i in range(255):
    #     for l in range(n):
    #         np[l] = (255-i,i,0)
    #     np.write()
    #     time.sleep_ms(30)
    # for j in range(255):
    #     for l in range(n):
    #         np[l] = (0,255-j,j)
    #     np.write()
    #     time.sleep_ms(30)
    # for k in range(255):
    #     for l in range(n):
    #         np[l] = (k,0,255-k)
    #     np.write()
    #     time.sleep_ms(30)
