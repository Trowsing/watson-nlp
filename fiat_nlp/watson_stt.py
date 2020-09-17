import os

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1

KEYWORDS = [
    "belo",
    "acabamento",
    "andróide",
    "quilômetros",
    "litro",
    "auto",
    "apple",
    "car",
    "lindíssimo",
    "motor",
    "porta-malas",
    "freios",
    "multimídia",
    "argo",
    "fiorino",
    "ducato",
    "cronos",
    "500",
    "marea",
    "linea",
    "renegade",
]


def get_speech_to_text():
    authenticator = IAMAuthenticator(os.getenv("STT_API_KEY"))
    speech_to_text = SpeechToTextV1(authenticator=authenticator)
    speech_to_text.set_service_url(os.getenv("STT_URL"))
    return speech_to_text


def get_file_text(file):
    stt = get_speech_to_text()
    response = stt.recognize(
        file,
        content_type="audio/flac",
        model="pt-BR_NarrowbandModel",
        keywords=KEYWORDS,
        keywords_threshold=0.3,
        split_transcript_at_phrase_end=False,
        end_of_phrase_silence_time=2.0,
        background_audio_suppression=0.3,
    ).get_result()
    texts = []
    for result in response["results"]:
        text = result["alternatives"][0]["transcript"]
        texts.append(text)
    return "\n".join(texts)
