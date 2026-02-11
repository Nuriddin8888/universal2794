from googletrans import Translator

translator = Translator()

def tarjimon(user_text: str, user_lang: str) -> str:
    result = translator.translate(text=user_text, dest=user_lang)
    return result.text
