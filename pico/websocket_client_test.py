import uwebsockets.client

websocket = uwebsockets.client.connect("ws://192.168.236.169:9080/")
websocket.send("hello world")
