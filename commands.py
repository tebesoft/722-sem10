from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

from handlers import OP_BUTTON_STATE


def start_command(update: Update, context: CallbackContext) -> int:
    kb = [
        ["Операции с R числами"],
        ["Операции с C числами"]
    ]

    reply_kb_markup = ReplyKeyboardMarkup(kb, one_time_keyboard=True)
    update.message.reply_text("Выберите действие", reply_markup=reply_kb_markup)

    return OP_BUTTON_STATE