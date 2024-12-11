from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    data = request.get_json()
    statement = data.get('statement', '')

    # Call the emotion detector function
    result = emotion_detector(statement)

    # Format the output as required
    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
