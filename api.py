from fastapi import FastAPI
from pydantic import BaseModel
import gradio as gr

from app1 import demo
from model1 import analyze_text


app = FastAPI(
    title="NLP Linguistic Analysis API",
    description=(
        "API for Named Entity Recognition, POS tagging, "
        "POS distribution, lemmatization, stemming, "
        "morphology and dependency parsing."
    ),
    version="1.0.0"
)


class TextRequest(BaseModel):
    text: str


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "NLP Linguistic Analysis API"
    }


@app.post("/api/analyze")
def analyze(request: TextRequest):
    return analyze_text(request.text)


app = gr.mount_gradio_app(
    app,
    demo,
    path="/"
)
