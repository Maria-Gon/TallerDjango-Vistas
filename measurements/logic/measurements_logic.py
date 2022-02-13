from ..models import Variable
from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_measurement(mea_pk, new_mea):
    measurement = get_measurement(mea_pk)
    measurement.value = new_mea["value"]
    measurement.unit = new_mea["unit"]
    measurement.place = new_mea["place"]
    measurement.save()
    return measurement

def create_measurement(mea, var_pk):
    measurement = Measurement(variable=Variable.objects.get(pk=var_pk))
    measurement = Measurement(value=mea["value"])
    measurement = Measurement(unit=mea["unit"])
    measurement = Measurement(place=mea["place"])
    measurement.save()
    return measurement

def delete_measurement(mea_pk):
    measurement = get_measurement(mea_pk)
    measurement.delete()
    return measurement