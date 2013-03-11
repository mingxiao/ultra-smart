import bluetooth
import select

class MyDiscoverer (bluetooth.DeviceDiscoverer) :
    """
    http://www.plugcomputer.org/plugforum/index.php?topic=2250.0
    Kludge to work around bluetooth.discover_devices not working.
    To get the list of device address:
        MyDiscoverer().discover_my_devices()
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

devices = MyDiscoverer().discover_my_devices() 
#for addr in devices:
#    print "%s | %s"%(addr, bluetooth.lookup_name(addr))
    
