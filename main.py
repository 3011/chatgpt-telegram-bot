"""===== Config ====="""
bot_token = ""  # 机器人的token
allowed_users = []  # 用户ID列表，建议个人使用
message_update_time = 1.5  # seconds 消息更新间隔

chatgpt_api_url = ""  # Optional 可选


"""===== ChatGPT ====="""
from revChatGPT.V1 import Chatbot

bot = Chatbot(config={"access_token": ""}, base_url=chatgpt_api_url)


def set_access_token(access_token):
    bot.set_access_token(access_token)


def reset_chat():
    bot.reset_chat()


def get_reply_stream(prompt):
    prev_text = ""
    for data in bot.ask(prompt):
        prev_text = data["message"]
        yield False, prev_text
    yield True, prev_text


"""===== Bot ====="""
import time
import logging
from telegram import (
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)
from telegram.constants import ParseMode

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def reset_reply(reply_message):
    reset_chat()
    await reply_message(text="An error occurred.\nConversation has been reset.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in allowed_users:
        await update.message.reply_text(text="You are not allowed to use this bot.")
        return

    if need_set_access_token:
        await update.message.reply_text(text="Please set access token first.")
        return

    reset_chat()
    await reset_reply(update.message.reply_text)


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in allowed_users:
        await update.message.reply_text(text="You are not allowed to use this bot.")
        return

    if need_set_access_token:
        await update.message.reply_text(text="Please set access token first.")
        return

    message = update.message.text
    reply_message = await update.message.reply_text(text="ChatGPT is typing...")

    try:
        prev_time = time.time()
        prev_reply_text = ""
        for is_done, reply_text in get_reply_stream(message):
            if is_done:
                try:
                    if prev_reply_text != reply_text:
                        await reply_message.edit_text(
                            text=reply_text,
                            parse_mode=ParseMode.MARKDOWN,
                        )
                except:
                    try:
                        await reply_message.edit_text(
                            text="[Default ParseMode]\n" + reply_text,
                        )
                    except:
                        await reset_reply(reply_message.edit_text)

            else:
                if time.time() - prev_time > message_update_time and reply_text:
                    prev_time = time.time()
                    try:
                        await reply_message.edit_text(
                            text=reply_text,
                        )
                        prev_reply_text = reply_text
                    except:
                        await reset_reply(reply_message.edit_text)
    except:
        await reset_reply(reply_message.edit_text)


async def set_access_token(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in allowed_users:
        await update.message.reply_text(text="You are not allowed to use this bot.")
        return

    try:
        access_token = update.message.text.split(" ")[1]
        set_access_token(access_token)
        global need_set_access_token
        need_set_access_token = False
        await update.message.reply_text(text="Access token set.")
    except:
        await update.message.reply_text(text="Access token set failed.")


if __name__ == "__main__":
    application = ApplicationBuilder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("set_access_token", set_access_token))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    application.run_polling()
