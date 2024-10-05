import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Получаем токен от BotFather
TOKEN = '7752030735:AAEbucqMMSZwqSnj-9F8MZrzJNbYc-0oWdw'  # Замените YOUR_BOT_TOKEN на свой токен

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение при команде /start."""
    await update.message.reply_text('Привет! Добро пожаловать в PIG Clicker! Нажмите на ссылку ниже, чтобы начать играть:')
    await update.message.reply_text('https://geleb33.github.io')  # Замените на свой адрес

async def main() -> None:
    """Запускает бота."""
    app = ApplicationBuilder().token(TOKEN).build()

    # На команду /start отвечает функцией start
    app.add_handler(CommandHandler("start", start))

    # Запускаем бота
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
