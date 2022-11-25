from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

(
    OP_BUTTON_STATE,  # 0
    NUM_A_STATE,      # 1 ...
    NUM_B_STATE,
    RESULT_STATE
) = range(4)  # [0, 1, 2, ..]

data = {
    "user_name": "",
    "num_a": 0,
    "num_b": 0,
    "op": "",           # +, -, *...
    "num_type": float
}

def op_select_handler(update: Update, context: CallbackContext) -> int:
    # сохранить с какими числами работаем (с вещественными или цилыми)
    text = update.message.text

    if "R" in text:
        data["num_type"] = float
    elif "C" in text:
        data["num_type"] = complex

    # Предложить пользователию выбрать действие InlineKeyboard
    kb = [
        [InlineKeyboardButton("a + b", callback_data="+")],
        [InlineKeyboardButton("a - b", callback_data="-")],
    ]
    reply_kb_markup = InlineKeyboardMarkup(kb)
    update.message.reply_text("Выберите операцию: ", reply_markup=reply_kb_markup)
    return NUM_A_STATE