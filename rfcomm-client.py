import bluetooth
import sys,serial,time
import re


def parse_reading(data):
    """
    @param data - string of data

    Returns a number if a reading is found otherwise return -1
    """
    pat =re.compile('([1-9][0-9]*).')
    datum = data.split()
    #get middle value since chances are it didn't get chopped
    #during transmission
    reading = datum[len(datum)/2]
    #print 'R:',reading
    #check that its an actual number, and not error output
    m = pat.search(reading)
    if m is not None:
        return m.group(1)
    else:
        return -1

def connect():
    pass

bd_addr = "00:12:10:23:10:18" #itade address

port = 1
#port = 8080


sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print 'Connected'
#sock.bind((bd_addr,port))
pat = re.compile('([1-9][0-9]*).')
while True:
    time.sleep(1)
    print '======='
    data = sock.recv(32)
    print data
    print data.split()
    print 'reading:',parse_reading(data)
#while True:pass
sock.close()
