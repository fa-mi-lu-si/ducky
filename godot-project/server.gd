@tool
extends Node

## The port the server will listen on.
const PORT = 9080

signal message_recieved(message: String)

var tcp_server := TCPServer.new()
var socket := WebSocketPeer.new()

func log_message(message: String) -> void:
	print("Message:\n\t" + message)


func _ready() -> void:
	if tcp_server.listen(PORT) != OK:
		log_message("Unable to start server.")
		set_process(false)
	
	print("started running the websocket server")


func _process(_delta: float) -> void:
	while tcp_server.is_connection_available():
		var conn: StreamPeerTCP = tcp_server.take_connection()
		assert(conn != null)
		socket.accept_stream(conn)

	socket.poll()

	if socket.get_ready_state() == WebSocketPeer.STATE_OPEN:
		while socket.get_available_packet_count():
			message_recieved.emit(socket.get_packet().get_string_from_ascii())


func _exit_tree() -> void:
	print("stopping the websocket server")
	socket.close()
	tcp_server.stop()
