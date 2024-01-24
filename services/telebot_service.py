# from models.parkingslotModel import Parkingslot
# from services.pricesService import *
# from services.parkingslotService import getAvailableSlots, updateStatusSlotByNumber
from config.database import MongoClientSingleton
from models.parkingslot_model import Parkingslot
from models.price_model import Price
from models.historical_model import Historical
from schemas.parkingslot_schema import parkingslotEntity
from services.earning_service import EarningService
from services.price_service import PriceService
from services.parkingslot_service import ParkingslotService
from services.historical_service import HistoricalService

price_service = PriceService()
parkingslot_service = ParkingslotService()
earning_service = EarningService()
historical_service = HistoricalService()

db = MongoClientSingleton().get_database()

letras_espanolas = "abcdefghijklmnopqrstuvwxyz"
    
def bot_workflow(data: dict):
    user_message = data.text.lower()
    print("mensaje entrada :", user_message)
    if user_message.startswith("ver parqueaderos disponibles"):
        return get_available_slots()
    elif user_message.startswith("actualizar precio por minuto"):
        return update_Price_S(user_message)
    elif user_message.startswith("ingresar vehiculo"):
        return post_historical_data(user_message)
    elif user_message.startswith("salida vehiculo"):
        return put_historical_data(user_message)
    elif user_message.startswith("ver ganancias de hoy"):
        return get_today_earnings()
    elif user_message.startswith("ver ganancias de este mes"):
        return get_month_earnings()
    elif user_message.startswith("ver estadisticas"):
        return "https://dgonzalez271.grafana.net/public-dashboards/5bce11aad21f405e8b574449e994d515"
    else:
        return "Esta opción no es disponible, recuerda que con /help puedes ver las acciones disponibles.\nCon SmartParkBot queremos hacerte la vida más fácil."

def post_historical_data(user_message: str):
    user_message = user_message.replace("ingresar vehiculo ", "")
    user_message = user_message.split(" ")
    print(user_message)
    plate = "";
    for i in user_message:
        if i[0] in letras_espanolas:
            plate = i.upper()
            break
        elif i.isdigit():
            plate = i
            break
    historical = historical_service.create_historical(Historical(**{'plate': plate}))
    print(historical)
    if historical: 
        return "Vehiculo con placas {} ingresado el día y hora {}.".format(plate, historical['checkInTime'])
    else: 
        return "No se ha podido registrar el vehiculo"
    
def put_historical_data(user_message: str):
    user_message = user_message.replace("salida vehiculo ", "")
    user_message = user_message.split(" ")
    plate = "";
    for i in user_message:
        if i[0] in letras_espanolas:
            plate = i.upper()
            break
        elif i.isdigit():
            plate = i
            break
    historical = historical_service.update_one_paid_by_plate(Historical(**{'plate': plate}))
    print(historical)
    if historical: 
        return "Vehiculo con placas {} sale el día y hora {}.\n Valor a pagar {}.".format(plate, historical['checkInTime'], historical['totalValue'])
    else: 
        return "No se ha podido registrar salida del vehiculo."
    
def update_Price_S(user_message: str):
    user_message = user_message.replace("actualizar precio por minuto ", "")
    user_message = user_message.split(" ")
    data = {'typeVehicle': user_message[0],
            'price': user_message[1]}
    result = price_service.update_price_value_by_name(user_message[0], Price(**data))
    if result != None and ('price' in result and result['price'] == int(user_message[1])):
        print("entro el primero")
        return "Se ha modificado correctamente el precio."
    else: 
        return "Hubo un error al realizar la operación."


    
def update_slot_by_number(number:int, slot: Parkingslot):
    slot = dict(slot)
    del slot['id']
    result = db.parkingslot.update_one({"number": number},{"$set": slot}).modified_count
    if result > 0:
        return {'id': -1002141047253,
                'message':"El parqueadero numero {} se encuentra ahora en estado {}".format(slot['number'], "Ocupado" if slot['busyStatus'] else "Disponible")}

    
def get_available_slots():
    slots = parkingslot_service.get_avalable_slots()
    avaiable_slots = ", ".join(str(d["number"]) for d in slots)
    print(avaiable_slots)
    return "Los parqueaderos disponibles son: {}.".format(avaiable_slots) if len(slots) > 0 else "No hay parqueaderos disponibles en este momento."


def get_today_earnings():
    earnings = earning_service.get_today_earnings()
    print(earnings)
    return "Las ganancias de hoy son: {} COP.".format(earnings) if earnings is not None else "El día de hoy no se han registrado ganancias."

def get_month_earnings():
    earnings = earning_service.get_month_earnings()
    if not earnings:
        return "En este momento no podemos proporcionar las ganancias de este mes."
    else:
        return "Las ganancias de este mes son: {} COP.". format(earnings)