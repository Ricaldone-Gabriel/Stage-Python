import socketio
import asyncio
#Necessita: websocket-client e python-socketio e aiohttp
async def main():
    sio = socketio.AsyncClient()
    print("Test")
    @sio.event
    async def connect():
        print('Connected')

    @sio.event
    async def disconnect():
        print('Disconnected')

    await sio.connect('http://localhost:8080', transports=["websocket"])
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())

#
#  ---------       ----------
#  |  Web  | <---- | Python | <---- Term
#  | Server| ----> | Server | <---- Term
#  ---------       ----------
#
#  Il server python raccoglie dati dai termometri, quando il web server richiede dei plot nuovi il server python risponde.

# Crea un socket server per i termometri
