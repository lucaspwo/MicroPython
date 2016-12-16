import machine, neopixel, time, network
from umqtt.simple import MQTTClient
np = neopixel.NeoPixel(machine.Pin(4), 10)
n = np.n

config = {
    'lRED': 255,
    'lGREEN': 0,
    'lGREEN': 0,
    'lBLUE': 0,
    'lPULSE': 1,
    'lPULSETIME': 15
}



SERVER = "192.168.0.27"
tRED = b"/led/red"
tGREEN = b"/led/green"
tBLUE = b"/led/blue"
tPULSE = b"/led/pulse"
tPULSETIME = b"/led/pulsetime"
ID = "esp"

def sub_cb(topic, msg):
    #global state
    msg = int(msg)
    print((topic, msg))
    if topic == tRED:
        config['lRED'] = msg
    if topic == tGREEN:
        config['lGREEN'] = msg
    if topic == tBLUE:
        config['lBLUE'] = msg
    if topic == tPULSE:
        config['lPULSE'] = msg
        #print(config['lPULSE'])
    if topic == tPULSETIME:
        config['lPULSETIME'] = msg

# wlan = network.WLAN(network.STA_IF)
# wlan.connect('BonoNet', 'bonooliveira402')
#
# time.sleep(5)

#while True:

#if wlan.isconnected():

c = MQTTClient(ID, SERVER)
c.set_callback(sub_cb)
c.connect()
c.subscribe(tRED)
c.subscribe(tGREEN)
c.subscribe(tBLUE)
c.subscribe(tPULSE)
c.subscribe(tPULSETIME)


while True:

    c.check_msg()

    if config['lPULSE'] == 0:
        #print("lPULSE = %s" % config['lPULSE'])
        for l in range(n):
            np[l] = (config['lRED'], config['lGREEN'], config['lBLUE'])
        np.write()
        c.check_msg()
        time.sleep_ms(10)

    if config['lPULSE'] == 1:
        #print("lPULSE = %s" % config['lPULSE'])
        for i in range(40, 255):
            for l in range(n):
                np[l] = (i,0,0)
            np.write()
            c.check_msg()
            if config['lPULSE'] == 0:
                break
            time.sleep_ms(config['lPULSETIME'])
        if config['lPULSE'] == 1:
            for i in range(255, 40, -1):
                for l in range(n):
                    np[l] = (i,0,0)
                np.write()
                c.check_msg()
                if config['lPULSE'] == 0:
                    break
                time.sleep_ms(config['lPULSETIME'])

    c.check_msg()
