import asyncio
import json
import time
import websockets

loop = asyncio.get_event_loop()

async def serve_requests(websocket, path):
  # Receive and parse a message from the browser.
  command = json.loads(await websocket.recv())
  print("Received command {}".format(command))

  # Loop infinitely and send a new message every second.
  i = 0
  while True:
    payload = {"counter": i,
               "time": time.time()}
    await websocket.send(json.dumps(payload))
    await asyncio.sleep(1)
    i += 1

if __name__ == "__main__":
  start_server = websockets.serve(serve_requests, "localhost", "12345")
  loop.run_until_complete(start_server)
  loop.run_forever()
