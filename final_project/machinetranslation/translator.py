'''Includes librarys and functions to translate'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION ='2018-05-01'

'''Function retrieve api key from env file'''
authenticator = IAMAuthenticator(f'{APIKEY}')
'''Function retrieve version of translator'''
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)
language_translator.set_service_url(URL)


'''Function will translate text'''
def english_to_french(english_text):

    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()

    french_text = translation['translations'][0]['translation']
    return french_text

'''Function will translate text'''
def french_to_english(french_text):

    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()

    english_text = translation['translations'][0]['translation']
    
    return english_text
