@tool
extends Node3D

func _on_server_message_recieved(message: String) -> void:
	var json := JSON.new()
	var error := json.parse(message)
	if error == OK:
		var message_data: Variant = json.data
		rotation.x = message_data.x
		rotation.z = message_data.y
	else:
		print("JSON Parse Error: ", json.get_error_message())
