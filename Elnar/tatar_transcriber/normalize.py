import re

def clean_text(text):
    """
    Keep only Arabic letters, spaces, line breaks
    """
    # \u0600-\u06FF = арабские символы
    text = re.sub(r'[^\u0600-\u06FF\s\n]', '', text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()

def normalize_arabic(text):
    """
    Remove Arabic diacritics and unwanted marks
    """
    # удаляем диакритики
    text = re.sub(r'[\u0610-\u061A\u064B-\u065F]', '', text)
    return text
