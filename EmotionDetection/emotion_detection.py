import requests
import json

def emotion_detector(text_to_analyse):
    # URL and Headers for the Watson NLP Emotion API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Send the POST request
    response = requests.post(url, json=myobj, headers=headers)
    
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the required set of emotions 
    # (The Watson API returns them under 'emotionPredictions')
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Create the dictionary as requested
    emotion_dict = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }
    
    # Find the dominant emotion (the one with the highest score)
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    
    # Add the dominant emotion to our dictionary
    emotion_dict['dominant_emotion'] = dominant_emotion
    
    return emotion_dict