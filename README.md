# OSCCord
Very simple little program for VRChat OSC, it takes the messages from a Discord Server (or servers) and outputs them to your chatbox.

![Program Demonstration](assets/readme-images/demo.gif)
##### Demonstrated by my good friend Envy!
<br>

## Instructions

### 1. Create a bot on Discord
Go to the [Discord Developer Portal](https://discord.com/developers) and login with your Discord account.

In the top right, click `New Application`.

![New Application button](assets/readme-images/new-app.png)

Give your bot a lovely name, agree to the lifeless corporation's contract to your life (Click the checkbox), then click `Create`.

Click `Bot` in the array of buttons on the left

![Bot side button](assets/readme-images/bot-button.png)

Feel free to give your bot a profile icon here.

Click `Reset Token` below the username box, then click `Copy`. Save your token somewhere safe.

![Reset Token button](assets/readme-images/reset-token.png)

![Copy button](assets/readme-images/copy-button.png)

Scroll down and click the switch next to `Message Content Intent` to enable it. This will allow your bot to read the content of your messages.

![Message Intent switch](assets/readme-images/message-intent.png)

Click `Save Changes`.

![Save Changes button](assets/readme-images/savechanges-button.png)

Click `OAuth2` then `URL Generator` in the array of buttons on the left.

![OAuth/URL Generator button](assets/readme-images/oauth-url.png)

Under `Scopes`, tick the `bot` and `applications.commands` scope.

![Bot Scope Tickbox](assets/readme-images/oauth2-scopes.png)

Another set of tickboxes should appear below. Under `Bot Permissions` and `General Permissions`, tick the following permissions:

```
Read Messages/View Channels
Send Messages
Use Slash Commands
```

At the very bottom of the page is your bot invite link. Keep this page open. We'll copy this to use later.

### 2. Setup and run the program

Download the latest release of OSCCord [here](https://github.com/Morg-S9/VRC-OSCCord/releases) and extract it somewhere where it won't get tangled in with all your other files (or [build it from source](#runningbuilding-from-source)).

Launch VRChat before running OSCCord.

With VRChat open, run OSCCord. It will prompt you for your Discord Token. Copy your token again if you need to, paste it into the console window, then press Enter. 

Return to the Discord Developer Portal. Click `Copy` to copy your bot invite link to your clipboard.

![Copy Link button](assets/readme-images/copy-url.png)

Paste it into your browser URL bar. Invite it to the server of your choosing.

Once done, run the `/setchannel` command in the channel you wish for the bot to listen in on.

Your bot should now be online and working! Happy playing!

## Running/Building from Source

1. Clone the repo
2. Run `python -m pip install -r requirements.txt`

From here, you can run the app by running `python OSCCord.py`. If you wish to build the program to use with an executable, you may do so by running `python setup.py build`.