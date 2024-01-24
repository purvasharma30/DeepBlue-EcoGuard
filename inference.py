from ultralytics import YOLO
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)
import torch
import cv2

labels = ['Mask', 'can', 'cellphone', 'electronics', 'gbottle', 'glove', 'metal', 'misc', 'net', 'pbag', 'pbottle',
        'plastic', 'rod', 'sunglasses', 'tire']

garbage = []
def detect(image):
    model = YOLO("/Users/chiya/Downloads/Underwater-Waste-Detection-Using-YoloV8-And-Water-Quality-Assessment-main/models/Underwater_Waste_Detection_YoloV8/60_epochs_denoised.pt")
    # results = model("C:\\Users\\Acer\\Documents\\Neural_Ocean\\Test_data\\test3.jpg")
    results = model(image)
    class_list = []
    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        class_list = boxes.cls.tolist()
    int_list = [int(num) for num in class_list]
    class_names = [labels[i] for i in int_list]
    garbage.extend(class_names)
    res_plotted = results[0].plot()
    return res_plotted, class_names

# cv2.imshow('res', res_plotted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()