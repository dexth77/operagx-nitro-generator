import requests
import uuid
import json
import os
from colorama import Fore, Back, Style

os.system('cls' if os.name == 'nt' else 'clear')

req_url = "https://api.discord.gx.games/v1/direct-fulfillment"

data = {
    "partnerUserId": str(uuid.uuid4()),
}

def geturl():
    r = requests.post(req_url, json=data)
    token = r.json()["token"]
    url = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
    return url, r.status_code


print(f"""
      {Fore.RED}
      
                                █▄░█ █ ▀█▀ █▀█ █▀█   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
                                █░▀█ █ ░█░ █▀▄ █▄█   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄ {Fore.MAGENTA}
                                \n
                                                          v1.0
                                                     Made by: dexth
                                             Opera GX Exploit Nitro Generator
""")

print(Fore.RESET)

nitro_count = int(input(f"[{Fore.BLUE}?{Fore.RESET}] {Fore.CYAN} How many nitro codes do you want to generate?{Fore.RESET} "))
output_path = input(f"[{Fore.BLUE}?{Fore.RESET}] {Fore.CYAN} Enter file name to save urls to (e.g:. urls.txt):{Fore.RESET} ")

print("\n")

was_broken = False

for i in range(nitro_count):
    url, status_code = geturl()
    if status_code == 200:
        print(f"[{Fore.GREEN}+{Fore.RESET}] {Fore.GREEN} {i+1}. Successfully generated nitro code!{Fore.RESET}")
        with open(output_path, "a") as f:
            f.write(f"{url}\n")
    else:
        print(f"[{Fore.RED}-{Fore.RESET}] {Fore.RED} Failed to generate, error code: {Fore.RESET}{status_code}{Fore.RESET}")
        was_broken = True
        break

print("\n")

if not was_broken:
    print(f"[{Fore.BLUE}?{Fore.RESET}] {Fore.CYAN} Generated {nitro_count} urls, saved to: {output_path}{Fore.RESET}")