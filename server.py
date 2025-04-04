"""Flask web application for detecting emotions from user input."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the home page with input form."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """Handle emotion analysis request and return formatted result."""    
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again.</b>"

    return f"""
        <b>Analysis Result:</b><br><br>
        Anger: {result['anger']}<br>
        Disgust: {result['disgust']}<br>
        Fear: {result['fear']}<br>
        Joy: {result['joy']}<br>
        Sadness: {result['sadness']}<br><br>
        <b>Dominant Emotion:</b> {result['dominant_emotion']}
    """

if __name__ == '__main__':
    app.run(debug=True)
    