import json
from datetime import datetime, timedelta

from Station_controls.constants import Constants
from Station_controls.models import *
from rest_framework.authtoken.models import Token


class Functions:

    @staticmethod
    def parse_send_request(request):
        return_message = ''
        time_delta = 3
        print(request.body)
        try:
            body_data = json.loads(request.body)
            if Constants.TIME_OF_MEASUREMENTS_VARIABLE in body_data and Functions.any_measurements_in_body(body_data):
                return_message += Constants.MINIMUM_REQUIREMENTS_MET_MESSAGE
                timestamp = datetime.strptime(body_data[Constants.TIME_OF_MEASUREMENTS_VARIABLE],
                                              Constants.DATETIME_FORMAT_STRING)
                if timestamp < datetime.now() - timedelta(days=time_delta):

                    return_message += Constants.DATA_TOO_OLD_ERROR_MESSAGE
                else:
                    tmp_token = request.META.get('HTTP_AUTHORIZATION')
                    identification_number = Token.objects.get(key=tmp_token[6:]).user_id
                    measurements_model = Measurements(
                        Station=Stations.objects.get(User=identification_number),
                        Time_of_measurement=body_data[Constants.TIME_OF_MEASUREMENTS_VARIABLE]
                    )
                    measurements_model.save()
                    latest_measurement_id = Measurements.objects.latest('id')
                    return_message += Constants.ID_MESSAGE + str(latest_measurement_id.id) + "\n"

                    if Constants.HUMIDITY_VALUE_VARIABLE in body_data:
                        humidity_measurements_model = HumidityMeasurements(
                            Measurement=latest_measurement_id,
                            Value=body_data[Constants.HUMIDITY_VALUE_VARIABLE]
                        )
                        humidity_measurements_model.save()
                        return_message += Constants.HUMIDITY_MEASUREMENT_FOUND_MESSAGE

                    if Constants.TEMPERATURE_VALUE_VARIABLE in body_data\
                            and Constants.TEMPERATURE_UNIT_VARIABLE in body_data:
                        temperature_measurements_model = TemperatureMeasurements(
                            Measurement=latest_measurement_id,
                            Value=body_data[Constants.TEMPERATURE_VALUE_VARIABLE],
                            Unit=body_data[Constants.TEMPERATURE_UNIT_VARIABLE]
                        )
                        temperature_measurements_model.save()
                        return_message += Constants.TEMPERATURE_MEASUREMENT_FOUND_MESSAGE

                    if Constants.PRESSURE_VALUE_VARIABLE in body_data\
                            and Constants.PRESSURE_UNIT_VARIABLE in body_data:
                        pressure_measurements_model = PressureMeasurements(
                            Measurement=latest_measurement_id,
                            Value=body_data[Constants.PRESSURE_VALUE_VARIABLE],
                            Unit=body_data[Constants.PRESSURE_UNIT_VARIABLE]
                        )
                        pressure_measurements_model.save()
                        return_message += Constants.PRESSURE_MEASUREMENT_FOUND_MESSAGE

                    if Constants.BIG_PARTICLES_MEASUREMENTS_VALUE_VARIABLE in body_data\
                            and Constants.BIG_PARTICLE_MEASUREMENTS_UNIT_VARIABLE in body_data:
                        big_particle_measurements_model = BigParticlesMeasurements(
                            Measurement=latest_measurement_id,
                            Value=body_data[Constants.BIG_PARTICLES_MEASUREMENTS_VALUE_VARIABLE],
                            Unit=body_data[Constants.BIG_PARTICLE_MEASUREMENTS_UNIT_VARIABLE]
                        )
                        big_particle_measurements_model.save()
                        return_message += Constants.BIG_PARTICLE_MEASUREMENT_FOUND_MESSAGE
                    if Constants.SMALL_PARTICLES_MEASUREMENTS_VALUE_VARIABLE in body_data\
                            and Constants.SMALL_PARTICLE_MEASUREMENTS_UNIT_VARIABLE in body_data:
                        small_particle_measurements_model = BigParticlesMeasurements(
                            Measurement=latest_measurement_id,
                            Value=body_data[Constants.SMALL_PARTICLES_MEASUREMENTS_VALUE_VARIABLE],
                            Unit=body_data[Constants.SMALL_PARTICLE_MEASUREMENTS_UNIT_VARIABLE]
                        )
                        small_particle_measurements_model.save()
                        return_message += Constants.SMALL_PARTICLE_MEASUREMENT_FOUND_MESSAGE
                    return_message += Constants.DATA_PARSING_ENDED_MESSAGE
            else:
                return_message += Constants.INSUFFICIENT_DATA_FOUND_ERROR
        except SyntaxError:
            return_message += Constants.INCORRECT_REQUEST_TYPE_MESSAGE
            return return_message
        except Exception:
            return_message += Constants.NO_SUCH_TOKEN_MESSAGE
            return return_message
        return return_message

    @staticmethod
    def any_measurements_in_body(body_data):
        if Constants.SMALL_PARTICLE_MEASUREMENTS_UNIT_VARIABLE in body_data:
            return True
        if Constants.BIG_PARTICLES_MEASUREMENTS_VALUE_VARIABLE in body_data:
            return True
        if Constants.PRESSURE_VALUE_VARIABLE in body_data:
            return True
        if Constants.TEMPERATURE_UNIT_VARIABLE in body_data:
            return True
        if Constants.HUMIDITY_VALUE_VARIABLE in body_data:
            return True
        return False

