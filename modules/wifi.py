from scapy.all import *

paquets = sniff(
    iface="en0",
    count=100,
    timeout=None,
    filter="udp"
    
)
ip = set()

for paquet in paquets:
    if paquet.haslayer(IP):
        ip.add(paquet[IP].src)
print(ip)
    