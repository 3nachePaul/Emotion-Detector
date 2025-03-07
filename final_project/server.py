"""
Flask server for emotion detection using Watson NLP API.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotions_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detection_route():
    """Function printing emotion % ."""
    text_to_analyze = request.args.get('text')

    if not text_to_analyze:
        return jsonify({"error": "Invalid text! Please try again!."}), 400

    result = emotions_detector(text_to_analyze)

    if isinstance(result, str) and result.startswith("Error"):
        return jsonify({"error": result}), 500

    if result['dominant_emotion'] is None:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
