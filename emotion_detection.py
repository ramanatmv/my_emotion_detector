import requests
import json  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = {"raw_document": {"text": text_to_analyse}}  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    
    try:
        response = requests.post(url, json=myobj, headers=header)  # Send a POST request to the API with the text and headers
        response.raise_for_status()  # Check for HTTP request errors
        
        formatted_response = response.json()  # Parse the JSON response from the API
        
        # Prepare the output format
        emotions = {
            'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
            'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
            'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
            'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
            'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness']
        }

        # Adding the dominant_emotion key
        emotions['dominant_emotion'] = max(emotions, key=emotions.get) if emotions else 'none'

        # Returning the formatted output
        return emotions

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"  # Return an error message if something goes wrong



