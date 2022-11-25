
(
    OP_BUTTON_STATE,  # 0
    NUM_A_STATE,      # 1 ...
    NUM_B_STATE,
    RESULT_STATE
) = range(4)  # [0, 1, 2, ..]


def op_select_handler(update: Update, context: CallbackContext) -> int:
    # сохранить с какими числами работаем (с вещественными или цилыми)
    # Предложить пользователию выбрать действие InlineKeyboard

    return NUM_A_STATE