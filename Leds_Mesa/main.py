import leds_mesa, reconnect

reconnect.connect()

leds_mesa.mqttConfig()                    # havendo sucesso na conexao, executar o codigo principal