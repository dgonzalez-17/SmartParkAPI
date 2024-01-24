from fastapi import APIRouter, HTTPException
import telebot
from models.parkingslot_model import Parkingslot
from services.telebot_service import bot_workflow, update_slot_by_number

telegram_router = APIRouter(prefix='/telegram')

API_TOKEN = "6712680828:AAH_SxfneToOhwUZtV9rkUj6I2vBaJuD7qk"

bot = telebot.TeleBot(API_TOKEN)


@telegram_router.post("/webhook", tags=["TelegramBot"])
def telegram_webhook(data: dict):
    if data:
        # print(data)
        update = telebot.types.Update.de_json(data)
        bot.process_new_updates([update])
        return {"status": "ok"}
    else:
        return


@bot.message_handler(commands=["start"])
def start_bot(message):
    bot.reply_to(message, """

""")

@bot.message_handler(commands=["help"])
def help_bot(message):
    bot.reply_to(message, """
                 Hola, soy tu SmartParkBot, estoy acá para hacer más fácil tu gestión, recuerda que las opciones son las siguientes:\n\n
/start inicia una nueva conversación. \n
/help te muestra este menú de ayuda. \n
\"Ver parqueaderos disponibles\" -> Te devuelve el numero (total y el identificador de cada parqueadero) de los parqueaderos libres.\n
\"Actualizar precio por minuto \"vehiculo\" \"precio\"\"-> Tienes las opciones "moto", bicicleta" o carro" en la opción vehiculo y un valor para la opción precio.\n
\"Ingresar vehiculo \"placa\"\" -> Envias la placa del vehiculo en la forma "XDE-897" para carros y motos y "101004596" para bicicletas. Te devolverá la hora de ingreso.\n
\"Salida vehiculo \"placa\"\" -> Envias la placa del vehiculo en la forma "XDE-897" para carros y motos y "101004596" para bicicletas. Te devolverá la hora en que se registró la salida y el total a pagar.\n
\"Ver ganancias de hoy\" -> "Te devolverá ganancias del día de hoy.\n
\"Ver ganancias de este mes\" -> Te devolvera ganancias del este mes.\n
""")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    print(message)
    bot.send_message(message.chat.id, bot_workflow(message))


@telegram_router.put("/status_slots/{number}", tags=["Parkingslot"])
def send_status_parkingslots(number: int, data: Parkingslot):
    message_parameters = update_slot_by_number(number, data)
    send_especific_message(message_parameters) if message_parameters else None


def send_especific_message(data: dict):
    bot.send_message(chat_id=data['id'], text=data['message'])


webhook_url = "https://bfdd-186-147-127-14.ngrok-free.app/telegram/webhook"
bot.remove_webhook()
bot.set_webhook(url=webhook_url)

# loop = asyncio.get_running_loop()
# loop.create_task(bot.set_webhook(url=webhook_url))
