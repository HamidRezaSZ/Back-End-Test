from django.apps import AppConfig
from django.conf import settings
from tensorflow import keras
import os


class CnnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cnn'


class CifarModelConfig(AppConfig):
    name = 'cnnAPI'
    MODEL_FILE = os.path.join(settings.MODELS, "my_cifar10_model.h5")
    model = keras.models.load_model(MODEL_FILE)