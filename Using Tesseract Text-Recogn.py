from PIL import Image
#from Python Image Library
import pytesseract

img = Image.open(r'/home/fantom/Documents/Tech Guide Non-Profit/ML-Text-Detection/screenshot.png')
string_text = pytesseract.image_to_string(img, lang="eng")
print(string_text)

output_file = open(r'/home/fantom/Documents/Tech Guide Non-Profit/ML-Text-Detection/extracted_text_from_image.txt', 'w+')
output_file.write(string_text)
output_file.close()