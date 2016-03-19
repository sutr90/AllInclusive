import serial
import DeviceClient
import datetime

# START: Azure IoT Hub settings
KEY = "lMFnJkQV9abr4kWKrrkFLLN2uNHoLs5k+EVtaAO6ehk="
HUB = "AH2016Sahaci"
DEVICE_NAME = "device0"
# END: Azure IoT Hub settings

device = DeviceClient.DeviceClient(HUB, DEVICE_NAME, KEY)

device.create_sas(600)

with serial.Serial('/dev/ttyUSB0', 115200) as ser:
        while True:
                msg = ser.readline().decode('utf-8').strip()
                msgs = msg.split(';')[:-1]

                # Device to Cloud
                msg = """{{ 'ts': '{}', 'id_sensor': {}, 'distance': {} }}"""
                for m in msgs:
                        data = m.split('=')
                        jsonmsg = msg.format(str(datetime.datetime.now()), data[0], data[1])
                        print(jsonmsg)
                        print(device.send(jsonmsg.encode()))





