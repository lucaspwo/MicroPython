import machine, neopixel, time, network, urandom

np = neopixel.NeoPixel(machine.Pin(4), 23)
n = np.n

def mqtt_config():
    import json
    from umqtt.simple import MQTTClient

    preJson = open('config.txt').read()         # abertura do arquivo de configuracoes
    data = json.loads(preJson)
    config = data['campos']

    preJson = open('ledsConfig.txt').read()
    config = json.loads(preJson)
    leds = config['all']

    SERVER = '192.168.0.31'
    tALL = b"/led/all"
    ID = "esp"

    def sub_cb(topic, msg):
        #global state
        msg = msg.decode("utf-8")
        leds = msg.split(",")
        for i in range(0,5):
            leds[i] = int(leds[i])
        #print((topic, msg))
        if topic == tALL:
            config['all'] = leds
        # if topic == tRED:
        #     config['r'] = msg
        # if topic == tGREEN:
        #     config['g'] = msg
        # if topic == tBLUE:
        #     config['b'] = msg
        # if topic == tPULSE:
        #     config['p'] = msg
        #     #print(config['lPULSE'])
        # if topic == tPULSETIME:
        #     config['t'] = msg

        #os.remove('ledsConfig.txt')
        data = json.dumps(config)
        f = open('ledsConfig.txt', 'w')
        f.write(data)
        f.close()

    c = MQTTClient(ID, SERVER)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(tALL)

def led0():
    #print("lPULSE = %s" % config['lPULSE'])
    for l in range(n):
        np[l] = (leds[0], leds[1], leds[2])
    np.write()
    c.check_msg()
    time.sleep_ms(1)

def led1():
    for i in range(40, 255):
        for l in range(n):
            np[l] = (i,0,0)
        np.write()
        c.check_msg()
        leds = config['all']
        if leds[3] != 1:
            break
        time.sleep_ms(leds[4])
    if leds[3] == 1:
        for i in range(255, 40, -1):
            for l in range(n):
                np[l] = (i,0,0)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 1:
                break
            time.sleep_ms(leds[4])

def led2():
    for i in range(40, 255):
        for l in range(n):
            np[l] = (i,i,i)
        np.write()
        c.check_msg()
        leds = config['all']
        if leds[3] != 2:
            break
        time.sleep_ms(leds[4])
    if leds[3] == 2:
        for i in range(255, 40, -1):
            for l in range(n):
                np[l] = (i,i,i)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 2:
                break
            time.sleep_ms(leds[4])

def led3():
    for l in range(n):
        np[l] = (0,0,0)
    np.write()
    #print("lPULSE = %s" % config['lPULSE'])
    rand = urandom.getrandbits(2)
    #rand_o = rand
    if(rand == 0):
        for i in range(0, 200):
            for l in range(0, 4):
                np[l] = (i,i,i)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 3:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 3:
            for i in range(200, 0, -1):
                for l in range(0, 4):
                    np[l] = (i,i,i)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 3:
                    break
                time.sleep_ms(leds[4])

    if(rand == 1):
        for i in range(0, 200):
            for l in range(4, 10):
                np[l] = (i,i,i)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 3:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 3:
            for i in range(200, 0, -1):
                for l in range(4, 10):
                    np[l] = (i,i,i)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 3:
                    break
                time.sleep_ms(leds[4])

    if(rand == 2):
        for i in range(0, 200):
            for l in range(10, 18):
                np[l] = (i,i,i)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 3:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 3:
            for i in range(200, 0, -1):
                for l in range(10, 18):
                    np[l] = (i,i,i)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 3:
                    break
                time.sleep_ms(leds[4])

    if(rand == 3):
        for i in range(0, 200):
            for l in range(18, 23):
                np[l] = (i,i,i)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 3:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 3:
            for i in range(200, 0, -1):
                for l in range(18, 23):
                    np[l] = (i,i,i)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 3:
                    break
                time.sleep_ms(leds[4])

def led4():
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
            c.check_msg()
            leds = config['all']
            if leds[3] != 3:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 4:
            for i in range(200, 0, -1):
                for l in range(0, 4):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 3:
                    break
                time.sleep_ms(leds[4])

    if(rand == 1):
        for i in range(0, 200):
            for l in range(4, 10):
                if l%2 == 0:
                    np[l] = (i,0,0)
                elif l%2 == 1:
                    np[l] = (0,i,0)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 3:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 4:
            for i in range(200, 0, -1):
                for l in range(4, 10):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 3:
                    break
                time.sleep_ms(leds[4])

    if(rand == 2):
        for i in range(0, 200):
            for l in range(10, 18):
                if l%2 == 0:
                    np[l] = (i,0,0)
                elif l%2 == 1:
                    np[l] = (0,i,0)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 3:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 4:
            for i in range(200, 0, -1):
                for l in range(10, 18):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 3:
                    break
                time.sleep_ms(leds[4])

    if(rand == 3):
        for i in range(0, 200):
            for l in range(18, 23):
                if l%2 == 0:
                    np[l] = (i,0,0)
                elif l%2 == 1:
                    np[l] = (0,i,0)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 3:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 4:
            for i in range(200, 0, -1):
                for l in range(18, 23):
                    if l%2 == 0:
                        np[l] = (i,0,0)
                    elif l%2 == 1:
                        np[l] = (0,i,0)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 3:
                    break
                time.sleep_ms(leds[4])

def led5():
    for l in range(n):
        np[l] = (0,0,0)
    np.write()
    #print("lPULSE = %s" % config['lPULSE'])
    rand = urandom.getrandbits(2)
    #rand_o = rand
    if(rand == 0):
        for i in range(0, 200):
            for l in range(0, 4):
                np[l] = (i,0,0)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 4:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 5:
            for i in range(200, 0, -1):
                for l in range(0, 4):
                    np[l] = (i,0,0)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 4:
                    break
                time.sleep_ms(leds[4])

    if(rand == 1):
        for i in range(0, 200):
            for l in range(4, 10):
                np[l] = (i,0,0)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 4:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 5:
            for i in range(200, 0, -1):
                for l in range(4, 10):
                    np[l] = (i,0,0)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 4:
                    break
                time.sleep_ms(leds[4])

    if(rand == 2):
        for i in range(0, 200):
            for l in range(10, 18):
                np[l] = (i,0,0)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 4:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 5:
            for i in range(200, 0, -1):
                for l in range(10, 18):
                    np[l] = (i,0,0)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 4:
                    break
                time.sleep_ms(leds[4])

    if(rand == 3):
        for i in range(0, 200):
            for l in range(18, 23):
                np[l] = (i,0,0)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] != 4:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 5:
            for i in range(200, 0, -1):
                for l in range(18, 23):
                    np[l] = (i,0,0)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] != 4:
                    break
                time.sleep_ms(leds[4])