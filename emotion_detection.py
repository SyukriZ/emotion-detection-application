import requests
import json

def emotion_detector(text_to_analyze):
    # URL API Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers untuk model AI
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Payload (Teks yang hendak dianalisis)
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Menghantar permintaan ke API
    response = requests.post(url, json=myobj, headers=header)
    
    # Menukar respons teks kepada JSON (Dictionary)
    formatted_response = json.loads(response.text)

    # Ekstrak data emosi (Logik untuk Task 3)
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Cari emosi dominan (skor paling tinggi)
        dominant_emotion = max(emotions, key=emotions.get)

        # Susun output akhir
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        # Jika API bermasalah (Task 7 persiapan)
        result = None

    return result
