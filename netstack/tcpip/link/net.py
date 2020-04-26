import ipaddress

def parse_cidr(cidr_name):
    net = ipaddress.ip_network(cidr_name, strict=False)
    
    cidr = net.hostmask
    return ip, cidr