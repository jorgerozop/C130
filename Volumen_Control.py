import cv2
import mediapipe as mp
from pynput.keyboard import Key, Controller
import pyautogui
keyboard = Controller()

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP))
height = int(cap.get(cv2.CAP_PROP))

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence = 0.8,
                       min_tracking_confidence = 0.5)

tipIds = [4, 8, 12, 16, 20]

state = None

# Define una función


global state

if hand


for lm_index in tipIds:
    # Obten la pos Y de la punta baja y pte baja
    finger_tip_y = landmarks[lm_index].y
    finger_bottom_y = landmarks[lm_index - 2].y

    # Revisa 
    if lm_index != 4 :
        if finger_tip_y < finger_bottom_y:
            fingers.append(1)
            #

        if finger_tip_y  > finger_bottom_y:
            fingers.append(0)

totalFingers = fingers.count(1)

# Reproduce o pausa un video

if totalFingers == 4:
    state = "Play"
if totalFingers == 0 and state == "Play":
    state = "Pause"
    keyboard.press(key.space)
    
# Adelanta o regresa el video
finger_tip_x = (landmarks[8].x)*width

if totalFingers == 1:
    if finger_tip_x < width-400:
        print("Regresar")
        keyboard.press(Key.left)
    if finger_tip_x > width-50:
        print("Adelantar")
        keyboard.press(Key.right)
# Aumenta o disminuye el volumen
finger_tip_y = (landmarks[8].y)*height
if totalFingers == 2:
    if finger_tip_y < height-250:
        print("Incrementar volumen")
        pyautogui.press("volumeup")
    if finger_tip_y > height-250:
        print("Disminuir volumen")
        pyautogui.press("volumedown")
# Define una funcion para
def drawHandLanmarks(image, hand_landmarks):
    # Establece conexiones entre ptos de referencia
    if hand_landmarks:
        for landmarks in hand_landmarks:
            mp_drawing.draw_landmarks(image, landmarks, mp_hands)
    while True:
        success, image = cap.read()
        image = cv2.flip(image, 1)
        # Detecta los ptos de referencia de las manos
        results = hands.process(image)
        # Obtén la posición del pto 
        hand_landmarks = results.multi_hand
