from PIL import Image
import pytesseract

def extract_text(screenshot_img: str) -> str:
    try:
        img  = Image.open(screenshot_img)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(f"Error while processing {screenshot_img}. Error: {e}")
        return ""