#!/user/bin/env python

import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Select interface you want to change")
    parser.add_option("-m", "--mac", dest="new_mac", help="Mac Address selected by user")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface, use --help for more info")#code to handle error
    elif not options.new_mac:
        parser.error("Please specify a new mac, use --help for more info")#code to handle error
    return options

def mac_changer(interface, new_mac):
    print("[+] Changing MAC address for " + interface + "to" + new_mac)
    subprocess.call(["ifconfig", interface, "down", ])
    subprocess.call(["ifconfig", interface, "up", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up", ])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_result:
        return mac_address_result.group(0)
    else:
        print("Could not read MAC address")


options = get_args()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
mac_changer(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("MAC address was successfully changed to " + current_mac)
else:
    print("Couldn't change MAC!")



