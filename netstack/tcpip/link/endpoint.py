from netstack.tcpip.header.eth import ETHERNET_MINI_MUM_SIZE

BUF_CONFIG = [128, 256, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]

next_link_endpoint_id = 1


class Mutex:

    def __init__(self, state=None, sema=None):
        self.state = state
        self.sema = sema

class RWMutex:

    def __init__(self):
        self.w = Mutex()
        self.writer_sem = 0
        self.reader_sem = 0
        self.reader_count = 0
        self.reader_wait = 0

link_ep_mu = RWMutex()

class Capability:

    def __init__(self):
        self.check_sum_off_load = 1
        self.resolution_required = 2
        self.save_restore = 4
        self.disconnect_ok = 8
        self.loop_back = 16

capability = Capability()


class EndPoint:

    def __init__(self, fd, mtu, hdr_size,closed, addr, caps, handle_local, views, ioveces):
        self.fd = fd
        self.mtu = mtu
        self.hdr_size = hdr_size
        self.addr = addr
        self.caps = caps
        self.closed = closed
        self.handle_local = handle_local
        self.views = views
        self.ioveces = ioveces

class Options:

    def __init__(self, fd, mtu, address, close_func=None, resolution_required=False, save_restore=False, check_sum_off_load=False, disconnect_ok=False, handle_local=False, test_loss_packet=None):
        self.fd = fd
        self.mtu = mtu
        self.close_func = close_func
        self.address = address
        self.resolution_required = resolution_required
        self.save_restore = save_restore
        self.check_sum_off_load = check_sum_off_load
        self.disconnect_ok = disconnect_ok
        self.handle_local = handle_local
        self.test_loss_packet = test_loss_packet


def register_link_endpoint(link_end_point):
    global next_link_endpoint_id
    v = next_link_endpoint_id
    next_link_endpoint_id += 1
    link_end_point[v] = li




def new_link_endpoint(opts):
    fd = opts.fd
    caps = 0
    if opts.resolution_required:
        caps = capability.resolution_required
    elif opts.check_sum_off_load:
        caps = capability.check_sum_off_load
    elif opts.save_restore:
        caps = capability.save_restore
    elif opts.disconnect_ok:
        caps = capability.disconnect_ok

    e = EndPoint(fd=opts.fd, mtu=opts.mtu, caps=caps, closed=opts.close_func, addr=opts.address, hdr_size=ETHERNET_MINI_MUM_SIZE, views=[len(BUF_CONFIG)], ioveces=[len(BUF_CONFIG)], handle_local=opts.handle_local)
    
    return register_link_endpoint(e)