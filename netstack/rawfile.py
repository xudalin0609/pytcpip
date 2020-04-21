import os

def read_block(fd):
    packet = list(os.read(fd, 2048))
    return packet
