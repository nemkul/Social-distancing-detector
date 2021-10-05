MODEL_PATH = "yolo"
MIN_CONF = 0.3
NMS_THRESH = 0.3

""" Config options to set for real-time inference """
# To count the total number of people (True/False).
People_Counter = True

# Threading ON/OFF. Please refer 'mylib>thread.py'.
Thread = False

# Set the threshold value for total violations limit.
Threshold = 2

# Enter the ip camera url
url = '0'

# Turn ON/OFF the email alert feature.
ALERT = True

# Set mail to receive the real-time alerts. 
MAIL = 'jeevitesh611@gmail.com'

# Set if GPU should be used for computations; Otherwise uses the CPU by default.
USE_GPU = False

# Define the max/min safe distance limits (in pixels) between 2 people.
MAX_DISTANCE = 180
MIN_DISTANCE = 149

