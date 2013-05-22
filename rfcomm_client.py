import bluetooth
import sys,serial,time
import re
import argparse
import select

class MyDiscoverer (bluetooth.DeviceDiscoverer) :
    """Kludge to work around bluetooth.discover_devices not working
    Usage: MyDiscoverer.discover_my_devices()
    """
    def pre_inquiry (self) :
        self.done = False
    def device_discovered(self, address, device_class, name):
        # print "%s - %s" % (address , name)
        if address not in self.discovered_list:
            self.discovered_list.append(address)
    def inquiry_complete(self) :
        self.done = True
    def discover_my_devices(self):
        self.discovered_list = []
        self.find_devices(lookup_names = False)
        while True :
            can_read, can_write, has_exc = select.select ([self ], [ ], [ ])
            if self in can_read :                             
                self.process_event()                               
            if self.done :
                break
        return self.discovered_list

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
    parser.add_argument('-d','--discover',help='Discover devices',action='store_true')
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
    elif args.discover:
        d = MyDiscoverer()
        lst = d.discover_my_devices()
        for device in lst:
            print device
            #print "{}   {}".format(device,bluetooth.lookup_name(device))
        parser.exit(message= "Discovered devices\n")

