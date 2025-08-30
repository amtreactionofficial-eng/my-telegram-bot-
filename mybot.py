from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = '8248149940:AAFhDNw5CCe_xCr9j5RyZW1gO91KPxIyZUQ'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("💰 ဈေးနှုန်းများ"), KeyboardButton("📦 ဝယ်ယူရန်")],
        [KeyboardButton("📱 ဆက်သွယ်ရန်"), KeyboardButton("ℹ️ အကြောင်းအရာ")],
        [KeyboardButton("🎥 VIP Channel"), KeyboardButton("🔞 Solo Videos")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        'ဟယ်လို! Hello မဂ်လာပါရှင့် ။\nအောက်က ခလုပ်တွေကို နှိပ်ပြီးသုံးလို့ရပါတယ်။',
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('မင်းကို ကူညီဖို့ ငါဒီမှာရှိနေတယ်ကွာ!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    if user_message == '💰 ဈေးနှုန်းများ':
        await update.message.reply_text('''𝟓 𝐦𝐢𝐧𝐬  _  𝟓𝟎𝟎𝟎𝐊𝐬

𝟏𝟎 𝐦𝐢𝐧𝐬 _ 𝟏𝟎𝟎𝟎𝟎𝐊𝐬

𝟏𝟓 𝐦𝐢𝐧𝐬     _  𝟏𝟓𝟎𝟎𝟎𝐊𝐬

သဲအပြီး _ 𝟐𝟓𝟎𝟎𝟎𝐊𝐬

လီးအတုလေးနဲ့ပက်လက်လှန်ထည့်ပြ/ဘေးစောင်းပြီးထည့်ပြ/အပေါ်ကနေမြင်းစီးပြ 𝟓 𝐦𝐢𝐧𝐬 𝟏𝟎𝟎𝟎𝟎𝐊𝐬

𝐕𝐢𝐩 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ရာသက်ပန်ကြေး ဖြင့်ဝင်လိုရပါသေးတယ် @thaethae883''')
    
    elif user_message == '📦 ဝယ်ယူရန်':
        await update.message.reply_text('ဝယ်ယူလိုပါက ဒီလင့်ကို နှိပ်ပါ - @thaethae883')
    
    elif user_message == '📱 ဆက်သွယ်ရန်':
        await update.message.reply_text('ဆက်သွယ်ရန် ဖုန်းနံပါတ် - Viber: 09686852188')
    
    elif user_message == 'ℹ️ အကြောင်းအရာ':
        await update.message.reply_text('ချက်မှာလား')
    
    elif user_message == '🎥 VIP Channel':
        await update.message.reply_text('VIP Channel ဝင်ရောက်ရန် - @thaethae883')
    
    elif user_message == '🔞 Solo Videos':
        await update.message.reply_text('အကြမ်းစားအသံပါ 𝐒𝐨𝐥𝐨 များဝယ်လိုရပါတယ်ရှ့်\n🇹🇭 ဖုန်းဘေးတိုဖြင့်ချက်နိုင်ပါတယ်')
    
    else:
        # Do nothing for other messages
        pass

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)
    
    print('Bot is polling...')
    app.run_polling(poll_interval=3)