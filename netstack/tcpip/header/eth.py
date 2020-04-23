dst_MAC = 0
src_MAC = 6
eth_type = 12

ETHERNET_MINI_MUM_SIZE = 14
ETHERNET_ADDR_SIZE = 6

class ethernet_fields:

    def __init__(self, src_addr=None, dst_addr=None, proc_type=None):
        self.src_addr = src_addr
        self.dst_addr = dst_addr
        self.proc_type = proc_type

class EthHeader:
    def __init__(self, b):
        self.__b = b

    @property
    def source_addr(self):
        return self.__b[src_MAC:][:ETHERNET_ADDR_SIZE]

    @property
    def destination_addr(self):
        return self.__b[dst_MAC:][:ETHERNET_ADDR_SIZE]

    @property
    def protocol_type(self):
        return self.__b[eth_type:]

class Nic():

    def __init__(self, id, name, link_ep, demux, primary, endpoints):
        

def new_nic():