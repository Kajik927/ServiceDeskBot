import telegram
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Bot
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, Filters

TOKEN='800916309:AAEd5dc4vXBz1fXeksPW-GTr5vC5j4AWvok'
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('PythonProject-9d39146577e3.json',scope)
client = gspread.authorize(creds)

url='https://docs.google.com/spreadsheets/d/1AzFZA6BQW4xgDI4dubQgH6uCm3vb29gB9X0ZEKw9RU4/edit?usp=sharing'

sheet = client.open_by_url(url).sheet1


def start(update, context):
  chat_id = update.message.chat_id
  text = update.message.text
  print(chat_id)
  print(update)
  first = update.message.chat['first_name']
  last = update.message.chat['last_name']
  print(first, last)
  
  context.bot.send_message(chat_id=chat_id, text=f'Привет, {first}\nЯ Service desk Bot и я помогаю тебе решить проблему с It service.\nУ меня есть такие команды: /problem - в этой команде есть список проблем с консультациями\n/cancel - отменяет заявку  ')

def problem(update, context):
  chat_id = update.message.chat_id
  text = update.message.text
  
  buttons = [['Не включается компьютер'], ['Не работает интернет'],['Не печатает принтер'],['Не включается проектор']]
  m = ReplyKeyboardMarkup(buttons, one_time_keyboard=True)

  context.bot.send_message(chat_id=chat_id,
    text='Выберите вашу проблему',
    reply_markup=m)
  return 1

