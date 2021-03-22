import io
import json
import cv2
import requests

img = cv2.imread("/home/fantom/Documents/Tech Guide Non-Profit/ML-Text-Detection/pythonProject/screenshot.png")
height, width, _ = img.shape
print(img)

# Cutting image
roi = img[0: height, 0: width]

# Sent to OCR
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)
result = requests.post(url_api,
              files = {"screenshot.jpg": file_bytes},
              data = {"apikey": "Y1b833cfeec88957",
                      "language": "eng"})
print(result.content.decode())
cv2.imshow("roi", roi)
cv2.imshow("Img", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


result = result.content.decode()
result = json.loads(result)



# this gives an array with only one slot
parsed_results = result.get("ParsedResults")[0]

string_text = parsed_results.get("ParsedText")


#print(string_text)

output_file = open(r'/home/fantom/Documents/Tech Guide Non-Profit/ML-Text-Detection/extracted_text_from_image.txt', 'w+')
output_file.write(string_text)
output_file.close()