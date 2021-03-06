import array
import os
from fcntl import ioctl
import fcntl
import struct
import uuid
import termios
import socket


TUNSETIFF =  0x400454ca
TUNSETOWNER = TUNSETIFF + 2
IFF_TUN   = 0x0001
IFF_TAP   = 0x0002
IFF_NO_PI = 0x1000

TUN = 1
TAP = 2

IPV4_PROTOCOL_NUMBER = 0x0800
IPV6_PROTOCOL_NUMBER = 0x86dd

# virtual network car config
class Config:
    def __init__(self, name=None, mode=None):
        self.name = name
        self.mode = mode


# return the config of virtual network
def new_net_dev(c: Config):
    if c.mode == TUN:
        fd = new_tun(c.name) 
    elif c.mode == TAP:
        fd = new_tap(c.name)
    else:
        raise "unsupport virtual network type"
    return fd

def new_tun(name):
    fd = os.open('/dev/net/tun', os.O_RDWR)
    # Tall it we want a TUN device named tun0.
    ifr = struct.pack('16sH', name.encode(), IFF_TUN | IFF_NO_PI)
    # fcntl.ioctl(tun, TUNSETIFF, ifr)
    # Optionally, we want it be accessed by the normal user.
    fcntl.ioctl(fd, TUNSETIFF, ifr)
    return fd

def new_tap(name):
    fd = os.open('/dev/net/tun', os.O_RDWR)
    ifr = struct.pack('16sH', name.encode(), IFF_TAP | IFF_NO_PI)
    ioctl(fd, TUNSETIFF, ifr)
    return fd

# make the netwrok card start
def set_link_up(name):

    out = os.system("ip link set {} up".format(name))
    return out

# add ip route
def set_route(name, ip):
    out = os.system("ip route add {} dev {}".format(ip, name).replace("'", ""))
    return out

# add ip address
def add_ip(name, ip):
    out = os.system("ip addr add {} dev {}".format(ip, name))
    return out

def get_hardware_addr(name):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', bytes(name, 'utf-8')[:15]))
    return ':'.join('%02x' % b for b in info[18:24])

if __name__ == '__main__':
    new_tap('tap0')