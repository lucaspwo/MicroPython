import machine, neopixel, time
np = neopixel.NeoPixel(machine.Pin(4), 10)
n = np.n

#VLAVAAV
#vermelho
#laranja
#amarelo
#verde
#anil
#azul
#violeta

def start():
    try:
        while True:
            for i in range(8, 256):
                for l in range(n):
                    #np[l] = (i,0,k-i)
                    np[l] = (i,1,-i)
                np.write()
                #print(i)
                time.sleep_ms(60)
            for j in range(8, 256):
                for l in range(n):
                    #np[l] = (i-j,j,0)
                    np[l] = (-j,j,1)
                np.write()
                #print(j)
                time.sleep_ms(60)
            for k in range(8, 256):
                for l in range(n):
                    #np[l] = (0,k-j,k)
                    np[l] = (1,-k,k)
                np.write()
                #print(k)
                time.sleep_ms(60)
    finally:
        for i in range(n):
            np[i] = (0, 0, 0)
        np.write()

def start2():
    try:
        while True:
            for i in range(0, 256):
                for l in range(n):
                    #np[l] = (i,0,k-i)
                    np[l] = (255-i,i,0)
                np.write()
                #print(i)
                time.sleep_ms(60)
            for j in range(0, 256):
                for l in range(n):
                    #np[l] = (i-j,j,0)
                    np[l] = (0,255-j,j)
                np.write()
                #print(j)
                time.sleep_ms(60)
            for k in range(0, 256):
                for l in range(n):
                    #np[l] = (0,k-j,k)
                    np[l] = (k,0,255-k)
                np.write()
                #print(k)
                time.sleep_ms(60)
    finally:
        for i in range(n):
            np[i] = (0, 0, 0)
        np.write()

def fade():
    try:
        while True:
            for i in range(45, 256):
                for j in range(n):
                    np[j] = (i,0,0)
                np.write()
                time.sleep_ms(20)
            for i in range(255, 45 ,-1):
                for j in range(n):
                    np[j] = (i,0,0)
                np.write()
                time.sleep_ms(20)
    finally:
        for i in range(n):
            np[i] = (0, 0, 0)
        np.write()
