from pyModbusTCP.server import ModbusServer
from time import sleep
from random import uniform

server = ModbusServer("127.0.0.1", 12345, no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    state = [0]
    while True:
        server.data_bank.set_holding_registers(0, [int(uniform(0, 100))])
        if state != server.data_bank.get_holding_registers(1):
            state = server.data_bank.get_holding_registers(1)
            print("Value of register 1 has changed to " + str(state))
            sleep(0.5)
except:
    print("Shutdown server...")
    server.stop()
    print("Server is offline")

