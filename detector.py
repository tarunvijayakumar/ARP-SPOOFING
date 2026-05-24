from scapy.all import sniff, ARP
import time

mac_ip_map = {}

def detect_arp(pkt):
    if pkt.haslayer(ARP):
        ip = pkt[ARP].psrc
        mac = pkt[ARP].hwsrc
        if ip in mac_ip_map and mac_ip_map[ip] != mac:
            print(f"ALERT: ARP anomaly for IP {ip} (MACs: {mac_ip_map[ip]} -> {mac})")
            # Optionally send Gratuitous ARP to restore mapping
        mac_ip_map[ip] = mac

if __name__ == "__main__":
    print("Monitoring ARP packets...")
    sniff(filter="arp", prn=detect_arp, store=0)
