import platform #
import subprocess #
import requests #
from datetime import datetime #
from sys import exit #
#
#
#
# Read me: 
# I've added comments everywhere to show you that I can only access your UUID and the time you opened it
# Like just look at the code, it only accesses your UUID and checks if its in the list.
# Also if you decided to spam this WebHook then props to you for being an asshole :D I have it muted anyways
#
#
buyers = [""] #
#
if platform.system() == "Windows": #
    uuid = subprocess.check_output("wmic csproduct get uuid").decode().split('\n')[1].strip() #
elif platform.system() == "Linux": #
    uuid = subprocess.check_output('cat /sys/class/dmi/id/product_uuid', shell=True).decode().strip() #
else: #
    print("[!] Unsupported platform!") #
    exit() #
#
if uuid not in buyers: #
    print("[!] You need to purchase Sky Advertiser first!") #
    input("[#] Press Enter to exit...") #
    exit() #
# 
data = { #
    "embeds": [ #
        { #
            "title": "UUID Check", #
            "description": f"UUID: {uuid}\n- Opened: {datetime.now()}", #
            "color": 0x7289DA #
        } #
    ] #
} #
#
if uuid: #
    response = requests.post("https://discord.com/api/webhooks/1320020511958499368/n_0h0AEuHYhuOoGQ4db93n4Wooru-wiJFN_ZTt4FIpbGCNRPCWwC9zD-r8MEQ2bYyIGQ", json=data) #
