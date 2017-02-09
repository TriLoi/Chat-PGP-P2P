#server
import socket
import signal
import sys
import urllib 


#########################
# PARAMETERS
#########################
port = 80
max_connections = 5
showRequest = False
width_px = 700
height_px = 500

id_new_message = "newMessage"
id_new_connection = "newConnection"
id_submit = "submit"

libelle_localhost = "Moi"
label_cancel = "Annuler"
label_ip_address = "Adresse IP"
label_add_new_connection = "Ajouter Contact"

value_new_message = "Partager"
value_new_connection = "Ajouter"
value_update_messages = "update"


#########################
# WEB CONTENTS
#########################
def getFormatedMessage(address, message):
	return '<div style="word-break: break-all;"><h4 style="margin: 0;">'+address+'</h4>'+message+'</div>'

def getFormatedConnection(address):
	return '<h4 style="margin: 0;">'+address+'</h4>'

def getWebContent():
	return """
<html>
	<head>
		<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
		<meta http-equiv="Content-Language" content="en-us" />
		<title>Local Web Chat</title>


		<script type="text/javascript">
			var ajaxCall = function(responseFunction, params){
				var xhttp = new XMLHttpRequest();
				xhttp.onreadystatechange = function() {
		  			if (this.readyState == 4 && this.status == 200) {
		    				responseFunction(this.responseText);
		  			}
				};
				xhttp.open("POST", "127.0.0.1", true);
				xhttp.send(params);
			}

			var updateMessage = function(){
				ajaxCall(function(response){
					document.getElementById(\'message_place\').innerHTML=response;
					setTimeout(updateMessage, 1000);
				},\""""+id_submit+'='+value_update_messages+"""\")
			}

			setTimeout(updateMessage, 1000);
		</script>


	</head>
	<body style="width: """+str(width_px)+'px; height: '+str(height_px)+"""px; margin: auto; overflow-y: hidden; padding: 10px; background-color: black;">
		<form action="#" method="POST" style="height: 100%; width: 100%;">


			<div id="accept_connection_form" style="display:none; background-color: rgba(0,0,0,0.5); height: 100%; width: 100%; position: absolute;">
	      	</div>


			<div id="add_connection_form" style="display:none; background-color: rgba(0,0,0,0.5); height: 100%; width: 100%; position: absolute;">
				<table style="width: """+str(width_px/2)+'px; height: '+str(height_px/2)+'px; position: absolute; background-color: white; z-index: 1; left: '+str(width_px/4)+'px; top: '+str(height_px/4)+"""px; border: 2px solid rgb(70,70,70);">
			  		<tr style="height: 75%;">
			    			<td colspan=2>
			      				<div style="width: 80%; margin: auto;">
								<label for=\""""+id_new_connection+'">'+label_ip_address+"""</label>
								<input type="text" style="width: 100%;" maxlength="15" name=\""""+id_new_connection+"""\"/>
			     				 </div>
			    			</td>
			  		</tr>
			  		<tr style="height: 25%;">
			    			<td style="width: 50%;">\
			      				<input type="submit" style="width: 100%; height: 100%;" name=\""""+id_submit+'" value="'+value_new_connection+"""\"/>
			    			</td>
			    			<td style="width: 50%;">
			      				<button type="button" style="width: 100%; height: 100%;" onclick="document.getElementById('add_connection_form').style.display='none';">"""+label_cancel+"""</button>
			    			</td>
			  		</tr>
				</table>
	      	</div>


			<table style="height: 100%; width: 100%">
				<tr>
			  		<td style="width: 75%; padding:10px; padding-top: 0;" colspan=2>
			    			<div id="message_place" style="height: """+str(height_px*18/25)+'px; width: 100%; overflow-y: scroll; background-color: rgb(240, 240, 240);">'+str_messages+"""</div>
			  		</td>
			  		<td rowspan=2>
			    			<div style="background-color: rgb(240, 240, 240); height: 100%">
			      				<div id="connections_place" style="height: 90%; width: """+str(width_px*171/700)+'px; overflow-y: scroll; overflow-x: hidden; background-color: rgb(240, 240, 240);">'+str_connections+"""</div>
			      				<button type="button" style="width: 100%; height: 10%;" onclick="document.getElementById('add_connection_form').style.display='inline';">"""+label_add_new_connection+"""</button>
			    			</div>
			  		</td>
				</tr>
				<tr style="height:25%;">
			  		<td style="width: 55%;">
			    			<textarea style="width: 100%; background-color: white; border: 2px solid black; height: 90%; background-color: rgb(240, 240, 240); resize: none;" name=\""""+id_new_message+"""\"></textarea>
			  		</td>
			  		<td style="width: 20%;">
			    			<input type="submit" style="width: 100%; height: 100%;" name=\""""+id_submit+'" value="'+value_new_message+"""\"/>
			  		</td>
				</tr>
		      	</table>


		</form>
	</body>
</html>"""


#########################
# VARIABLES
#########################
connections = []
str_connections = ""
str_messages = ""


#########################
# MAIN SCRIPT
#########################
def onCtrlC(signal, frame):
	print ""
	print "--- close ---"
	sock_src.close()
	sys.exit(0)

signal.signal(signal.SIGINT, onCtrlC)

def URLunescape(string):
	return urllib.unquote(string.replace('+',' ')).decode('utf8') 

def extractVariable(variable_name,request):
	iDeb = request.find(variable_name+"=")
	iDebVal = request[iDeb:].find("=") + iDeb + 1
	iFinVal = request[iDebVal:].find("&") + iDebVal

	if(iFinVal < iDebVal):
		return URLunescape(request[iDebVal:])
	
	return URLunescape(request[iDebVal:iFinVal])

def getResponseRequest(request):
	global str_messages
	global str_connections
	global connections

	action = extractVariable(id_submit,request)

	if(action==value_update_messages):
		return str_messages

	if(action==value_new_message):
		message = extractVariable(id_new_message,request)
		str_messages = str_messages + getFormatedMessage(libelle_localhost, message)
		for connection in connections:
    			connection.send(message)

	if(action==value_new_connection):
		connection = extractVariable(id_new_connection,request)
		str_connections = str_connections + getFormatedConnection(connection)

		sock_dest = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock_dest.connect((connection, port))

		connections.append(sock_dest)

	return getWebContent()

#main
sock_src = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_src.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_src.bind(('', port))
sock_src.listen(max_connections)
print "--- listen on port " + str(port) + " ---"
print ""

while True:
	client, address = sock_src.accept()
	request = client.recv(1000)

	print "--- receive from " + address[0] + ":" + str(address[1]) + " ---"
	if(showRequest):
		print request
		print ""

	if(address[0]=="127.0.0.1"): client.send(getResponseRequest(request))
	#elif(
	else: str_messages = str_messages + getFormatedMessage(address[0], request)

	client.close()
		


