import socket
import ssl

# Connect to the mail server
mailserver = ("smtp.gmail.com", 587)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(mailserver)

# Receive server response
recv = clientSocket.recv(1024).decode()
print(recv)

# Send HELO command and get server response
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)


# Send MAIL FROM command
mailFrom = "MAIL FROM:<21223203062@cse.bubt.edu.bd>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send RCPT TO command
rcptTo = "RCPT TO:<tusar.cse78@gmail.com>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Send DATA command
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)

# Send the actual message
message = "Subject: Test Email\r\n\r\nHello! This is a test email."
clientSocket.send(message.encode())

# End the message with a period (.)
clientSocket.send("\r\n.\r\n".encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Send QUIT command to close the connection
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)

clientSocket.close()
