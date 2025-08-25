import cv2

imagem = cv2.imread("img/pexels-photo-6238122.webp")


detector_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
deteccoes = detector_face.detectMultiScale(imagem_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for x, y, largura, altura in deteccoes:
  cv2.rectangle(imagem, (x, y), (x + largura, y + altura), (255, 0, 0), 2)
cv2.imshow("Deteccco de rostos:", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()