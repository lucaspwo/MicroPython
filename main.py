import mqtt_casa, reconnect

while(True):
    reconnect.connect()

    mqtt_casa.conectar()                    # havendo sucesso na conexao, executar o codigo principal
