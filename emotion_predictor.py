from transformers import pipeline


def emotion_predictor(text):
    emotion_classifier = pipeline('sentiment-analysis', model='j-hartmann/emotion-english-distilroberta-base')
    result = emotion_classifier(text)
    # Formattazione dell'output come richiesto: un dizionario con "emotion" e "score"
    if result:
        formatted_result = {"emotion": result[0]['label'], "score": result[0]['score']}
        return formatted_result
    else:
        return {"emotion": None, "score": None}


if __name__ == "__main__":
    text = "I am very happy today!"
    emotions = emotion_predictor(text)
    print(emotions)