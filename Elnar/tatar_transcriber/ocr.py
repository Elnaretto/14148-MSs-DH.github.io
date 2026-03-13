from PIL import Image
import pytesseract

def ocr_image(file_path):
    """
    Считывает изображение и распознает текст арабской вязи
    """
    img = Image.open(file_path)
    
    # Указываем язык: ara = арабский
    text = pytesseract.image_to_string(img, lang='ara')
    
    return text
