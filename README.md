# Applied-ML-for-Manufacturing-Industrys-problem
Applied ML for Manufacturing Industry's problem Problem statement: Identification of Week Number on Cement Bags on running belt Problem Description :- We have to develop a Image processing Algorithm for Identification of Week number on Cement Bag on a running belt, Colour of Character is Black , Cement Bag colour may be black , White, Green, Yellow. In this algorithm if we found any bag without week no , we have put an entry in SQL database (Which will be utilized for stopping the Belt).

**Approach 1:**
Using Open CV :

https://user-images.githubusercontent.com/71602041/156870461-7791f879-db60-411f-b908-bfb99bb3f603.mp4

we have use tracker.py library which will trace our object(here cement bag) .
ROI is used here to detect selected portion of video which is only conveyor belt.
we have used mask to detect actual moving bag.
using contours we will remove small elements or error.


**Approach 2:**

https://drive.google.com/file/d/16XYHL4hAX2lp3D3GcPbZ0MQp1APrMsg7/view?usp=sharing

Features:

we have trained cnn model using more than 200+ images of cement bags.
we are using cnn model which can give result from the sequence of frames to which frame has proper cement bag and gives that frames. 
it also detects the text on the cement bag using ocr and prints the data in csv file.

dependencies:

Tensorflow
Keras
numpy
pandas
os
cv2
pytesseract
PIL
