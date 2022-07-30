import time
import random
import cv2
from keras.models import load_model
import numpy as np

def get_prediction():
    model = load_model('/Users/haoquanliu/Desktop/AiCore/converted_keras/keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    prediction = []
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows() 
    cap.release()
    if np.amax(prediction) == prediction[0][0]:
        return 'Rock'
    elif  np.amax(prediction) == prediction[0][1]:
        return 'Paper'
    elif np.amax(prediction) == prediction[0][2]:
        return 'Scissors'
    else:
        return 'nothing'

def get_computer_choice():
    list  = ['Rock', 'Paper', 'Scissors']
    return random.choice(list)

def get_user_choice():
    choice= get_prediction()
    return choice

def get_winner(computer_choice, user_choice):
    computer_win = (computer_choice == 'Rock' and user_choice == 'Scissor') or (computer_choice == 'Scissors' and user_choice == 'Paper') or (computer_choice == 'Paper' and user_choice == 'Rock')
    if computer_win:
        return 'computer'
    elif computer_choice == user_choice:
        return 'draw'
    else:
        return 'user'

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    
    print(get_winner(computer_choice, user_choice))
