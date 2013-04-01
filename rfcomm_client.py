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
    if len(datum) < 1:
        return -1
    reading = datum[len(datum)/2]
    #print 'R:',reading
    #check that its an actual number, and not error output
    m = pat.search(reading)
    if m is not None:
        return int(m.group(1))
    else:
        return -1

def connect(MAC, port=1,time=1):
    global sock
    try:
        sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        sock.connect((MAC, port))
        sock.settimeout(time)
    except:
        print 'Connection error'


if __name__ == '__main__':
    bd_addr = "00:12:10:23:10:18" #itade address
    port = 1
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bd_addr, port))
    print 'Connected'
    while True:
        time.sleep(.5)
        print '======='
        data = sock.recv(32)
        print data
        print 'reading:',parse_reading(data)
    sock.close()
