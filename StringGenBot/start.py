from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""۞¦ اهلا بـك عزيـزي  {msg.from_user.mention}
۞¦ فـي بـوت اسـتـخـراج الـجـلـسـات
۞¦ يمكنك استخراج الجلسات الـتالية
۞¦ بايروجرام للحسابات & بايروجرام للبوتات
۞¦ بـايـروجـرام مـيوزك احـدث إصـدار 
۞¦ تيرمـكـس للحسابات & تيرمـكـس للبوتات

۞¦ بواسطـة : [ᕼᗩᗰO ᗩᒪᖇIᗴՏ](tg://user?id=5820956681) √""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="📥 ⍆ اضغط لبدا استخراج كود ⍅ 📥", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𝖲𝖮𝖴𝖱𝖢𝖤 𝖧𝖠𝖬𝖮", url="https://t.me/Y_U_U_9"),
                    InlineKeyboardButton("𝙳𝙴𝚅 𝙷𝙰𝙼𝙾", user_id=5820956681)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
