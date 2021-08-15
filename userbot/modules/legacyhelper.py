""" Userbot module for other small commands. """
from userbot import CMD_HELP, DEFAULTUSER
from userbot.events import register


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} 🐈 If You Don't Know The Command To Order Me,\nType:** `.help` Atau Bisa Minta Bantuan Ke\n"
        "\n📬**Developer :**"
        "\n[Telegram](t.me/LEGACY_LEAVERS_UB_SUPPORT)"
        "\n[Dev Repo](https://github.com/LEGACY-LEAVERS-TEAM/LEGACY-LEAVERS-USERBOTS)"
        


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**List of Vars For {DEFAULTUSER}:**\n"
        "\nClick » [ [Legacy-VARS](https://raw.githubusercontent.com/LEGACY-LEAVERS-TEAM/LEGACY-LEAVERS-USERBOTS/LEGACY-LEAVERS-USERBOTS/varshelper.txt) ] «")


CMD_HELP.update({
    "legacyhelper":
    "✘ Pʟᴜɢɪɴ : Legacy Helper\
\n\n⚡𝘾𝙈𝘿⚡: `.lhelp`\
\n↳ : Help For Users Legacy.\
\n\n⚡𝘾𝙈𝘿⚡: `.vars`\
\n↳ : View List of Vars Legacy-Userbot."
})
