#https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
#https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/example_sub_led.py
#https://github.com/micropython/micropython-lib/pull/91#issuecomment-239030008

def conectar():
    from umqtt.simple import MQTTClient
    #import micropython

    SERVER = "10.6.1.112"
    TOPIC = b"/rfid/normal"
    ID = "esp"
    USER = b"esp"
    PASSWORD = b"senhaesp"

    def sub_cb(topic, msg):
        #global state
        print((topic, msg))

    c = MQTTClient(ID, SERVER, user=USER, password=PASSWORD)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    #c.publish(b"test",b"test")

    try:
        while True:
            #micropython.mem_info()
            c.wait_msg()
    finally:
        c.disconnect()
