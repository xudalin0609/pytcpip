import sys
sys.path.append('/root/codes/pytcpip')
from netstack.tuntap import *
from netstack.rawfile import *

def main():
    print('start')
    tap_name = "tap0"
    c = Config(tap_name, TAP)
    print('new net dev')
    fd = new_net_dev(c)
    print('start tap')
    # start tap network card
    set_link_up(tap_name)
    add_ip(tap_name, '192.168.1.1')
    while True:
        rn = read_block(fd)
        print('read {} bytes'.format(len(rn)))



if __name__ == '__main__':
    main()