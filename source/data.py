from tensorflow.keras.models import load_model
from tensorflow.keras.models import model_from_json
import tensorflow as tf

# load the json model from models/model_json.json
json_file = open('models/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

# load the weights from models/model.h5
model = loaded_model.load_weights("models/model.h5")


