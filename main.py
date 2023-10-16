#!/usr/bin/env python

import itertools
import threading
import time
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import time
import subprocess
import optparse
import re

subprocess.call("clear")

logo = """


  __  __          _____    _____ _                                 
 |  \/  |   /\   / ____|  / ____| |                                
 | \  / |  /  \ | |      | |    | |__   __ _ _ __   __ _  ___ _ __ 
 | |\/| | / /\ \| |      | |    | '_ \ / _` | '_ \ / _` |/ _ \ '__|
 | |  | |/ ____ \ |____  | |____| | | | (_| | | | | (_| |  __/ |   
 |_|  |_/_/    \_\_____|  \_____|_| |_|\__,_|_| |_|\__, |\___|_|   
                                                    __/ |          
                                                   |___/           
"""




print(f"{Fore.GREEN}{logo}")
print(f"\n [+]-[+]-[+]-[+]-[+]-[+]-[+]-[+]-[+]-[+]-[+]-[+]-[+]-[+]-[+]-[+]-[+] *** Created by {Fore.RED}Totenkopf\n")

done = False
#here is the animation
def animate():

    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write("\r[+] Changing MAC address "  + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')




t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(7)
done = True


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address.")
    (options, arguments) = parser.parse_args()
    # print(arguments)
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    # elif options.interface != "eth0" or options.interface != "wlan0" or options.interface != "wlan1":
    #     print("Wrong interface given!")
    #     return

    return options



def change_mac(interface, new_mac):
    print(f"\n{Fore.LIGHTBLUE_EX}[+] Changing MAC address for " + interface + " to " + new_mac)
    time.sleep(7)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface,  "up"])




def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        pass


options = get_arguments()
current_mac = get_current_mac(options.interface)
print(f"\n\n[+] Current MAC: {Fore.LIGHTBLUE_EX}{str(current_mac)}")


change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print(f"\n[+] MAC address was successfully changed to: {Fore.GREEN}{current_mac}\n")
    print(f"\n\t{Fore.LIGHTBLACK_EX}#")
    print(f"\t{Fore.LIGHTGREEN_EX}#")
    print(f"\t{Fore.LIGHTMAGENTA_EX}#")
    print(f"\t{Fore.LIGHTYELLOW_EX}#")
    print(f"\t{Fore.LIGHTRED_EX}#")
    print(f"\t{Fore.LIGHTBLUE_EX}#")
    print(f"\t{Fore.LIGHTWHITE_EX}#\n")

else:
    print(f"\n{Fore.RED}[-] The chosen interface doesn't have a MAC address!")
    print(f"\n{Fore.RED}[-] MAC address did not get changed.\n")
    print(f"\n\t{Fore.LIGHTBLACK_EX}#")
    print(f"\t{Fore.LIGHTGREEN_EX}#")
    print(f"\t{Fore.LIGHTMAGENTA_EX}#")
    print(f"\t{Fore.LIGHTYELLOW_EX}#")
    print(f"\t{Fore.LIGHTRED_EX}#")
    print(f"\t{Fore.LIGHTBLUE_EX}#")
    print(f"\t{Fore.LIGHTWHITE_EX}#\n")

