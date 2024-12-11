import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send POST request to the Watson NLP EmotionPredict function
    response = requests.post(url, headers=headers, json=input_json)
    
    # Check if response is successful
    if response.status_code != 200:
        return {"error": "Failed to get a valid response"}
    
    # Parse the JSON response
    predictions = response.json().get('emotionPredictions', [])
    
    if predictions:
        emotions = predictions[0]['emotion']
        
        # Extract scores
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)

        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Create the output dictionary
        output = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
        return output
    else:
        return {}

# Example usage (uncomment to test)
# result = emotion_detector("I am very happy today!")
# print(result)