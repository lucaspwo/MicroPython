#https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
#https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/example_pub.py
#https://github.com/micropython/micropython-lib/pull/91#issuecomment-239030008

def conectar():
    import dht
    import machine
    import time
    d = dht.DHT11(machine.Pin(13))
    from umqtt.simple import MQTTClient
    #import micropython

    SERVER = "10.6.1.112"
    TOPIC1 = b"/esp/dht/temp"
    TOPIC2 = b"/esp/dht/hum"
    ID = "esp"
    USER = b"esp"
    PASSWORD = b"senhaesp"

    c = MQTTClient(ID, SERVER, user=USER, password=PASSWORD)
    #c.connect()

    while True:
        #try:
        c.connect()
        d.measure()
        temp = d.temperature()
        hum = d.humidity()
        print('Temp: %s' % temp)
        print('Hum: %s' % hum)
        c.publish(TOPIC1, str(temp))
        c.publish(TOPIC2, str(hum))
        c.disconnect()
        time.sleep(30) #30 segundos
        #finally:
            #c.disconnect()
