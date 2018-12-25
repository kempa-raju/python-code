#!/usr/bin/env python

import subprocess
import optparse

# ori_Mac = "28:d2:44:72:98:9b"
def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface name for the MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="The MAC address")
    (options, argument) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface name, use --help for more info")
    elif not options.mac:
        parser,error("-] Please specify the mac adress, use --help for more info")
    return options

def change_mac(interfaceName, new_Mac):
    print("[+] changing the MAC address for " + interfaceName + " to " + new_Mac)
    subprocess.call(["ifconfig", interfaceName, "down"])
    subprocess.call(["ifconfig", interfaceName, "hw", "ether", new_Mac])
    subprocess.call(["ifconfig", interfaceName, "up"])
    subprocess.call(["ifconfig", interfaceName])


options = get_argument()
change_mac(options.interface, options.new_mac)


