import os
import sqlite3
import simplejson as json
import discord
from pythonosc import udp_client

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = discord.Bot(intents=intents)

print("\n{OSCCord}\nVersion 2.0.0\nWritten by morg.mov\nIdea by envypaw\n")

if not os.path.isfile("./config.json"):
    print("No config.json found.\n")
    while True:
        token = input("Enter your Discord Bot Token: ")
        if token:
            break
        print("No bot token provided.\n")
    config = {"token": token}
    print("Creating config.json...")
    try:
        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        print("Done.\n")
    except OSError as e:
        print(f"\nAn error occurred creating the file.\n{e}\n")
        input("Press [Enter] to exit...")
        exit(1)

if not os.path.isfile("./guilds.db"):
    print("Initializing Guilds Database...")
    try:
        conn = sqlite3.connect("./guilds.db")
        db = conn.cursor()
        db.execute(
            """ CREATE TABLE channels (
                guildID INT PRIMARY KEY NOT NULL,
                channelID INT NOT NULL
            ); """
        )
        conn.commit()
        db.close()
        conn.close()
        print("Done.\n")
    except (OSError, sqlite3.Error) as e:
        print(f"\nAn error occurred creating the database.\n{e}\n")
        input("Press [Enter] to exit...")
        exit(1)

print("Starting...")

with open("./config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

conn = sqlite3.connect("./guilds.db")
db = conn.cursor()

udpclient = udp_client.SimpleUDPClient("127.0.0.1", 9000)


def check(guildid, channelid):
    """
    Checks to see if the channel ID matches the one stored in the db by user.
    Returns true if match, returns false otherwise.
    """
    db.execute(f"SELECT channelID FROM channels WHERE guildID={int(guildid)};")
    response = db.fetchone()
    if response is None:
        return False
    elif response[0] == channelid:
        return True
    else:
        return False


@bot.slash_command()
async def setchannel(ctx):
    """Run this in the channel you want the bot to listen on."""
    db.execute(f"SELECT channelID FROM channels WHERE guildID = {int(ctx.guild_id)};")
    response = db.fetchone()
    if response is None:
        db.execute(
            f"INSERT INTO channels VALUES ({int(ctx.guild_id)},{int(ctx.channel_id)});"
        )
        conn.commit()
    else:
        db.execute(
            f"UPDATE channels SET channelID = {int(ctx.channel_id)} WHERE guildID = {int(ctx.guild_id)};"
        )
        conn.commit()

    await ctx.respond("Channel has been set.")


@bot.event
async def on_ready():
    print(f"[Py-Cord] Logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.guild is None or check(message.guild.id, message.channel.id):
        msg = f"{message.author.name}: {message.content}"
        print(f"[OSCCord] {msg}")
        udpclient.send_message("/chatbox/input", (msg, True))


bot.run(config["token"])
