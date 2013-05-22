import bluetooth
import sys,serial,time
import re
import argparse

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

def MAC_valid(mac):
    """
    Returns true if the given MAC address is valid:
    HH:HH:HH:HH:HH:HH
    """
    regex = re.compile(r"[0-9a-f]{2}([-:])[0-9a-f]{2}(\1[0-9a-f]{2}){4}$")
    m = regex.search(mac.lower())
    return m is not None

def read():
    global sock
    while True:
        time.sleep(1)
        print sock.recv(64)

descript = """
Connect to bluetooth device and read data
"""

if __name__ == '__main__':
    global sock
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--address',help='MAC address of bluetooth device')
    parser.add_argument('-p','--port',help='rfcomm port number',type=int)
    args = parser.parse_args()
    if args.address and args.port:
        if not MAC_valid(args.address):
            raise Exception('Invalid MAC address: {}'.format(args.address))
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((args.address,args.port))
        read()
        parser.exit(message = "Fininished reading\n")
        pass
        
##    bd_addr = "00:12:10:23:10:18" #itade address
##    itade2 = '00:12:12:10:90:88'
##    port = 2

