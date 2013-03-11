import bluetooth

#bd_addr = "01:23:45:67:89:AB"
#bd_addr = "localhost"
#bd_addr = "00:1b:63:3a:26:72"
bd_addr = "00:12:10:23:10:18" #itade address

port = 1
#port = 8080

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")
print 'Sent data'

sock.close()
