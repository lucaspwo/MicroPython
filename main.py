# import reconnect, mqtt_casa
import reconnect, xmas_pc2

while(True):
    reconnect.connect()

    # mqtt_casa.conectar()                    # havendo sucesso na conexao, executar o codigo principal
    xmas_pc2.init()
