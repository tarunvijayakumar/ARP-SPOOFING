    import subprocess

def block_mac(mac):
    subprocess.run(['iptables', '-A', 'INPUT', '-m', 'mac', '--mac-source', mac, '-j', 'DROP'])

def auto_configure_static_arp(ip, mac):
    subprocess.run(['arp', '-s', ip, mac])