def first(update,context):
  chat_id=update.message.chat_id
  text=update.message.text

  if text=='Не включается компьютер':
    context.bot.send_message(chat_id=chat_id,text='''Не паникуйте и не делайте лишних движений. В такой ситуации главное не наделать лишнего, то есть не ухудшить ситуацию. К примеру, Вы можете спалить что-либо в ПК, поломать (ту же кнопку запуска), «сбить» операционную систему и т.д. Поэтому, если заметили, что компьютер не реагирует на нажатие кнопки, остановитесь и подумайте, всё ли включено, что Вы (или кто-либо ещё) сделали с компьютером ранее. Стабильно ли работает электроэнергия, нет ли перепадов. После чего приступайте к следующим пунктам.

Проверьте электропитание системного блока и монитора. Первым делом, проверьте питание компьютера, возможно шнур плохо вставлен в розетку или в сам системный блок. Попробуйте отсоединить/подсоединить его и ещё раз запустить компьютер. Если используете сетевой фильтр в качестве удлинителя, то проверьте, включен ли он в розетку, а также горит ли лампочка на его выключателе. Неисправным может быть и сам удлинитель либо одна из его розеток, для этого подключите системный блок напрямую или воспользуйтесь другим сетевым фильтром. Обратите внимание на блок питания: на современных моделях на них размещают дополнительную кнопку, отвечающую за включение или отключение компьютера, поэтому переключите кнопку в иное положение и попробуйте снова включить свой ПК. Также обратите внимание на кабель монитора, не отошел ли он.

Не включается или не запускается? Определитесь с формулировкой! Если компьютер не включается, это значит, что он не шумит, не горят индикаторы на системном блоке и монитор не подаёт «признаков жизни». Под фразой «компьютер не запускается» следует понимать работу компьютера, однако без загрузки операционной системы. Если Ваш ПК не запускается, то Вы будете слышать работу вентиляторов из системного блока, наблюдать мигание дисплея и индикаторов на системном блоке. На экране, как правило, будет мигать курсор. Ещё Вы можете слышать писк (разной звуковой длины и частоты, о том, что они означают и как их отличать, мы поговорим в конце статьи).
    ''')
  elif text=='Не работает интернет':
    context.bot.send_message(chat_id=chat_id,text=''' Подключаем кабель к маршрутизатору и компьютеру, в сетевой разъем, а реакции никакой. Статус подключения (на панели уведомлений), компьютер с красным крестиком “Нет доступных подключений”, который отображается когда сетевой кабель не подключен, никак не меняется после подключения кабеля.

Не работает интернет через роутер "Нет доступных подключений"Может быть проблема как в роутере, так и в кабеле, или компьютере. Точнее, в сетевой карте, которая как правило интегрирована в материнскую плату. Это выяснить очень просто: достаточно подключить к компьютеру кабель от интерне-провайдера, не через роутер. Если реакция на подключение есть, то с сетевой картой скорее всего все нормально. Или подключить к роутеру, этим же кабелем другой компьютер. Таким способом, мы узнаем в чем проблема.

Если компьютер не реагирует ни на одно подключение кабеля (из разных источников), то возможно, что проблема в сетевой карте. Можно купить и поставить новую, стоят они не дорого. Так же, зайдите в диспетчер устройств, и посмотрите, есть ли там сетевая карта.
    ''')
  elif text=='Не печатает принтер':
    context.bot.send_message(chat_id=chat_id,text=''' Всем привет! Если вы посетили эту статью, то, наверняка, у вас возникли проблемы с принтером и вас интересует вопрос «Почему принтер не печатает?» Постараюсь вам в этом помочь. Конечно же, пользу печатающего устройства сложно переоценить. Он нужен везде: в доме и в офисе, в школе и на заводе. Словом, в эпоху информационных технологий этот аппарат необходим почти повсеместно, поскольку значительно облегчает работу. Можете еще прочитать статью про ошибку 651, а еще иногда у вас может возникнуть неопознанная сеть без доступа к интернету.


Проблемы с печатающим устройством не зависят от его типа (лазерный, матричный, струйный, сублимационный) или от фирмы производителя. Даже такие известные марки, как Canon, HP, Epson или Samsung не гарантируют отсутствие поломок или проблем с их печатающими устройствами. Итак, если принтер не хочет печатать с компьютера, тогда проделайте следующее:

Проверьте сам девайс. То есть сделайте распечатку тестовой страницы, нажав на принтере соответствующую кнопку. Если не получилось, проверьте бумагу, правильность установки картриджа и повторите снова. Обратите внимание на индикатор: он должен гореть «зелёным». Не помогает? Идем дальше.
Проверьте провод электропитания, его контакт с принтером. Если тестовая страница печатается, а с компьютера данные не выходят на печать, тогда нужно отрегулировать настройки в системе.
Для начала проверьте контакт кабеля в принтере и в системном блоке. Теперь пронаблюдайте за экраном монитора, когда отсылаете документы на печать. Если ничего не происходит, проверьте, не стоит ли «птичка» в диспетчере, возле пункта «Приостановить печать»?
    ''')
  elif text=='Не включается проектор':
    context.bot.send_message(chat_id=chat_id,text='''Проверьте кабель питания и если все подключено нажмите на проекторе либо на пулте от проектора "Power"  
    ''')
 
  buttons=[['Да'],['Нет']] 
  m = ReplyKeyboardMarkup(buttons, one_time_keyboard=True)

  context.bot.send_message(chat_id=chat_id,text='Помогло ли вам решение ?',reply_markup=m)
  return 2

  

def second (update,context):
  chat_id=update.message.chat_id
  text=update.message.text

  if text=='Да':
    context.bot.send_message(chat_id=chat_id,text='Спасибо мы были рады вам помочь до скорых встреч))')
  else:
    context.bot.send_message(chat_id=chat_id,text='Пожлуйста опишите вашу проблему')
  to_add=[chat_id,text]
  sheet.insert_row(to_add)  
  return ConversationHandler.END



def cancel (update,context):
  chat_id = update.message.chat_id
  text = update.message.text
  
  context.bot.send_message(chat_id=chat_id,text='вы отменили заявку')
  
  return ConversationHandler.END


updater=Updater(TOKEN,use_context=True) 

dialog =ConversationHandler(
  entry_points=[CommandHandler('problem',problem)],
  
  states={
    1:[MessageHandler(Filters.text,first,pass_user_data=True)],
    2:[MessageHandler(Filters.text,second,pass_user_data=True)]
  },
  
  fallbacks=[CommandHandler('cancel',cancel,pass_user_data=True)]    
)


start_handler=CommandHandler('start',start)
cancel_handler=CommandHandler('cancel',cancel)


dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(dialog)
dispatcher.add_handler(cancel_handler)

	
updater.start_polling()
updater.idle()

