from enum import Enum

# Токент бота
token = '5043420848:AAFSQjtCTJCbUFlXrh_NVcSvRKtFCG0Qu0Q'

# Файл базы данных Vedis
db_file = "db.vdb"

# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"


# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_FIRST_NUM = "STATE_FIRST_NUM"
    STATE_SECOND_NUM = "STATE_SECOND_NUM"
    STATE_THIRD_NUM = "STATE_THIRD_NUM"
    STATE_OPERATION = "STATE_OPERATION"
