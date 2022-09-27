from tensorflow.keras.models import load_model
import numpy as np
import librosa
import librosa.display
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils

# load the model
model = load_model('./models/model.h5')

sample_data = "./data/u1.wav"

# load the audio file
audio_data, sample_rate = librosa.load(sample_data, res_type='kaiser_fast')

# reshape the audio data
audio_data = audio_data.reshape(1, -1)

# extract the features
mfccs = np.mean(librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=40).T, axis=0)

# print the features
print(mfccs)

# reshape the features
mfccs = mfccs.reshape(1, -1)

# predict the class
prediction = model.predict_step(mfccs)

# print the class
print(f"The class With : {prediction}")

# print the summary of the model
# model.summary()

# print(model.evaluate("rec.wav"))
