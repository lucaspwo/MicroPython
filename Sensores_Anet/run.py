import time, utime, machine, onewire, ds18x20, network
from umqtt.simple import MQTTClient

wlan = network.WLAN(network.STA_IF)
while not wlan.isconnected():
    utime.sleep(1)

SERVER = "206.189.191.14"
TOPIC1 = b"/esp/temp"
TOPIC2 = b"/esp/smoke"
TOPICR = b"/esp/daymsgr"
TOPICS = b"/esp/daymsgs"
ID = "esp"

mens = ''

def sub_cb(topic, msg):
    global mens
    mens = msg.decode("utf-8")

dat = machine.Pin(5)
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
    c.publish(TOPICS, mens.encode())
    time.sleep_ms(2000)