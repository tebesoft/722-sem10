import logging

from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler

# Enable logging
from commands import start_command
from handlers import OP_BUTTON_STATE, op_select_handler, op_input_handler, OP_INPUT_STATE, NUM_A_STATE, NUM_B_STATE, \
    num_b_handler, num_a_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = ""



def main() -> None:
    """Start the bot."""

    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    # dispatcher.add_handler(CommandHandler("start", start))

    calc_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_command)],
        states={
            OP_BUTTON_STATE: [MessageHandler(Filters.regex(r"R|C"), op_select_handler)],
            OP_INPUT_STATE: [CallbackQueryHandler(op_input_handler)],
            NUM_A_STATE: [MessageHandler(Filters.text, num_a_handler)],
            NUM_B_STATE: [MessageHandler(Filters.text, num_b_handler)],
        },
        fallbacks=[]
    )

    dispatcher.add_handler(calc_conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()