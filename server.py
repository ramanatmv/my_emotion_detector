"""
This module sets up a Flask web application for detecting emotions from text input.

The application has two routes:
1. "/" - Renders the home page.
2. "/emotionDetector" - Accepts a text input.

Modules:
- Flask: A web framework for creating web applications.
- render_template: Renders HTML templates.
- request: Handles incoming requests and extracts query parameters.
- emotion_detector: A function from the EmotionDetection module that analyzes text.

Functions:
- render_index_page: Renders the home page.
- emo_detector: Processes text input to detect emotions and returns the results.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create a Flask application instance
app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Render the home page.
    
    Returns:
        HTML template of the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    """
    Detect emotions from the provided text and return the results.
    
    Returns:
        str: A formatted string with the sentiment label and score.
        or
        str: A message requesting text input if none provided.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze:
        # Pass the text to the emotion_detector function and store the response
        response = emotion_detector(text_to_analyze)

        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        dominant_emotion = response['dominant_emotion']
        # Check if the dominant emotion is None (i.e., invalid text was provided)
        if dominant_emotion is None:
            return 'Invalid text! Please try again!'

        # Return a formatted string with the sentiment labels and their corresponding values
        return (f'For the given statement, the system response is '
                f'\'anger\': {anger}, \'disgust\': {disgust}, \'fear\': {fear}, '
                f'\'joy\': {joy}, \'sadness\': {sadness}. '
                f'The dominant emotion is {dominant_emotion}.')
    # If no text was provided, return a message requesting text input
    return "Please provide text to analyze."

# Run the Flask application when the script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
