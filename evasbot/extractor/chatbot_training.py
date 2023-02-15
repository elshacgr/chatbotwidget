#!/usr/bin/env python
import string
import joblib
import pickle
import pandas as pd
import pyrebase
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.calibration import CalibratedClassifierCV
from sklearn.feature_extraction.text import TfidfVectorizer

from json_parser import json_parser
import warnings
warnings.filterwarnings("ignore")
 
# import json
# import pyrebase
import json

firebaseConfig = {
  "apiKey": "AIzaSyDgPO_M_b8CezbOCfS3UndPd89_W8vZawY",
  "authDomain": "evasbottrainintent.firebaseapp.com",
  "databaseURL": "https://evasbottrainintent-default-rtdb.firebaseio.com",
  "projectId": "evasbottrainintent",
  "storageBucket": "evasbottrainintent.appspot.com",
  "messagingSenderId": "474135742583",
  "appId": "1:474135742583:web:a32e85f5637171e0df9e72"
};
# Initialize Firebase
firebase= pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

xxx= database.get()
# print(xxx.val())
saved= xxx.val()

jsonString = json.dumps(saved)
jsonFile = open("./data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()


# Preprocessing data
def preprocess(chat):
    """
    Fungsi yang digunakan untuk melakukan praproses
    """
    # konversi ke lowercase
    chat = chat.lower()
    # menghapus tanda baca
    tandabaca = tuple(string.punctuation)
    chat = ''.join(ch for ch in chat if ch not in tandabaca)
    return chat

# Load data

# Load data
path = "./data.json"
jp = json_parser()
jp.parse(path)
df = jp.get_dataframe()


# Implementasikan fungsi preprocess ke string

df['text_input_prep'] = df.text_input.apply(preprocess)

corpus = df['text_input_prep'].to_numpy()

# Pemodelan
model_vectorizer = TfidfVectorizer(analyzer='word',ngram_range=(1,3)) #coba ganti (0,4)
model_vectorizer.fit(corpus)

# print(model_vectorizer.vocabulary_)

joblib.dump(model_vectorizer, "./vectorize.pkl")

vectorizer = joblib.load("./vectorize.pkl")
train_data = vectorizer.transform(df['text_input_prep']).toarray()
feature_train = pd.DataFrame(data=train_data, columns = vectorizer.get_feature_names_out())
feature_train

model = SVC(probability=True,kernel='linear')
svm = LinearSVC()
model = CalibratedClassifierCV(svm)

# Deklarasi pipeline yang mengandung vektorisasi (CountVectorizer) & pemodelan
pipe = make_pipeline(TfidfVectorizer(),
                    CalibratedClassifierCV(svm))

# Training
pipe.fit(df.text_input, df.intents)

# Training data
# print("[INFO] Training Data ...")
model.fit(train_data, df.intents)

# save the model to disk
filename = './svm.model'
pickle.dump(model, open(filename, 'wb'))
print("Helloworld")
