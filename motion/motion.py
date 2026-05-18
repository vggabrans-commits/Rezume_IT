#1 step : PowerShell:Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#2 step  : .\.venv\Scripts\Activate.ps1
#3 step :IMPORTANT: right now, when activated (.venv). pip install opencv-python
#4 step : run : python motion.py

#Подключаем OpenCV
import cv2

#Подключение камеры
cap = cv2.VideoCapture(0)

#Читаем первые два кадра
ret, frame1 = cap.read()
ret, frame2 = cap.read()

frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)

#Цикл работы камеры
while cap.isOpened():
    #Находим разницу между кадрами absdiff = absolute difference
    diff = cv2.absdiff(frame1, frame2)
    #Перевод в серый цвет
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    #Размытие (убираем шум)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    #Пороговая обработка (делаем маску движения)
    _, thresh = cv2.threshold(blur,20, 255, cv2.THRESH_BINARY)
    #Расширяем белые зоны
    dilated = cv2.dilate(thresh, None, iterations=3)
    #Поиск контуров
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        #Фильтрация мелкого шума
        if cv2.contourArea(contour) < 4000:
            continue
        #Рисуем прямоугольник
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,220,0), 2)
        #Пишем текст
        cv2.putText(frame1, "MOTION", (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    #Показываем результат
    cv2.imshow("Motion Detector", frame1)
    #Обновляем кадры
    frame1 = frame2
    ret, frame2 = cap.read()
    #Выход  27 = ESC
    if cv2.waitKey(40) == 27:
        break
#Освобождение камеры
cap.release()
cv2.destroyAllWindows()
