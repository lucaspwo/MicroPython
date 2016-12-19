#https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
#https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/example_pub.py
#https://github.com/micropython/micropython-lib/pull/91#issuecomment-239030008

def conectar():
    from umqtt.simple import MQTTClient
    #import micropython

    SERVER = "10.6.1.112"
    TOPIC = b"/teste"
    ID = "esp"
    USER = b"esp"
    PASSWORD = b"senhaesp"

    c = MQTTClient(ID, SERVER, user=USER, password=PASSWORD)
    c.connect()
    c.publish(TOPIC, b"test")
    c.disconnect()
