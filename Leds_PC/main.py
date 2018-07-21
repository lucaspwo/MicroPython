import leds
def conectar():
    import reconnect
    reconnect.connect()

def run():
    leds.mqttConfig()
# import reconnect, xmas_pc2

conectar()
run()

# while(True):
    # conectar()
    # leds.mqttConfig()                    # havendo sucesso na conexao, executar o codigo principal
    # xmas_pc2.init()
