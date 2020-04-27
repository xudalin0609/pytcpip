from netstack.tcpip.statck import registion

class Stack:

    def __init__(self, transport_protocols=None, 
                       network_protocols=None, 
                       link_addr_resolvers=None, 
                       demux=None, 
                       stats=None,
                       link_addr_cache=None,
                       mu=None,
                       nics=None,
                       forwarding=False,
                       route_table=None,
                       tcp_probe_func=None,
                       clock=None)

class TransportProtocolState:

    def __init__(self, proto=None, default_handler=None):
        self.proto=proto
        self.default_handler=default_handler



def new(network, transport, opts):
    s = Stack(
        transport_protocols={}
    )

    # 添加指定的网络层协议
    try:
        net_proto_fac = registion.network_protocols['name']
    except:
        net_proto = j
        s.network_protocols[net]
    
