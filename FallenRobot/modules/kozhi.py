import html
import random
import time
from FallenRobot import dispatcher
from FallenRobot.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler
from telegram.error import BadRequest
from telegram.ext import CallbackContext ,Filters,CommandHandler,run_async

KOYI_STRINGS = (
     "കുളക്കോഴി🐔 ", 
     "നാടൻ കോഴി🐔🐔 ", 
     "ഗിരിരാജൻ കോഴി 🐓🐓", 
     "🐔🐔കൂട്ടിൽ കയറു കോഴി ", 
     "🐓🐓പ്ഫാ കോഴി ",
     "🐔കോഴി സ്പോട്ടേഡ് 🐔",
     "🐔🐓ഇവിടെ രണ്ട് പൊരിച്ച കോഴി ",
     "🐓🐓ഉളുപ്പ് ഉണ്ടോ കോഴിയെ ",
     "🐔ഡാ മോനെ കോഴി അത് ലോക്കാ..ഇങ് പോര് ",
     "🐔🐔എന്താ കോഴിമോനെ ",
     "🐓🐓 എന്താടാ നോക്കുനെ കോഴിയെ."
     "😂വിധി പോലും വിറച്ചുപ്പോയി ഇവന്റെ കോഴിത്തരം കണ്ട് 🐓🐔🐓",
     " എടാ കോഴി നിനക്ക് ഇതുതന്നെ ആണോ പണി 🐓🤭",
     "😏നിന്റെ ഒകെ കോഴിത്തുക്കല്മുളക്കുന്ന കാലത്ത് നുമ്മ ഈ സീൻ വിട്ടതാ",
     "നീ കോഴി ആണോ അതോ കോഴി ആയി അഭിനയിക്കുവാണോ🤭🤣🤣🐓",
     
)

@run_async
def kozhi(update, context):
    # reply to correct message
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(KOYI_STRINGS))





__mod_name__ = "kozhi "

KOZHI_HANDLER = DisableAbleCommandHandler("kozhi", kozhi)

dispatcher.add_handler(KOZHI_HANDLER)
