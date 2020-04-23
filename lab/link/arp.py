import argparse
import ipaddress

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    parser.add_argument('--cidr')
    args = parser.parse_args()
    tap_name = args.name
    cidr_name = args.cidr

    net = (ipaddress.ip_network(cidr_name, strict=False))
    addr = net.network_address

    






if __name__ == '__main__':
    main()