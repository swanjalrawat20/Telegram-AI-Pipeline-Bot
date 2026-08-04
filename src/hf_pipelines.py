from transformers import pipeline

# Global model variables
sentiment_pipeline = None
summarizer = None


def get_sentiment_pipeline():
    global sentiment_pipeline
    if sentiment_pipeline is None:
        print("Loading sentiment model...")
        sentiment_pipeline = pipeline("sentiment-analysis")
        print("Sentiment model loaded!")
    return sentiment_pipeline


def get_summarizer():
    global summarizer
    if summarizer is None:
        print("Loading summarization model...")
        summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6"
        )
        print("Summarization model loaded!")
    return summarizer

# Text Generation
generator = None

def get_generator():
    global generator

    if generator is None:
        print("Loading text generation model...")
        generator = pipeline(
            "text-generation",
            model="distilgpt2"
        )
        print("Text generation model loaded!")

    return generator


def generate_text(prompt):
    model = get_generator()

    result = model(
        prompt,
        max_length=100,
        num_return_sequences=1
    )

    return result[0]["generated_text"]

def analyze_sentiment(text):
    model = get_sentiment_pipeline()
    result = model(text)

    return (
        f"😊 Sentiment: {result[0]['label']}\n"
        f"⭐ Confidence: {result[0]['score']:.2%}"
    )

translator = None

def get_translator():
    global translator

    if translator is None:
        print("Loading translation model...")
        translator = pipeline(
            "translation",
            model="Helsinki-NLP/opus-mt-en-fr"
        )
        print("Translation model loaded!")

    return translator


def translate_text(text):
    model = get_translator()

    result = model(text)

    return result[0]["translation_text"]

# Zero-Shot Classification
classifier = None

def get_classifier():
    global classifier

    if classifier is None:
        print("Loading zero-shot classification model...")
        classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
        print("Zero-shot classification model loaded!")

    return classifier


def classify_text(text):

    labels = [
        "Technology",
        "Education",
        "Business",
        "Sports",
        "Politics",
        "Health",
        "Entertainment"
    ]

    model = get_classifier()

    result = model(text, labels)

    return (
        f"🏷️ Category: {result['labels'][0]}\n"
        f"⭐ Confidence: {result['scores'][0]:.2%}"
    )

def summarize_text(text):
    model = get_summarizer()

    summary = model(
        text,
        max_length=100,
        min_length=20,
        do_sample=False
    )

    return summary[0]["summary_text"]