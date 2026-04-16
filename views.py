from django.shortcuts import render
import speech_recognition as sr
import tempfile
from pydub import AudioSegment
import tempfile


# Create your views here.

def UserHomePage(request):
    return render(request, 'users/userhome.html')

#-----------------------------------------------------------------------------------------------------

def Task1(request):
    return render(request, 'users/task1.html')

#-----------------------------------------------------------------------------------------------------

def ConfusionMatrice(request):
    return render(request, 'users/confusion_matrix.html')

#------------------------------------------------------------------------------------------------------

 
#-------------------------------------------------------------------------------------------------------
# views.py
from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from .forms import HateSpeechForm
from django.conf import settings
import os

svm_path = os.path.join(settings.MEDIA_ROOT,'finalized_model_SVM.sav')
nb_path = os.path.join(settings.MEDIA_ROOT,'finalized_model_NB.sav')
# Load the models and vectorizer
loaded_model_svm = pickle.load(open(svm_path, 'rb'))
loaded_model_nb = pickle.load(open(nb_path, 'rb'))


data_path = os.path.join(settings.MEDIA_ROOT,'processed_data_vol2.csv')
# Load the processed data to fit the vectorizer
dp = pd.read_csv(data_path, encoding='cp1252')

# Fit the Tfidf Vectorizer
Tfidf_vect = TfidfVectorizer()
Tfidf_vect.fit(dp['text_final'])

def hate_speech_predictor(request):
    import speech_recognition as sr
    import tempfile
    from pydub import AudioSegment

    result = None

    if request.method == 'POST':
        print("🔥 VIEW CALLED")
        print("✅ POST REQUEST RECEIVED")

        form = HateSpeechForm(request.POST, request.FILES)

        if not form.is_valid():
            print("❌ FORM ERRORS:", form.errors)
            return render(request, 'users/hate_speech_form.html', {
                'form': form
            })

        print("✅ FORM IS VALID")

        text_input = form.cleaned_data.get('sentence', '')
        audio_file = request.FILES.get('audio')

        print("📝 TEXT:", text_input)
        print("🎙 AUDIO:", audio_file)

        # 🔴 BLOCK EMPTY INPUT
        if (not text_input.strip()) and not audio_file:
            return render(request, 'users/hate_speech_form.html', {
                'form': form,
                'error': 'Please enter text or upload audio'
            })

        # 🎙 AUDIO → TEXT
        if audio_file:
            recognizer = sr.Recognizer()
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                    audio = AudioSegment.from_file(audio_file)
                    audio = audio.set_channels(1).set_frame_rate(16000)
                    audio.export(temp_audio.name, format="wav")

                with sr.AudioFile(temp_audio.name) as source:
                    audio_data = recognizer.record(source)

                try:
                    text_input = recognizer.recognize_google(audio_data, language="en-IN")
                    print("🎧 AUDIO TEXT:", text_input)

                except sr.UnknownValueError:
                    print("❌ Google could not understand audio")
                    text_input = "Audio could not be recognized"

                except sr.RequestError as e:
                    print("❌ API error:", e)
                    text_input = "Speech service error"

            except Exception as e:
                print("❌ AUDIO PROCESSING ERROR:", e)
                text_input = "Audio processing failed"

        # 🔎 ML PREDICTION
        new_input = [text_input]
        new_input_Tfidf = Tfidf_vect.transform(new_input)

        svm_pred = loaded_model_svm.predict(new_input_Tfidf)[0]
        nb_pred = loaded_model_nb.predict(new_input_Tfidf)[0]

        result = {
            'input_text': text_input,
            'svm': 'Hateful' if svm_pred == 0 else 'Not Hateful',
            'nb': 'Hateful' if nb_pred == 0 else 'Not Hateful'
        }

        print("✅ RESULT:", result)

    else:
        form = HateSpeechForm()

    return render(request, 'users/hate_speech_form.html', {
        'form': form,
        'result': result
    })
