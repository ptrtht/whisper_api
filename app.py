from datetime import datetime
import json
import whisper
from flask import request
import requests as r


from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "chech"


@app.route("/transcribe", methods=['POST'])
def transcribe():
    start = datetime.now()
    print("start", start.isoformat())
    data = request.json
    url: str = data["url"]
    model: str = data["model"]

    if model not in ["tiny", "base", "small", "medium", "large"]:
        return {
            "success": False,
            "error": """Model not in ["tiny", "base", "small", "medium", "large"]"""
        }

    print("loading model")
    model = whisper.load_model(model)
    print("model loaded")
    result = model.transcribe(url)
    # print(result["text"])

    print("end", datetime.now())
    print("processing time:", datetime.now() - start)

    return {
        "success": True,
        "language": result["language"],
        "text": result["text"]
    }
