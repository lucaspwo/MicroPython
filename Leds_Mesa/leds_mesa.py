def mqttConfig():
    import machine, neopixel, time, network, urandom, json
    from umqtt.simple import MQTTClient

    np = neopixel.NeoPixel(machine.Pin(5), 100)
    n = np.n

    preJson = open('ledsConfig.txt').read()
    config = json.loads(preJson)
    leds = config['all']

    SERVER = '192.168.0.34'
    TOPIC = b"/led/all"
    ID = "esp"
    #USER = b"lucas"
    #PASSWORD = b"9l11p02w31o5"

    def sub_cb(topic, msg):
        global leds
        msg = msg.decode("utf-8")
        leds = msg.split(",")
        for i in range(0,5):
            leds[i] = int(leds[i])
        print((topic, msg))
        if topic == TOPIC:
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
    c.subscribe(TOPIC)

    # import json

    # preJson = open('config.txt').read()         # abertura do arquivo de configuracoes
    # data = json.loads(preJson)
    # config = data['campos']

    def led0():
        leds = config['all']
        #print("lPULSE = %s" % config['lPULSE'])
        for l in range(n):
            np[l] = (leds[0], leds[1], leds[2])
        np.write()
        # print ("led0")
        # print (leds)
        c.check_msg()
        time.sleep_ms(1)

    while True:
        leds = config['all']
        # print("while")
        # print(leds)
        c.check_msg()
        
        if leds[3] == 0:
            led0()

        c.check_msg()