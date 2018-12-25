#!/usr/bin/env python

import subprocess
import optparse
import re
# ori_Mac = "28:d2:44:72:98:9b"

#Parse the input arguments.
def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface name for the MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="The MAC address")
    (options, argument) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface name, use --help for more info")
    elif not options.new_mac:
        parser,error("-] Please specify the mac adress, use --help for more info")
    return options

def change_mac(interfaceName, new_Mac):
    print("[+] changing the MAC address for " + interfaceName + " to " + new_Mac)
    subprocess.call(["ifconfig", interfaceName, "down"])
    subprocess.call(["ifconfig", interfaceName, "hw", "ether", new_Mac])
    subprocess.call(["ifconfig", interfaceName, "up"])

def get_currentMac(interface):
    result_str = subprocess.check_output(["ifconfig", interface])
    regexp_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result_str))
    if regexp_mac:
        return regexp_mac.group(0)
    else:
        print("[-] MAc address not present for this interface " + interface)


options = get_argument()

current_mac = get_currentMac(options.interface)
print("[+] current MAC is", current_mac)

if current_mac:
    change_mac(options.interface, options.new_mac)

if options.new_mac == get_currentMac(options.interface):
    print("[+] MAC address successfully changed to " + options.new_mac)
else:
    print("[-] Failed to change the mac address")


