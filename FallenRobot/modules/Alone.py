import html
import random
import time
from FallenRobot import dispatcher
from FallenRobot.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler
from telegram.error import BadRequest
from telegram.ext import CallbackContext ,run_async,Filters,CommandHandler




AFW_STRINGS = (
    "ഒരു കവിത കൂടി ഞാൻ എഴുതി വക്കാം എന്റെ കനവിൽ നീ.....എത്തുമ്പോൾ ഓമനിക്കാൻ....",
    "അറിയില്ല നീ ആരാണെന്നു. എവിടെയാണെന്ന്... നിന്റെ പേരെന്താണെന്നു .. ഒരുനാൾ എന്റെ പേരെഴുതിയ മോതിരം നിന്റെ കൈകളിൽ അണിയുന്നതും സ്വപ്നം കണ്ട് ഇന്നും ഞാൻ ഏകനായ്.....",
    "ജീവിതത്തിൽ ഞാൻ ഏറെ ഇഷ്ട്ടപ്പെടുന്നത് സ്വപ്നം കാണാനാണ്....കാരണം, അവിടെയാണ് ഞാൻ സ്നേഹിക്കുന്നവർ എന്റെ കൂടെയുളളത്..*.",
    "മഞ്ഞുതുള്ളിക്കായ്...എഴുതിയ ഒരു വരിയെക്കാൾ പ്രണയം തുളുമ്പുന്ന നൂറുവരികളുണ്ട് മനസ്സിൽ, നിന്നെക്കുറിച്ചു ഓർക്കുമ്പോൾ..",
    "നമുക്ക്‌ വേണ്ടി ഒന്നും ചെയ്യാനായില്ലെങ്കിലും നമ്മളെ സന്തോഷിപ്പിക്കാൻ സ്നേഹിക്കുന്നവർ ചെയ്യുന്ന ശ്രമങ്ങൾ മാത്രം മതി, മനസ്സ്‌ നിറയാൻ. അതൊരു വാക്കിലൂടെയാണെങ്കിൽ പോലും...",
    "കേന്ദ്രം കേരളത്തോട് കാണിക്കുന്നതാണ് പലപ്പോഴുംനീ എന്നോടും കാണിക്കാറ്...അതെന്നെ വേദനിപ്പിക്കുന്നുണ്ടെന്ന് ഇനിയെങ്കിലും നീ മനസ്സിലാക്കണം..",
    "ഇഷ്ട്പെട്ടത് നഷ്ടപ്പെടാതിരിക്കാൻ ഒരു പാട് കഷ്ടപ്പെടേണ്ടി വരും... !കഷ്ടപ്പെടാൻ ബുദ്ദിമുട്ടാണെൽ ചുമ്മാ കേറി കാണുന്നതൊന്നും ഇഷ്ട്പെടാൻ നിൽക്കരുത്.",
    "ജീവിതത്തിൽ നിന്നും ആരെയെങ്കിലും അകറ്റി നിർത്തിയിട്ടുണ്ടെങ്കിൽ അത് സ്നേഹക്കുറവ് കൊണ്ടല്ല, സ്നേഹക്കൂടുതൽ കൊണ്ടാണന്ന് മനസ്സിലാക്കുന്ന നിമിഷം ബന്ധങ്ങൾക്ക് ശക്തി കൂടും..",
    "ആരെയും വിഷമിപ്പിക്കാതെ ചിരിച്ചുകൊണ്ട് ജീവിക്കണം, ഉള്ളിൽ കരഞ്ഞിട്ടാണെങ്കിലും... സ്നേഹിക്കുന്നവരുടെ നിറഞ്ഞ കണ്ണുകളിൽ നോക്കി ചിരിച്ചുകൊണ്ട് മരിക്കണം.",
    "എനിക് സ്നേഹം വേണം. അത് പ്രകടമായി തന്നെ കിട്ടണം. ഉള്ളിൽ സ്നേഹം ഉണ്ട് പക്ഷേ, പ്രകടിപ്പിക്കാനാവില്ല എന്നതിൽ ഞാൻ വിശ്വസിക്കുന്നില്ല..ശവകുടിരത്തിൽ വന്ന് പുവിട്ടാൽ ഞാനറിയുമോ.?.",
    "മിഴിയു൦ മനസ്സു൦ നിറയ്ക്കാ൯നിനക്കേ കഴിയൂപ്രണയമേ....",
    "നീ കാറ്റും ഞാൻ കടലുമായിരുന്നു.തിരകളെ തലോടിയകലും നിനക്ക് പുറകെ ഓടിയെത്തി തീരത്ത് തലതല്ലി ചത്തുപോയ എൻ മോഹങ്ങൾ.",
    "കിട്ടില്ല എന്നറിഞ്ഞിട്ടും പിന്നെയും അവളെ പ്രണയിക്കുന്നതിലൊരു സുഖമുണ്ട്. മുറ്റത്തെ വെള്ളക്കെട്ടില്‍ തെളിഞ്ഞ അമ്പിളിമാമനെ കോരിയെടുക്കാന്‍ ശ്രമിക്കുന്ന കുട്ടിക്കാലത്തിന്‍റെ സുഖം..",
    "കാണാം കിനാവിന്റെ മധുരിക്കും ഓർമയിൽ നിന്നെ ഓർത്തു അകലെ വേദനിക്കുന്ന മനസ്സോടെ കണ്ണുനീരോടെ നമ്മൊളൊരുമിച്ചുള്ള നിമിഷങ്ങൾക്ക് വേണ്ടി കാത്തു നിൽക്കുകയാണ്.",
    "അറിയില്ല നീ ആരാണെന്നു. എവിടെയാണെന്ന്... നിന്റെ പേരെന്താണെന്നു .. ഒരുനാൾ എന്റെ പേരെഴുതിയ മോതിരം നിന്റെ കൈകളിൽ അണിയുന്നതും സ്വപ്നം കണ്ട് ഇന്നും ഞാൻ ഏകനായ്...",
    "മണ്ണായ് പടച്ച എന്നെ മണ്ണിലേക്ക് തിരികെ... വിളിക്കും മുന്‍പ് മണ്ണാല്‍ പടച്ച നിന്റെ കൂടെ ഒന്ന് ജീവിക്കണം...അതിനു വേണ്ടിയാണ് ഇന്നെന്‍ കാത്തിരിപ്പ്..",
    "ആഗ്രഹിച്ചത് കിട്ടണമെന്നില് ലആർഹമില്ലാത്തത് ആഗ്രഹിക്കുകയും അരുത്അതിനു വേണ്ടി വെമ്പൽ കൊള്ളുകയും അരുത്അങ്ങനെ ചെയുമ്പോൾകാലത്തിന്റെ വീഥിയിൽ തിരായടിച്ചു മായിച്ചാനൊമ്പരം മാത്രം മിച്ചം!!!.",
    "ദുഃഖത്തിന്റെ ത്രിവ്രതാ അറിയുന്നവർ പ്രണയിക്കില്ല മറിച്ചാണ് എങ്കിലോ പ്രീണയിച്ചവൻ ദുഃഖികയാതെയും ഇരുന്നിട്ടില്ല.",
    "സങ്കടങ്ങള്‍ വാനോളമുണ്ട്. കരഞ്ഞിട്ടുണ്ട്പക്ഷെ അരുടെയും മുന്നില്‍ കരയാന്‍ എനിക്കറിയില്ല.. കുഞ്ഞുനാള്‍ മുതല്‍ ചിരിച്ചാണ് ശീലിച്ചത്...അത് മാറ്റാനും കഴിയില്ല",
    "കൂടെ നടക്കുന്നവരല്ല കൂട്ടുകാർ... കൂട്ടത്തിൽ ഒരു തന്റെ പ്രശ്നത്തിൽ കൂടെ നിൽക്കുന്നവനാണ് യഥാർത്ഥ കൂട്ടുകാരൻ....",
    "അകലും നേരം ഒഴുകി പോകുന്ന കണ്ണുനീർ തുള്ളികളുടെ വില അറിയുന്നത് ഹൃദയത്തിൽ സൂക്ഷിച്ച സുഹൃത്ത് ബന്ധങ്ങൾ നഷ്ട്ടപെടുമ്പോൾ ആണ്.",
    "വിജയങ്ങളിൽ അഹങ്കാരമില്ല അഹങ്കാരം കാണിക്കാൻ ഞാൻ രാജാവല്ല പക്ഷെ വരവ് രാജകിയമായിരിക്കും.",
    "നിന്നെ കാണാതിരിക്കാൻ എന്റെ കണ്ണുകൾക്കാവില് സേനഹിക്കാതിരിക്കാൻ എന്റെ മനസ്സിനും",
    "തണുത്ത ഈ സന്ധ്യയിൽ ഞാന് തനിച്ചായി എന്നൊരു തോന്നൽ . . . . തനിച്ച് അല്ല എന്ന് അറിയിച്ചുകൊണ്ട് എനിക്കുവേണ്ടി പെയ്യുകയാണ് എന്റെ സ്വന്തം മഴ.",
    "ഞാൻ നിന്നെ എന്റെ ജീവനായി കണ്ടു പോയി പെണ്ണേ .......ഇനി അത് മാറണമെങ്കിൽ എന്റെ ഈ ജീവൻ പോകണം....",
    "തിരിച്ചു കിട്ടാത്ത സ്നേഹത്തിനു പിറകേ... അലയുന്നത് മരണത്തിനു തുല്യമാണെന്ന് അറിയാം...., എങ്കിലും...,. എവിടെയൊക്കെയോ..,.. ഒരു പ്രതീക്ഷ......",
    "Pranayikkuvaaanenkil oru paavam Pennine pranayikkanam... Avallde snehathin oru pratheka sukamaaa.",
    "നീ’ എന്ന ഒറ്റക്ഷരത്തിൽ തുടങ്ങിയ ‘പ്രണയം’‘നീ’ എന്ന ഒറ്റക്ഷരത്തിൽ ഒതുങ്ങുന്ന ‘ജീവിതം’‘നീ’ എന്ന ഒറ്റക്ഷരത്തിൽ അവസാനിക്കുന്ന ‘മരണം.",
    "ഒരിക്കലും മറക്കാന്‍ ആഗ്രഹിക്കാത്ത എന്‍റെ പ്രണയം അവനുമാത്രം അവകാശപ്പെടാനുള്ളതാണ്!!!.",
    "സ്വന്തമാക്കാന്‍ കഴിയില്ല എന്ന് നൂറുവട്ടം ഞാന്‍ എന്‍റെ മനസിനെ പറഞ്ഞ് പഠിപ്പിച്ചിട്ടും വീണ്ടും നിന്‍റെ ഓര്‍മ്മകള്‍ എന്നില്‍ നീ എന്‍റെ സ്വന്തമാണെന്ന് തോന്നിപ്പിക്കുന്നു...",
    "നമ്മളെ ഏറ്റവും കൂടുതൽ വേദനിപ്പിക്കാൻ കഴിയുന്നത്...നമ്മൾ ഏറ്റവും കൂടുതൽ സ്നേഹിക്കുന്നവർക്കാണ്....",
    "വിധിച്ച പെണ്ണിന്റെ പ്രാർഥനയാകും കൊതിച്ച പെണ്ണിനെ കിട്ടാതെ പോയത്....",
    "പരിഭവങ്ങള് പറയണം.. ഇടയ്ക്ക് പിണങ്ങണം..മൗനം കൊണ്ടെന്നെ നോവിക്കണം. അപ്പോഴേ...അപ്പോള് മാത്രമേ..എനിക്ക് നിന്നെവീണ്ടും വീണ്ടും സ്നേഹിക്കാനാകൂ.",
    "നല്ല കാര്യങ്ങൾ ചെയ്തുകൊണ്ടിരിക്കുക... ആരെയും ബോധ്യപ്പടുത്താൻ ശ്രമിക്കാതിരിക്കുക..ആളുകൾ ഒരിക്കലും നമ്മളിൽ സന്തുഷ്ടരാവുകയില്ല... ആരിൽ നിന്നും ഒരു നന്ദി വാക്കുപോലും പ്രതീക്ഷിക്കേണ്ടതുമില്ല... ഫലം ഇച്ഛിക്കാതെ കർമ്മം ചെയ്യുക..... വിജയം ഉറപ്പായും നമ്മെ തേടിയത്തും.",
    "ഏതു സങ്കടത്തിൽ നിന്നും കര കയറാനുള്ള ഒരേയൊരു വഴി നമ്മളേക്കാൾ സങ്കടമുള്ളവരുടെ കഥകൾ കേൾക്കുക എന്നത് തന്നെയാണ്'.",
    "ഒരു സംശയവുമില്ലാതെ നിങ്ങൾ പൂർണമായി ഒരാളെ വിശ്വസിക്കുമ്പോൾ,നമുക്ക് രണ്ട് ഫലങ്ങൾ ലഭിക്കാൻ സാധ്യതയുണ്ട്,ഒരെണ്ണം ജീവിതത്തിന്‌ നല്ല ഒരു വ്യക്തി,അല്ലെങ്കിൽ നല്ലൊരു പാഠം.",
    "പുതിയ പൂവുകൾ വിടരുമ്പോൾഒരിക്കൽ വസന്തം സമ്മാനിച പഴയ പൂവിനെ മറക്കരുത്,,,,,,,വാടിയതാണേലും സുഗന്ധമുള്ള പൂവായിരിന്നു അതും.............",
    "സിംഗിളാണെങ്കിലും ഡബിൾ ഓംലെറ്റ് എന്നുമെനിക്കൊരു വീക്ക്നെസ്സാണ്.....",
    "വിധിയും ഞാനും പിടിവലിയിലാണ്.... ജയിക്കാൻ ഞാനും... തോല്പ്പികാൻ ദൈവങ്ങളും.. കൂടെ അവളും.",
    "ബന്ധങ്ങൾ ഹൃദയത്തിൽ നിന്നും ഉണ്ടാകണം അല്ലാതെ വെറും വാക്കുകളിൽ മാത്രം ആകരുത്. പിണക്കങ്ങൾ വാക്കുകളിൽ ഉണ്ടായാലും ഒരിക്കലും ഹൃദയത്തിലുണ്ടാകരുത്...:.",
    "കൈയിൽ നാരങ്ങാ വെള്ളം കുടിക്കാൻ കാശിലേലും ഹിമാലയൻ യാത്ര പോണം എന്നാണ് ആഗ്രഹം....",
    "ഒരു നേരം പോക്കിന് എന്നെങ്കിലും കഴിഞ്ഞു പോയത് ആരോടെങ്കിലും പങ്ക് വെക്കുമ്പോൾ ,ഒരു തുള്ളി കണ്ണീര് പോലും വീഴാതെ നോക്കണേ പെണ്ണേ നീ....",
    "അകലങ്ങൾ നമ്മുടെ ഫ്രണ്ട്ഷിപ് അകറ്റിയാലും കാലം നമ്മെ പിരിച്ചാലും ഒരു മധുര സ്വപ്നമായി നിന്റെ സൗഹൃദം എന്നും എന്റെ മനസ്സിലുണ്ടാവും ..",
    "ഇടക്കൊക്കെ വിഷമങ്ങളെ സ്നേഹിക്കുക കാരണം .. വേനൽ ഇല്ലങ്കിൽ മഞ്ഞു കാലത്തിൻ സുഖം അറിയാൻ ആവില്ലന്നു ഓർക്കുക.",
    "അറിയില്ല നീ ആരാണെന്നു. എവിടെയാണെന്ന്... നിന്റെ പേരെന്താണെന്നു .. ഒരുനാൾ എന്റെ പേരെഴുതിയ മോതിരം നിന്റെ കൈകളിൽ അണിയുന്നതും സ്വപ്നം കണ്ട് ഇന്നും ഞാൻ ഏകനായ്.....",
    "ജീവിതത്തിൽ ഞാൻ ഏറെ ഇഷ്ട്ടപ്പെടുന്നത് സ്വപ്നം കാണാനാണ്....കാരണം, അവിടെയാണ് ഞാൻ സ്നേഹിക്കുന്നവർ എന്റെ കൂടെയുളളത്..",
    "ഒരു കവിത കൂടി ഞാൻ എഴുതി വക്കാം എന്റെ കനവിൽ നീ.....എത്തുമ്പോൾ ഓമനിക്കാൻ.",
    "എഴുതിയ ഒരു വരിയെക്കാൾ പ്രണയം തുളുമ്പുന്ന നൂറുവരികളുണ്ട് മനസ്സിൽ, നിന്നെക്കുറിച്ചു ഓർക്കുമ്പോൾ....",
    "നമുക്ക്‌ വേണ്ടി ഒന്നും ചെയ്യാനായില്ലെങ്കിലും നമ്മളെ സന്തോഷിപ്പിക്കാൻ സ്നേഹിക്കുന്നവർ ചെയ്യുന്ന ശ്രമങ്ങൾ മാത്രം മതി, മനസ്സ്‌ നിറയാൻ. അതൊരു വാക്കിലൂടെയാണെങ്കിൽ പോലും...",
    "കേന്ദ്രം കേരളത്തോട് കാണിക്കുന്നതാണ് പലപ്പോഴുംനീ എന്നോടും കാണിക്കാറ്...അതെന്നെ വേദനിപ്പിക്കുന്നുണ്ടെന്ന് ഇനിയെങ്കിലും നീ മനസ്സിലാക്കണം..",
    "ഇഷ്ട്പെട്ടത് നഷ്ടപ്പെടാതിരിക്കാൻ ഒരു പാട് കഷ്ടപ്പെടേണ്ടി വരും... !കഷ്ടപ്പെടാൻ ബുദ്ദിമുട്ടാണെൽ ചുമ്മാ കേറി കാണുന്നതൊന്നും ഇഷ്ട്പെടാൻ നിൽക്കരുത്.",
    "ജീവിതത്തിൽ നിന്നും ആരെയെങ്കിലും അകറ്റി നിർത്തിയിട്ടുണ്ടെങ്കിൽ അത് സ്നേഹക്കുറവ് കൊണ്ടല്ല, സ്നേഹക്കൂടുതൽ കൊണ്ടാണന്ന് മനസ്സിലാക്കുന്ന നിമിഷം ബന്ധങ്ങൾക്ക് ശക്തി കൂടും...",
    "കിട്ടില്ല എന്നറിഞ്ഞിട്ടും പിന്നെയും അവളെ പ്രണയിക്കുന്നതിലൊരു സുഖമുണ്ട്. മുറ്റത്തെ വെള്ളക്കെട്ടില്‍ തെളിഞ്ഞ അമ്പിളിമാമനെ കോരിയെടുക്കാന്‍ ശ്രമിക്കുന്ന കുട്ടിക്കാലത്തിന്‍റെ സുഖം.... ❤.",
    "അറിയില്ല നീ ആരാണെന്നു. എവിടെയാണെന്ന്... നിന്റെ പേരെന്താണെന്നു .. ഒരുനാൾ എന്റെ പേരെഴുതിയ മോതിരം നിന്റെ കൈകളിൽ അണിയുന്നതും സ്വപ്നം കണ്ട് ഇന്നും ഞാൻ ഏകനായ്.....",
    "മണ്ണായ് പടച്ച എന്നെ മണ്ണിലേക്ക് തിരികെ... വിളിക്കും മുന്‍പ് മണ്ണാല്‍ പടച്ച നിന്റെ കൂടെ ഒന്ന് ജീവിക്കണം...അതിനു വേണ്ടിയാണ് ഇന്നെന്‍ കാത്തിരിപ്പ്.",
    "ദുഃഖത്തിന്റെ ത്രിവ്രതാ അറിയുന്നവർ പ്രണയിക്കില്ല മറിച്ചാണ് എങ്കിലോ പ്രീണയിച്ചവൻ ദുഃഖികയാതെയും ഇരുന്നിട്ടില്ല.",
    "ആവശ്യത്തിലധികം ലുക്കുമില്ല,,സംസാരിച്ച് വീഴ്ത്താനുള്ള കഴിവുമില്ല...പക്ഷെ എപ്പോഴെങ്കിലും എന്നേയുംതേടി ഒരു പെണ്ണ് വരുമെന്ന് വിശ്വസിക്കുന്നു.... വരുവോ ആവോ,,,.",
    "സ്നേഹിക്കാൻ ഒരു മനസ്സുണ്ടെങ്കിൽ പിന്നെ കുറവുകൾക്കൊന്നും അവിടെ സ്ഥാനമില്ല...കുറവുകൾ അറിഞ്ഞുസ്നേഹിക്കുമ്പോഴാണ് സ്നേഹം ആത്മാർത്ഥമാകുന്നത്....",
    "നമ്മളെ ഏറ്റവും കൂടുതല്‍ വേദനിപ്പിക്കാന്‍ കഴിയുന്നത് നമ്മള്‍ ഏറ്റവും കൂടുതല്‍ സ്നേഹിക്കുന്നവര്ക്കാണ്....",
    "ചുണ്ടുകൊണ്ട് ഒരുപെണ്കുട്ടിക്ക് നൽകുവാൻ കഴിയുന്ന ഏറ്റവും വലിയ സമ്മാനം. അത്ചുമ്പനം അല്ല പുഞ്ചിരിയാണ്.",
)

@run_async 
def alone(update, context):
    # reply to correct message
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(AFW_STRINGS))





__mod_name__ = "Alone"

ALONE_HANDLER = DisableAbleCommandHandler("alone", alone)

dispatcher.add_handler(ALONE_HANDLER)
