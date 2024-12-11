import requests

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
    
    # Print the entire response for debugging
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())
    
    # Return the text attribute from the response object
    return response.json().get('text', '')

# Example usage (uncomment to test)
# result = emotion_detector("I am very happy today!")
# print(result)
