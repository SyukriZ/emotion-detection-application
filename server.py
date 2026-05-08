from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Ambil teks daripada input pengguna di laman web
    text_to_analyze = request.args.get('textToAnalyze')

    # Guna fungsi padu kau tadi
    response = emotion_detector(text_to_analyze)

    # Kalau tak dapat respon (Task 7 nanti kita buat lebih detail)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Ayat yang akan keluar kat skrin web pengguna
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    # Paparkan interface utama
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
