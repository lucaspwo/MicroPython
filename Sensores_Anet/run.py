def run():
    import time, utime, machine, onewire, ds18x20, network, neopixel
    from umqtt.simple import MQTTClient

    wlan = network.WLAN(network.STA_IF)
    while not wlan.isconnected():
        utime.sleep(1)

    rele = machine.Pin(14, machine.Pin.OUT)
    rele.off()

    np = neopixel.NeoPixel(machine.Pin(5), 10)
    n = np.n

    for i in range(n):
        np[i] = (127,127,127)

    np.write()

    relay = ''

    def sub_cb(topic, msg):
        global relay
        relay = msg.decode("utf-8")
        if(relay == '1'):
            rele.on()
        if(relay == '0'):
            rele.off()

    SERVER = "206.189.191.14"
    TOPIC1 = b"/esp/temp"
    TOPIC2 = b"/esp/smoke"
    TOPICS = b"/esp/relay/mcu"
    TOPICR = b"/esp/relay/node"
    ID = "esp"

    dat = machine.Pin(4)
    ds = ds18x20.DS18X20(onewire.OneWire(dat))
    roms = ds.scan()

    adc = machine.ADC(0)

    c = MQTTClient(ID, SERVER)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPICR)

    while True:

        c.check_msg()
        ds.convert_temp()
        time.sleep_ms(750)
        tmp = ds.read_temp(roms[0])
        stmp = str(tmp)
        btmp = stmp.encode()
        smk = adc.read()
        ssmk = str(smk)
        bsmk = ssmk.encode()
        print('temp: ', tmp)
        print('mq2: ', smk)
        c.publish(TOPIC1, btmp)
        c.publish(TOPIC2, bsmk)
        #time.sleep_ms(2000)