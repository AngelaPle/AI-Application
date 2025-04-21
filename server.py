from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

def emotion_predictor(text):
    emotion_classifier = pipeline('sentiment-analysis', model='j-hartmann/emotion-english-distilroberta-base')
    result = emotion_classifier(text)
    return result

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'text' not in data:
            return jsonify({'error': 'La chiave "text" è obbligatoria nel corpo della richiesta JSON'}), 400
        text = data['text']
        emotions = emotion_predictor(text)
        return jsonify(emotions)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)