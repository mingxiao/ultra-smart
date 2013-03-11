import bluetooth

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
#port = 8080
server_sock.bind(("",port))

print 'Listening for clients'
server_sock.listen(1)

client_sock,address = server_sock.accept()
print "Accepted connection from ",address

client_sock.send('X')
print 'Sent X'
#data = client_sock.recv(1024)
#print "received [%s]" % data

client_sock.close()
server_sock.close()
