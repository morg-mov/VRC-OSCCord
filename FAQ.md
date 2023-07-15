# FAQ/Troubleshooting

## *"I keep getting a warning on startup talking about a missing package!"*
This is safe to ignore. This was caused by a bug with the package compiler I use that didn't grab the Pycord version data properly. This was fixed in v2.1.1 and I would recommend [downloading the latest version of OSCCord](https://github.com/Morg-S9/VRC-OSCCord/releases).

## *"The `/setchannel` command isn't working!"*
There are two major reasons this usually happens.
- You forgot to give your bot slash command permissions when creating the invite link. **Kick the bot from your server and [re-follow the steps in the README pertaining to generating the invite link](https://github.com/Morg-S9/VRC-OSCCord/blob/main/README.md#2-create-an-invite-url).**
- You invited the bot to your server before running it for the first time. If you do this, it takes a while for the slash commands to register in your server. **Either wait an hour or kick and re-invite the bot to your server.** 

## *"The program is running but the text box in game isn't working!"*
This can happen for a number of reasons. Try these fixes in order.
- You may have launched OSCCord before opening VRChat, or restarted your game while OSCCord was connected. VRChat needs to be open when you launch OSCCord so that it can make a successful connection with VRChat's Internal OSC Server. **Close and re-open OSCCord.**
- Make sure VRChat OSC is turned on. **Open your action menu by holding down your menu button, go to `Options > OSC`, and turn on the `Enabled` toggle if it isn't already. Restart your game after enabling to make sure everything is set properly. MAKE SURE YOU RESTART OSCCORD WITH IT.**
- There could be a number of problems on Discord side:
    - You may have forgotten to set the channel the bot listens on. **Run `/setchannel` in the Discord Channel you wish for the bot to listen in on.**
    - The bot may not have sufficient permissions to see the channel you're trying to use. **Check your server permissions.**
    - You may have forgotten to select one of the required permissions while generating the invite link. **Kick the bot from your server and [re-follow the steps in the README pertaining to generating the invite link](https://github.com/Morg-S9/VRC-OSCCord/blob/main/README.md#2-create-an-invite-url).**
- Since the OSC Protocol is communicated over UDP, VRChat and/or OSCCord may be restricted by the firewall settings on your computer. **See [Allowing VRChat/OSCCord through your firewall](https://github.com/Morg-S9/VRC-OSCCord/blob/main/TROUBLESHOOTING.md#allowing-vrchatosccord-through-your-firewall).**

If all else fails, open a discussion thread detailing your issue, and I'll try your best to help you out.

