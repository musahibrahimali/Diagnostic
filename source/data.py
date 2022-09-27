from tensorflow.keras.models import load_model
import numpy as np
import librosa
import librosa.display

# load the model
model = load_model('./models/model.h5')
# print the summary of the model
# model.summary()

# location of test audio file
test_audio_file = 'rec.wav'

# test the model
# load the audio file
audio, sample_rate = librosa.load(test_audio_file, res_type='kaiser_fast')
# extract mfcc features
mfccs = np.mean(librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40).T, axis=0)
# convert 2d mfcc to 4d
mfccs = mfccs.reshape(1, mfccs.shape[0])
# make prediction
prediction = model.predict_step(mfccs)
# print the predicted label
print('Predicted:', prediction)
