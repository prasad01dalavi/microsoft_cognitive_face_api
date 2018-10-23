# Microsoft Cognitive Face API
## Steps:

1. Create a Person Group

-- Where we will be storing faces of different people

2. Create Face in that Person Group

-- Creates face for each person

-- It generates a faceId to represent the person

3. Add face images in the created Face

-- Add face images of the person to the respective faceId created

-- More images will give us more accuracy. 

-- But also fine with only one image.

-- We will get persistedFaceId which will be representing the face images and will not expire


4. Train the Person Group

-- This will ultimately train the faces in that group 

-- We need to train only when we add or remove face in the created face


5. Test the Prediction (Face Identification)

a) We need to detect the face in the test image 

b) While detecting the face, we will get faceId(will expire in 24 hours) and the co-ordinates of face

c) We need to pass the face id in for face identification
