"""
server.py

This module provides a Flask web server for detecting emotions from text
using the EmotionDetection package. It exposes an endpoint that accepts
a statement and returns emotion scores along with the dominant emotion.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Endpoint to detect emotions from a given statement.
    
    Returns:
        JSON response containing emotion scores and dominant emotion,
        or an error message if the input is invalid.
    """
    data = request.get_json()
    statement = data.get('statement', '')

    # Call the emotion detector function
    result = emotion_detector(statement)

    # Check if dominant_emotion is None
    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Return the result directly
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
