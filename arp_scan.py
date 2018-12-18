#!/usr/bin/env python
#ARP Scanner

import scapy.all as scapy
import pprint

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=0)[0]
	
	print("IP\t\t\t\tMAC Address\n---------------------------------------------------------------------")
	for element in answered_list:
		print(element[1].psrc+"\t\t\t"+element[1].hwsrc)

ip_input = raw_input("ENTER THE NETWORK YOU WISH TO ARP SCAN: ")

scan(ip_input)
 
