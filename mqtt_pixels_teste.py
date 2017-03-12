import machine, neopixel, time, network, utime, json, os
from umqtt.simple import MQTTClient
np = neopixel.NeoPixel(machine.Pin(4), 23)
n = np.n

wlan = network.WLAN(network.STA_IF)
while not wlan.isconnected():
    utime.sleep(1)

preJson = open('ledsConfig.txt').read()
config = json.loads(preJson)
leds = config['all']

# config = {
#     'lRED': 255,
#     'lGREEN': 0,
#     'lBLUE': 0,
#     'lPULSE': 1,
#     'lPULSETIME': 15
# }

SERVER = "192.168.0.12"
tALL = b"/led/all"
# tRED = b"/led/red"
# tGREEN = b"/led/green"
# tBLUE = b"/led/blue"
# tPULSE = b"/led/pulse"
# tPULSETIME = b"/led/pulsetime"
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

    os.remove('ledsConfig.txt')
    data = json.dumps(config)
    f = open('ledsConfig.txt', 'w')
    f.write(data)
    f.close()

# wlan = network.WLAN(network.STA_IF)
# wlan.connect('BonoNet', 'bonooliveira402')
#
# time.sleep(5)


#if wlan.isconnected():

c = MQTTClient(ID, SERVER)
c.set_callback(sub_cb)
c.connect()
c.subscribe(tALL)
# c.subscribe(tRED)
# c.subscribe(tGREEN)
# c.subscribe(tBLUE)
# c.subscribe(tPULSE)
# c.subscribe(tPULSETIME)


while True:

    c.check_msg()
    leds = config['all']

    if leds[3] == 0:
        #print("lPULSE = %s" % config['lPULSE'])
        for l in range(n):
            np[l] = (leds[0], leds[1], leds[2])
        np.write()
        c.check_msg()
        time.sleep_ms(1)

    if leds[3] == 1:
        #print("lPULSE = %s" % config['lPULSE'])
        for i in range(40, 255):
            for l in range(n):
                np[l] = (i,0,0)
            np.write()
            c.check_msg()
            leds = config['all']
            if leds[3] == 0:
                break
            time.sleep_ms(leds[4])
        if leds[3] == 1:
            for i in range(255, 40, -1):
                for l in range(n):
                    np[l] = (i,0,0)
                np.write()
                c.check_msg()
                leds = config['all']
                if leds[3] == 0:
                    break
                time.sleep_ms(leds[4])

    c.check_msg()
