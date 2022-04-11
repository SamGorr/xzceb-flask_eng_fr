import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create an instance of the IBM Watson Language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(text):
    '''Function englishToFrench'''

    translation = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()

    return translation.get("translations")[0].get("translation")

def frenchToEnglish(text):
    '''Function frenchToEnglish'''

    translation = language_translator.translate(
        text=text,
        model_id='fr-en').get_result()

    return translation.get("translations")[0].get("translation")
    