def init():
    import machine, neopixel, time, urandom

    np = neopixel.NeoPixel(machine.Pin(4), 23)
    n = np.n

    while True:

        for l in range(n):
            np[l] = (0,0,0)
        np.write()
        #print("lPULSE = %s" % config['lPULSE'])
        rand = urandom.getrandbits(2)
        #rand_o = rand
        if(rand == 0):
            for i in range(0, 200):
                for l in range(0, 4):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                # c.check_msg()
                # leds = config['all']
                # if leds[3] != 3:
                #     break
                time.sleep_ms(15)
            # if leds[3] == 4:
            for i in range(200, 0, -1):
                for l in range(0, 4):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                    # c.check_msg()
                    # leds = config['all']
                    # if leds[3] != 3:
                    #     break
                time.sleep_ms(15)

        if(rand == 1):
            for i in range(0, 200):
                for l in range(4, 10):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                # c.check_msg()
                # leds = config['all']
                # if leds[3] != 3:
                #     break
                time.sleep_ms(15)
            # if leds[3] == 4:
            for i in range(200, 0, -1):
                for l in range(4, 10):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                    # c.check_msg()
                    # leds = config['all']
                    # if leds[3] != 3:
                    #     break
                time.sleep_ms(15)

        if(rand == 2):
            for i in range(0, 200):
                for l in range(10, 18):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                # c.check_msg()
                # leds = config['all']
                # if leds[3] != 3:
                #     break
                time.sleep_ms(15)
            # if leds[3] == 4:
            for i in range(200, 0, -1):
                for l in range(10, 18):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                    # c.check_msg()
                    # leds = config['all']
                    # if leds[3] != 3:
                    #     break
                time.sleep_ms(15)

        if(rand == 3):
            for i in range(0, 200):
                for l in range(18, 23):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                # c.check_msg()
                # leds = config['all']
                # if leds[3] != 3:
                #     break
                time.sleep_ms(15)
            # if leds[3] == 4:
            for i in range(200, 0, -1):
                for l in range(18, 23):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                    # c.check_msg()
                    # leds = config['all']
                    # if leds[3] != 3:
                    #     break
                time.sleep_ms(15)