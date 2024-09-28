
"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.constants import ParseMode, ChatType

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

turl = "https://t.me/shadeienbot/bigdream"
url = "https://s3.us-west-2.amazonaws.com/tma-front-dev.cudis.xyz/beanbit/index.html"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # print(str(update))
    
    message = update.message
    member = message.from_user
    chat_id = message.chat.id
    
    print(message.chat.type)
    if message.chat.type != ChatType.PRIVATE :
        reply_markup = InlineKeyboardMarkup.from_button(InlineKeyboardButton("start game", url=turl))
        await context.bot.send_message(
            chat_id=chat_id, text="hello, "+member.first_name, reply_markup=reply_markup, disable_notification=True
        )
    else :
        print("web_app")
        reply_markup = InlineKeyboardMarkup.from_button(InlineKeyboardButton("start game", web_app=WebAppInfo(url=url)))
        await update.message.reply_text("start", reply_markup=reply_markup)
        


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    # print(str(update))
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    # await context.bot.send_message(
    #     chat_id=chat_id, text="hello, "+member.first_name, reply_markup=reply_markup, disable_notification=True
    # )

    # await query.edit_message_text(text=f"Selected option: {query.data}")


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    # print(str(update))

    post = update.channel_post
    message = post.text
    chat_id = post.chat.id
    # print(message.text)

    # await update.message.reply_text(chat_id+":::"+message.text)
    await context.bot.send_message(
        chat_id=chat_id, text=message, parse_mode=ParseMode.HTML
    )

async def message_handler2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    # print(str(update))
    message = update.message
    chat_id = message.chat.id
    # print(message.text)


    await context.bot.send_message(
        chat_id=chat_id, text=message.text, parse_mode=ParseMode.HTML
    )

async def message_handler3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    message = update.message
    members = message.new_chat_members
    chat_id = message.chat.id

    names = ""
    for member in members:
        names += member.first_name + ","

    reply_markup = InlineKeyboardMarkup.from_button(InlineKeyboardButton("start game", url=turl))

    await context.bot.send_message(
        chat_id=chat_id, text="hello, "+names, reply_markup=reply_markup
    )

def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.7360876811:AAEZ1202AxhdUs-cxzuUvS09pu0SoNHDE-g
    # application = Application.builder().token("7741809313:AAEaAWpy1P_OBPqyLNHrUsoRjbfoPOV8F64").build()
    application = Application.builder().token("7360876811:AAEZ1202AxhdUs-cxzuUvS09pu0SoNHDE-g").build()

    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CallbackQueryHandler(button))
    # application.add_handler(CommandHandler("help", help))
    # application.add_handler(CallbackQueryHandler(button))

    # application.add_handler(MessageHandler(filters.TEXT & filters.ChatType.CHANNEL, message_handler))
    # application.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, message_handler2))
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS & filters.ChatType.GROUPS, message_handler3))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()