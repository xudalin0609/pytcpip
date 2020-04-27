import sys
sys.path.append('/root/codes/pytcpip')
import argparse
import ipaddress

from netstack import tuntap
from netstack.tcpip.link.endpoint import new_link_endpoint, Options

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    parser.add_argument('--cidr')
    args = parser.parse_args()
    tap_name = args.name
    cidr_name = args.cidr

    net = (ipaddress.ip_network(cidr_name, strict=False))
    cidr = net.with_netmask
    # 解析ip地址
    if net.version == 4:
        proto = tuntap.IPV4_PROTOCOL_NUMBER
    elif net.version == 6:
        proto = tuntap.IPV6_PROTOCOL_NUMBER

    # 虚拟网卡配置
    conf = tuntap.Config(name=tap_name, mode=tuntap.TAP)
    fd = tuntap.new_net_dev(conf)
    tuntap.set_link_up(tap_name) # 启动tap网卡
    tuntap.set_route(tap_name, cidr) # 设置路由

    # 获取mac地址
    mac = tuntap.get_hardware_addr(tap_name)
    print('mac:::', mac)

    opts = Options(fd=fd, mtu=1500, address=mac)

    # 网卡文件接口
    link_id = new_link_endpoint(opts)

    s = 




if __name__ == '__main__':
    main()