from scapy.all import *
from scapy.layers.inet import ARP, Ether
import os
import requests as req
blue = '\033[94m'
green = '\033[32m'
red = '\033[91m'
w = '\033[0m'
os.system("cls")
print(red + "Scaning...")
ipp = ("192.168.1.")
for addr in range(255):
    ip = ipp + str(addr)
    ans = sr1(ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        arp_frame = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=ip)
        resp, unans = srp(arp_frame, verbose=0)
        for s, r in resp:
            macAdress = r[Ether].src
            resp = req.get("https://api.macvendors.com/{}".format(macAdress))
            vendor = resp.text
            print(green + "[*]" + ip + " " + macAdress + " " + vendor)
