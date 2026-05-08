import requests  # Import library untuk menghantar HTTP requests
import json      # Import library untuk memproses data JSON

def emotion_detector(text_to_analyze):
    # URL untuk perkhidmatan Watson NLP Emotion Analysis
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Header yang diperlukan oleh API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Format data (Payload) yang akan dihantar dalam bentuk JSON
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Menghantar POST request ke API
    response = requests.post(url, json=myobj, headers=header)
    
    # Menukar maklum balas (response) dari bentuk teks ke JSON (Dictionary)
    formatted_response = json.loads(response.text)
    
    # Memulangkan hasil analisis emosi
    return formatted_response
