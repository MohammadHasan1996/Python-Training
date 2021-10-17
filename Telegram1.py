from telegram.ext import Updater,CommandHandler
token = Updater('1911623203:AAH355GYRCldQP5kyIFMRzmXyXpJ64aa-gk' , use_context=True)

def start (update , context):
    context.bot.send_message(text='سلام {} به ربات تلگرام من خوش آمدید.\n برای اطلاعات بیشتر روی /help کلیک کنید'.format(update.message.from_user.first_name),chat_id=update.message.chat_id)

def help(update,context):
    context.bot.send_message(text=''''شروع مجدد /start.
    نمایش وبسایت:/website
    نمایش یوزر نیم شما:/myuser
    چک ربات بودن یا نبودن:/check_me''', chat_id= update.message.chat_id)

def website(update,context):
    context.bot.send_message(text="techone24.com",chat_id = update.message.chat_id)

def myuser(update,context):
    context.bot.send_message(chat_id=update.message.chat_id,text="id:{},\nUser name:{},\nFirst name:{},\nLast name:{}".format(update.message.chat_id,update.from_user.username,update.from_user.first_name,update.from_user.last_name))

def check_me(update,context):
    if username[-3:] == "bot":
        context.bot.send_message(text="ROBOT-(BEEP BOOP)",chat_id=update.message.chat_id)

    else:
        context.bot.send_message(text="USER",chat_id=update.message.chat_id)





token.dispatcher.add_handler(CommandHandler('start',start))
token.dispatcher.add_handler(CommandHandler('help',help))
token.dispatcher.add_handler(CommandHandler('website',website))
token.dispatcher.add_handler(CommandHandler('myuser',myuser))
token.dispatcher.add_handler(CommandHandler('check_me',check_me))


token.start_polling()
token.idle()