import datetime
from models.earning_model import Earning
from services.price_service import PriceService
from services.earning_service import EarningService

price_service = PriceService()
earning_service = EarningService()


def get_total_value(historical):
    minutes = difference_in_minutes(historical['checkInTime'], historical['checkOutTime'])
    price = price_service.get_one_price_by_name(type_vehicle(historical['plate']))
    return price * minutes

def difference_in_minutes(checkInTime: datetime, checkOutTime: datetime) -> int:
    if checkInTime is None or checkOutTime is None:
        return None

    difference = checkOutTime - checkInTime
    if (difference.total_seconds() // 60) <= 0:
        return 1
    else:
        return difference.total_seconds() // 60

def type_vehicle(plate: str):
    if len(plate) > 8:
        return "bicicleta"
    elif len(plate) == 6:
        return "moto"
    else:
        last_character = plate[-1]
        return "moto" if last_character.isalpha() else "carro"
    
def update_earning(value: int):
    earning = Earning(earnings=value)
    result = earning_service.update_one_earning_by_day(earning)
    if 'error' not in result:
        return True
    else: 
        return False
    
