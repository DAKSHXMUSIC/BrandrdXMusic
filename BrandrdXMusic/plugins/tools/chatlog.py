import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from BrandrdXMusic import app  

photo = [
    "https://te.legra.ph/file/6109aba28fa1e115fa05d.jpg",
    "https://te.legra.ph/file/8537b01a994ae3602ae74.jpg",
    "https://te.legra.ph/file/d06bf5d07189dee355821.jpg",
    "https://te.legra.ph/file/7da19e0084eb332c0396c.jpg",
    "https://te.legra.ph/file/3ee6851e13febb5a12ae7.jpg",
    "https://te.legra.ph/file/7e9799e874eee3ba8c1fc.jpg"
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"📝 Music Bot ADDED IN YOUR GROUP\n\n"
                f"───────────────────────────\n\n"
                f"😊 CHAT NAME: {message.chat.title}\n"
                
                f"🙃 Chat I'D: {message.chat.id}\n"
                
                f"🙂 Chat Username: @{message.chat.username}\n"
                
                f"🙂 CHAT link: [𝗖𝗟𝗜𝗖𝗞]({link})\n"
                
                f"🤔Group Member: {count}\n"
                
                f"🥲 ADDED BY: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"★ 𝗦𝗘𝗘 𝗚𝗥𝗢𝗨𝗣 ★", url=f"{link}")]
         ]))


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝗨𝗡𝗞𝗠𝗢𝗪𝗡 𝗨𝗦𝗘𝗥 "
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝗣𝗥𝗜𝗩𝗔𝗧𝗘 𝗖𝗛𝗔𝗧"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝗟𝗘𝗙𝗧 𝗚𝗥𝗢𝗨𝗣</u></b> ✫\n\𝗖𝗛𝗔𝗧 𝗧𝗜𝗧𝗟𝗘 : {title}\n\𝗖𝗛𝗔𝗧 𝗜𝗗  : {chat_id}\n\n𝗥𝗘𝗠𝗢𝗩𝗘𝗗 𝗕𝗬 : {remove_by}\n\nʙᴏᴛ: @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)

#welcome

@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"🙃 {member.id} WELCOME IN A NEW GROUP🥳\n\n"
                
                f"👀 Chat name: {message.chat.title}\n"
                
                f"🙂 Chat Username: @{message.chat.username}\n"
                
                f"😊 Your I'D: {member.id}\n"
                
                f"🤩 YOUR NAME: @{member.username}\n"
            
                f"👥 TOTAL {count} MEMBERS🎉"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"★ ADD ME IN YOUR GROUP ★", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))

#tagall
