import person_group
import face

person_group_id = 'celebrities'
person_group_display_name = 'celebrities_group'

person1_name = "Angelina"
person2_name = "Mr.Bean"

person1_image = 'person1_image.jpg'
person2_image = 'person2_image.jpg'

person1a_image = 'person1a_image.jpg'
person1b_image = 'person1b_image.jpg'
person1c_image = 'person1c_image.jpeg'

# ---------------------------- Person Group --------------------------------- #

status = person_group.create(person_group_id, person_group_display_name)
print 'Group Creation Status:', status

status = person_group.info(person_group_id)
print 'Person Group Info:', status
"""
Output:
{"personGroupId":"celebrities","name":"celebrities_group","userData":null}
"""

# --------------------------------------------------------------------------- #


# -------------------------- Person Face - ---------------------------------- #

status = face.create(person_group_id, person1_name)
print 'Face Creation Status:', status
"""
Output:
{"personId":"65e13663-b189-4bd1-b470-37eb796ec9af"}
"""

status = face.create(person_group_id, person2_name)
print 'Face Creation Status:', status
"""
Output:
{"personId":"b9aae391-131e-4cda-9163-dfc3fe0341e7"}
"""

status = face.get_list(person_group_id)
print 'List of Faces in Group:', status
"""
Output:
[{"personId":"65e13663-b189-4bd1-b470-37eb796ec9af","persistedFaceIds":[],"name":"Angelina","userData":null},
{"personId":"b9aae391-131e-4cda-9163-dfc3fe0341e7","persistedFaceIds":[],"name":"Mr.Bean","userData":null}]
"""

person1_id = "65e13663-b189-4bd1-b470-37eb796ec9af"
status = face.add(person_group_id, person1_id, person1_image)
print 'Person Add Status:', status
"""
Output:
{"persistedFaceId":"ad0c4f99-5826-4916-adec-f6953b00cb30"}
"""

person2_id = "b9aae391-131e-4cda-9163-dfc3fe0341e7"
status = face.add(person_group_id, person2_id, person2_image)
print 'Person Add Status:', status
"""
Output:
{"persistedFaceId":"3f017d9b-d343-4896-93e6-492fa87e92e1"}

"""

# --------------------------------------------------------------------------- #


# ----------------------------- Training ------------------------------------ #

status = person_group.train(person_group_id)
print 'Train Response:', status

status = person_group.training_status(person_group_id)
print 'Training Status:', status
"""
Output:
{"status":"succeeded","createdDateTime":"2018-10-19T10:13:55.765508Z",
"lastActionDateTime":"2018-10-19T10:13:55.8717856Z","message":null}
"""

# --------------------------------------------------------------------------- #


# --------------------------- Testing --------------------------------------- #

image = open(person1c_image, 'rb').read()
status = face.detect(image)
print 'Face Detection Status:', status
"""
Output:
[{"faceId":"348a98ae-acd3-4b05-ae73-f5cf4d749819",
"faceRectangle":{"top":327,"left":268,"width":450,"height":450}}]
"""

detected_face_id = "348a98ae-acd3-4b05-ae73-f5cf4d749819"
status = face.identify(person_group_id, detected_face_id)
print 'Face Identification status:', status
"""
Output:
[{"faceId":"2e4ae129-9221-44ec-a496-7ed3739378a5",
"candidates":[{"personId":"0c434de7-0ad3-43c5-9440-90f2d4f27b81",
"confidence":1.0}]}]
"""

# --------------------------------------------------------------------------- #


# ------------------------- Delete Operations ------------------------------- #

person1_id = "0c434de7-0ad3-43c5-9440-90f2d4f27b81"
status = face.delete(person_group_id, person1_id)
print 'Delete Face status:', status

status = person_group.delete(person_group_id)
print 'Delete Person Group Status:', status

# ----------------------------------------------------------------------------#
