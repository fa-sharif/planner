import asyncio
import websockets
import requests

async def test():
    response = requests.post('http://localhost:8000/api/users/token/', json={
        'username': 'ehsan',
        'password': '67890'
    })
    
    print("STATUS CODE:", response.status_code)
    print("RESPONSE TEXT:", response.text)

    access_token = response.json().get('access')
    print(access_token)

    if not access_token:
        print('❌ Failed to get token')
        return

    # 🛠️ توکن را در URL بفرست
    uri = f"ws://localhost:8000/ws/notifications/?token={access_token}"

    async with websockets.connect(uri) as websocket:
        print("✅ Connected to WebSocket")
        response = await websocket.recv()
        print("👋 Server:", response)

        while True:
            message = await websocket.recv()
            print("📩 Notification:", message)

asyncio.run(test())
