import os

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import EntitiesOptions, Features


def process_text(text):
    authenticator = IAMAuthenticator(os.getenv("NLU_API_KEY"))
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version="2020-09-13", authenticator=authenticator
    )
    natural_language_understanding.set_service_url(os.getenv("NLU_URL"))
    response = natural_language_understanding.analyze(
        text=text,
        features=Features(
            entities=EntitiesOptions(sentiment=True, model=os.getenv("NLU_MODEL"))
        ),
    ).get_result()
    return response
