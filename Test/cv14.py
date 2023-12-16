import cv2
import numpy as np
import requests

url = r'https://media.discordapp.net/attachments/1061377727363567707/1147218173540716574/image.png?format=webp&width=662&height=662'
resp = requests.get(url, stream=True).raw
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

ksize = (90, 90) 

 
image1 = cv2.blur(image, ksize, cv2.BORDER_DEFAULT) 
cv2.imwrite("C:/Users/yeash/Downloads/koop.png",image1)

cv2.waitKey(0)
