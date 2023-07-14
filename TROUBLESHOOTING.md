# Guides and Troubleshooting
## Allowing VRChat/OSCCord through your firewall
Your computer's firewall may be blocking OSCCord's Connection and/or VRChat's ability to recieve connections.

The OSC Protocol is communicated over UDP on port 9000. This will detail how to allow VRChat and OSCCord to communicate on that port through Windows Firewall.

**THIS GUIDE DOES NOT DETAIL ON PROPRIETARY FIREWALL SOFTWARE, ONLY THE ONE INCLUDED WITH WINDOWS. YOU'RE ON YOUR OWN WITH THAT.**

Press `Windows Key + R` on your keyboard to open your system run dialog. Type `wf.msc` and press enter or click `OK`.

![Windows Run Dialog](assets/readme-images/windows-firewall/run.png)

A window will open containing your firewall overview. On the left side, click `Inbound Rules`.

![Inbound Rules Button](assets/readme-images/windows-firewall/inbound-rules.png)

On the right side, click `New Rule...`

![New Rule button for Inbound Rules](assets/readme-images/windows-firewall/new-rule-inbound.png)

A new window will open called the `New Inbound Rule Wizard`. Click the `Custom` option out of the provided list, then click `Next`.

![New Rule Wizard for Inbound Rules](assets/readme-images/windows-firewall/inbound-wizard-start.png)

Select `This program path:` out of the list and click `Browse...`. Find your VRChat Executable and select it. Then, click `Next`.

If you're having trouble locating your install, these are the most common locations for the most common platforms:
- Steam: `C:\Program Files (x86)\Steam\steamapps\common\VRChat\VRChat.exe`
- Oculus Rift/Quest Link: `C:\Program Files\Oculus\Software\Software\vrchat-vrchat\VRChat.exe`

![Inbound Wizard Program Select](assets/readme-images/windows-firewall/inbound-wizard-program.png)

![Browse Dialog](assets/readme-images/windows-firewall/inbound-program-browse.png)

On this next prompt, set each option to the same ones shown in the screenshot below, then click `Next`.

![Port/Protocol definition screen](assets/readme-images/windows-firewall/inbound-ports.png)

Click `Next` again, this prompt is already set properly.

![Scope Prompt](assets/readme-images/windows-firewall/inbound-scope.png)

If not selected already, click `Allow the connection` from the list of given options, then click `Next`.

![Inbound Action Prompt](assets/readme-images/windows-firewall/inbound-action.png)

Depending on what your local network setting is set to, either tick `Private` or `Public`.

*(If you don't know, just tick both. If they're both already ticked, just leave it.)*

Click `Next`.

![Profile Prompt](assets/readme-images/windows-firewall/inbound-profile.png)

Name this profile `VRChat OSC Inbound`, and click `Finish`.

![Name Prompt](assets/readme-images/windows-firewall/inbound-name.png)

You may also need to allow OSCCord through your firewall.

On the left of the window again, click `Outbound Rules`

![Outbound Rules button](assets/readme-images/windows-firewall/outbound-rules.png)

and follow these instructions exactly as last time, except for two things:

- Set the target program to OSCCord instead of VRChat.
![Outbound Program](assets/readme-images/windows-firewall/outbound-program.png)

- Name the rule `OSCCord Outbound`.
![Outbound Name](assets/readme-images/windows-firewall/outbound-name.png)