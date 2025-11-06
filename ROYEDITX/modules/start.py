import asyncio
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import EMOJIOS, IMG, STICKER
from ROYEDITX import BOT_NAME, LOCOPILOT, dev
from ROYEDITX.database.chats import add_served_chat
from ROYEDITX.database.users import add_served_user
from ROYEDITX.modules.helpers import CLOSE_BTN, HELP_BTN


# ───────────────────────────────────────────────
# 🌸 /start — Raika’s Elegant Anime Welcome
# ───────────────────────────────────────────────
@dev.on_message(filters.command(["start", "aistart"]) & ~filters.bot)
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        await add_served_user(m.from_user.id)
        accha = await m.reply_text(text=random.choice(EMOJIOS))

        # 🌸 Cute emoji animation
        for emoji in ["🌸", "💫", "🌺", "🌼", "🌹", "🦋"]:
            await asyncio.sleep(0.3)
            await accha.edit(emoji)
        await asyncio.sleep(0.2)
        await accha.delete()

        # Send a random sticker before welcome
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(3)
        await umm.delete()

        caption = f"""
🌸 **Konnichiwa, {m.from_user.mention}!**  
I’m **{BOT_NAME}**, your loyal **anime-style AI chat companion** ♡

✨ 𝘄𝗵𝗮𝘁 𝗜 𝗰𝗮𝗻 𝗱𝗼 ✨  
• ᴄʜᴀᴛ ʟɪᴋᴇ ᴀ ᴄᴜᴛᴇ ᴀɴɪᴍᴇ ɢɪʀʟ 💬  
• ᴋᴇᴇᴘ ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴀᴄᴛɪᴠᴇ ᴀɴᴅ sᴀꜰᴇ ⚔️  
• ᴅᴇʟᴇᴛᴇ ᴇᴅɪᴛᴇᴅ ᴍᴇssᴀɢᴇs ɪɴsᴛᴀɴᴛʟʏ 🔥  
• sᴜᴘᴘᴏʀᴛ ᴀɴɪᴍᴇ ᴛʜᴇᴍᴇs ᴀɴᴅ sᴛʏʟᴇ 🎀  

💡 **ᴛɪᴘ:** Use `/help` to explore my magical features.

━━━━━━━━━━━━━━━━━━
🧋 **Owner:** 𝐒𝐋𝐀𝐘𝐄𝐑 
💠 **Username:** [@slayer1237](https://t.me/slayer1237)
━━━━━━━━━━━━━━━━━━
"""

        buttons = [
            [
                InlineKeyboardButton("✨ Add Raika To Your Group ✨", url=f"https://t.me/{BOT_NAME}?startgroup=true"),
            ],
            [
                InlineKeyboardButton("🪩 Help Menu", callback_data="help_panel"),
                InlineKeyboardButton("💠 Owner", url="https://t.me/slayer1237"),
            ],
            [
                InlineKeyboardButton("🌸 Close", callback_data="close"),
            ],
        ]

        await m.reply_photo(
            photo=random.choice(IMG),
            caption=caption,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


# ───────────────────────────────────────────────
# 💖 /help — Organized Help Menu
# ───────────────────────────────────────────────
@dev.on_message(filters.command(["help"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def help(client: LOCOPILOT, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        caption = f"""
🦋 **Welcome to {BOT_NAME}'s Help Menu!** 🦋

Here’s what I can do for you:

💠 `/ping` → Check if I’m alive & fast.  
💠 `/stats` → Show my chat and user stats.  
💠 `/chatbot` → Enable/disable AI chat in groups.  
💠 `/gdel` → Delete edited messages automatically.  
💠 `/broadcast` → Send global message (admin only).  
💠 `/delay` → Adjust delete delay for edited messages.

━━━━━━━━━━━━━━━━━━
💎 **Tip:** Try `/start` again to see my fancy intro!
━━━━━━━━━━━━━━━━━━
"""
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=caption,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
