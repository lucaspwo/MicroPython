# import reconnect, mqtt_casa
import reconnect, xmas_pc

while(True):
    reconnect.connect()

    # mqtt_casa.conectar()                    # havendo sucesso na conexao, executar o codigo principal
    xmas_pc.init()
