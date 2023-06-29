# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, invalid-name
import os
import simplejson as json
import discord
from pythonosc import udp_client

print("\n{OSCCord}\nVersion 1.0.0\nWritten by morg.mov\nIdea by envypaw\n")

if not os.path.isfile("./config.json"):
    print("No config.json found.\n")
    while True:
        token = input("Enter your Discord Bot Token: ")
        if token:
            break
        print("No bot token provided.\n")
    config = {
        "token": token
    }
    print("Creating config.json...")
    try:
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"\nAn error occurred creating the file.\n{e}")
        exit(1)

with open("./config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

udpclient = udp_client.SimpleUDPClient("127.0.0.1", 9000)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"[discord.py] Logged on as {self.user}!")

    async def on_message(self, message):
        a = f"{message.author}: {message.content}"
        print(f"[OSCCord] {a}")
        udpclient.send_message("/chatbox/input", (a, True))


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = MyClient(intents=intents)
client.run(config["token"])
