import logging
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler,filters
from chatgpt_translator import translate

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
with open("./credentials.json","r") as f:
    data = json.load(f)
    token = data["telegram_token"]
with open("./users_info.json","r") as f:
    users_dict = json.load(f)
    

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.username
    if user_name in users_dict:
        user = users_dict[user_name]
        text = translate(update.effective_message.text,user["language"],user["gender"])        
        message_id = update.effective_message.id
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_to_message_id=message_id)
    
if __name__ == '__main__':

    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    application.run_polling()