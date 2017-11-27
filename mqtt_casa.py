def conectar():
    import json

    preJson = open('config.txt').read()         # abertura do arquivo de configuracoes
    data = json.loads(preJson)
    config = data['campos']

    preJson = open('ledsConfig.txt').read()
    config = json.loads(preJson)
    leds = config['all']

    from leds import mqtt_config
    mqtt_config()

    while True:

        mqtt_config.c.check_msg()
        leds = config['all']

        if leds[3] == 0:
            from leds import led0
            led0()

        if leds[3] == 1:
            from leds import led1
            led1()

        if leds[3] == 2:
            from leds import led2
            led2()

        if leds[3] == 3:
            from leds import led3
            led3()

        if leds[3] == 4:
            from leds import led4
            led4()

        if leds[3] == 5:
            from leds import led5
            led5()

        mqtt_config.c.check_msg()