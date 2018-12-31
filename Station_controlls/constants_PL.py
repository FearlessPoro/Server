class Constants:
    DATA_TOO_OLD_ERROR_MESSAGE = '''Zbyt stare dane.
    Upewnij się czy twoj czujnik wysyla poprawna date w formacie:
    YYYY-MM-DD HH:MM:SS\n'''
    MINIMUM_REQUIREMENTS_MET_MESSAGE = 'Dane sa wystarczajace. Przetwarzanie...\n'
    INSUFFICIENT_DATA_FOUND_ERROR = 'Dane musza zawierac pola: Station_ID i Time_of_measurements\n'
    PRESSURE_MEASUREMENT_FOUND_MESSAGE = 'Znaleziono i dodano pomiar cisnienia\n'
    TEMPERATURE_MEASUREMENT_FOUND_MESSAGE = 'Znalezino i dodano pomiar temperatury\n'
    HUMIDITY_MEASUREMENT_FOUND_MESSAGE = 'Znaleziono i dodano pomiar wilgotnosci\n'
    SMALL_PARTICLE_MEASUREMENT_FOUND_MESSAGE = 'Znaleziono i dodano pomiar czasteczek PM2.5\n'
    BIG_PARTICLE_MEASUREMENT_FOUND_MESSAGE = 'Znaleziono i dodano pomiar czasteczek PM10\n'
    DATETIME_FORMAT_STRING = "%Y-%m-%d %H:%M:%S"
    DATA_PARSING_ENDED_MESSAGE = 'Zakonczono przetwarzanie danych.\n'
    ID_MESSAGE = 'Dodane dane maja id: '
    INCORRECT_REQUEST_TYPE_MESSAGE = 'Ta strona powinna byc wywolywana tylko poprzez poprawne paczki danych JSON\n'

    SMALL_PARTICLES_MEASUREMENTS_VALUE_VARIABLE = 'PM25_value'
    SMALL_PARTICLE_MEASUREMENTS_UNIT_VARIABLE = "PM25_unit"
    BIG_PARTICLES_MEASUREMENTS_VALUE_VARIABLE = 'PM10_value'
    BIG_PARTICLE_MEASUREMENTS_UNIT_VARIABLE = "PM10_unit"
    PRESSURE_VALUE_VARIABLE = 'pressure_value'
    PRESSURE_UNIT_VARIABLE = 'pressure_unit'
    TEMPERATURE_VALUE_VARIABLE = 'temperature_value'
    TEMPERATURE_UNIT_VARIABLE = 'temperature_unit'
    HUMIDITY_VALUE_VARIABLE = 'humidity_value'
    STATION_ID_VARIABLE = "Station_ID"
    TIME_OF_MEASUREMENTS_VARIABLE = "Time_of_measurements"



