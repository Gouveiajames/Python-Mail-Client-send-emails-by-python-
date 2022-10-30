from socket import * 

msg = ”\r\n I love computer networks!” 

endmsg = ”\r\n.\r\n”

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.gmail.com"#Fill in start   #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver 
#Fill in start
serverPort = 25

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort)) 

#Fill in end

#print info about the connection or an error message
recv = clientSocket.recv(1024)
print recv

if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)

recv1 = clientSocket.recv(1024)
print recv1

if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
# Fill in start
#mailFrom = "james@csus.edu\r\n"
mailFrom = "MAIL FROM"
clientSocket.send(mailFrom)

recv2 = clientSocket.recv(1024)
print recv2

# Fill in end 

# Send RCPT TO command and print server response. 
#mailTo = "jamesgouveia@csus.edu"
mailTo = "RCPT TO"
clientSocket.send(mailTo)

recv3 = clientSocket.recv(1024)
print recv3

# Send DATA command and print server response.
data = "DATA"
clientSocket.send(mdata)

recv3 = clientSocket.recv(1024)
print recv3

# Send message data.

# Message ends with a single period.

# Send QUIT command and get server response. 
clientSocket.close()


