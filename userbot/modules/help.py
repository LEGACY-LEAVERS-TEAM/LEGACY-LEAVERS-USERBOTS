# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot help command"""

import asyncio
from userbot import CMD_HELP, DEFAULTUSER
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help_handler(event):
    """For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(f"#WRONG\n**PLUGIN** : `{args}` ❌ **\nPlease Type the Plugin Name Correctly.**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t💖  "
        await event.edit("⚡")
        await asyncio.sleep(2.5)
        await event.edit(f"**[⚡𝗟𝗲𝗴𝗮𝗰𝘆-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡](t.me/LEGACY_LEAVERS_UB_SUPPORT)**\n\n"
                         f"**◑» Bᴏᴛ ᴏꜰ {DEFAULTUSER}**\n**◑» Pʟᴜɢɪɴ : {len(modules)}**\n\n"
                         "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
                         f"╰►| {string} ◄─\n\n"
                         f"**License : [Raphielscape Public License 1.d](https://github.com/LEGACY-LEAVERS-TEAM/LEGACY-LEAVERS-USERBOTS/blob/Lynx-Userbot/LICENSE)**\n"
                         f"**Copyright © 2021 [Legacy-Userbot LLC Company](https://github.com/LEGACY-LEAVERS-TEAM/LEGACY-LEAVERS-USERBOTS/)**")
        await event.reply(f"\n**Example** : Type » `.help admin` for Admin Plugin Usage Information.")
        await asyncio.sleep(1000)
        await event.delete()
