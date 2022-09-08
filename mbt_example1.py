from pyModbusTCP.server import ModbusServer

server = ModbusServer("127.0.0.1", 12345, no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    while True:
        continue
except:
    print("Shutdown server...")
    server.stop()
    print("Server is offline")

