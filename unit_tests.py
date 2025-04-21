import unittest
from transformers import pipeline

# Funzione da testare
def emotion_predictor(text):
    emotion_classifier = pipeline('sentiment-analysis', model='j-hartmann/emotion-english-distilroberta-base')
    result = emotion_classifier(text)
    return result

# Classe di test unitari
class TestEmotionPredictor(unittest.TestCase):
    def test_happy_emotion(self):
        text = "I am very happy today!"
        result = emotion_predictor(text)
        self.assertEqual(result[0]['label'], 'joy')

    def test_sad_emotion(self):
        text = "I am very sad today."
        result = emotion_predictor(text)
        self.assertEqual(result[0]['label'], 'sadness')

    def test_neutral_emotion(self):
        text = "I am feeling okay."
        result = emotion_predictor(text)
        self.assertEqual(result[0]['label'], 'joy')

if __name__ == "__main__":
    unittest.main()
