"""
Provides text translation from/to English & French
"""
import os
#import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION='2018-05-01'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)
language_translator.set_service_url(URL)

def englishToFrench(english_text):
    """translates string from English to French"""
    if english_text is None:
        return ""
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """translates string from French to English"""
    if french_text is None:
        return ""
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()['translations'][0]['translation']
    return english_text
