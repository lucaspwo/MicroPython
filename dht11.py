import dht
import machine
import time
d = dht.DHT11(machine.Pin(13))
def ler():
    while True:
        d.measure()
        print('Temp: %s' % d.temperature())
        print('Hum: %s' % d.humidity())
        time.sleep(1)
