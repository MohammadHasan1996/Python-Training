from telegram.ext import Updater , CommandHandler , MessageHandler , CallbackQueryHandler
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
import datetime
import random

token = Updater("1911623203:AAH355GYRCldQP5kyIFMRzmXyXpJ64aa-gk", use_context = True)

def start(update, context):
    Start_Keys = [[InlineKeyboardButton('شروع به کار',callback_data ='1')]]
    Start_Keys1 = InlineKeyboardMarkup(Start_Keys)
    context.bot.sendChatAction(update.message.chat_id, "typing")
    context.bot.send_Message(text="سلام{} به ربات من خوش آمدید.\n برای اطلاعات بیشتر به /help مراحعه کنید".format(update.from_user.first_name), chat_id=update.message.chat_id, reply_markup= Start_Keys1)


def buttons(update,context):
    Options = [[InlineKeyboardButton('نمایش تصویر', callback_data='2')],
               [InlineKeyboardButton('اطلاعات من', callback_data='3')],
               [InlineKeyboardButton('مکان نما', callback_data='4')],
               [InlineKeyboardButton('تاریخ و زمان', callback_data='5')]]
    Options1 = InlineKeyboardMarkup(Options)
    context.bot.send_message(chat_id=update.message.chat_id, text='انتخاب نمایید.', reply_markup=Options1)

    query = update.callback_query
    if query.data == '2':
        photo_1 = open("dog.jpg",'rb')
        photo_2 = open("cat.jpg",'rb')
        photo_3 = open("tiger.jpg",'rb')
        PIC = random.choice(photo_1,photo_2,photo_3)
        context.bot.sendChatAction(update.message.chat_id, "upload_photo")
        Context.bot.sendPhoto(query.message.chat_id,PIC)

    elif query.data == '3':
        context.bot.sendChatAction(update.message.chat_id, "typing")
        context.bot.send_Message(text = '''id:{}\n username:{}\nfirstname:{}\n lastname:{}'''.format(update.message.chat_id,update.message.from_user.username,update.message.from_user.first_name,update.message.from_user.last_name),chat_id = update.message.chat_id)

    elif query.data == '4':
        chat_id =  update.message.chat_id
        context.bot.sendChatAction(update.message.chat_id, "typing")
        context.bot.sendLocation(chat_id,"35.7261","51.3304")

    elif query.data == '5':
        NOW = datetime.datetime.now
        context.bot.sendChatAction(update.message.chat_id, "typing")
        context.bot.send_Message(text = NOW , chat_id = update.message.chat_id)

def help(update , context):
    context.bot.send_Message(text = '''شروع ربات:/start''')




token.dispatcher.add_handler(CommandHandler('start' , start))
token.dispatcher.add_handler(CallbackQueryHandler(buttons))

token.start_polling()
token.idle()

