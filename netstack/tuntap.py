import os
from fcntl import ioctl
import struct


TUNSETIFF = 0x400454ca
IFF_TUN   = 0x0001
IFF_NO_PI = 0x1000

TUN = 1
TAP = 2

# virtual network car config
class Config:
    name = None
    mode = int


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
    ftun = os.open("/dev/net/tun", os.O_RDWR) # linux中的一切本质上都是文件,这里生成了一个文件描述符
    return ioctl(ftun, TUNSETIFF, struct.pack("16sH", name.encode(), IFF_TUN | IFF_NO_PI))

def new_tap(name):
    ftap = os.ope
    return ioctl()


if __name__ == '__main__':
    print(new_tun('tun0'))