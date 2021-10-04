# Настройки БД
DB_ADDR = "192.168.3.74"
DB_NAME = "archMain"
DB_URI = f"postgresql+psycopg2://postgres:postgres@{DB_ADDR}:5432/{DB_NAME}"
DB_NAMES_URI = f"postgresql+psycopg2://postgres:postgres@{DB_ADDR}/archRef"

# Настройки потоков
NUMBER_OF_THREADS = 1


# Настройки моделей
MODEL_NAME = "trixie_old_version"
