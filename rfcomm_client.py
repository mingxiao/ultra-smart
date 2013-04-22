import bluetooth
import sys,serial,time
import re


def parse_reading(data):
    """
    @param data - string of data

    Returns a number if a reading is found otherwise return -1
    """
    pat =re.compile('([1-9][0-9]*)')
    datum = data.split('\n')
    #print datum
    for d in datum:
        m = pat.search(d)
        if m is not None:
            return float(m.group(1))
    return float(-1)

def connect(MAC, port=1,time=1):
    global sock
    try:
        sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        sock.connect((MAC, port))
        sock.settimeout(time)
    except Exception,e:
        print 'Exception: %s'%e
        #raise Exception('%s connection error at port %s'%(MAC,port))


if __name__ == '__main__':
    bd_addr = "00:12:10:23:10:18" #itade address
    port = 1
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bd_addr, port))
    print 'Connected'
    while True:
        time.sleep(.5)
        print '======='
        data = sock.recv(64)
        print 'data',data
        print 'reading:',parse_reading(data)
    sock.close()
