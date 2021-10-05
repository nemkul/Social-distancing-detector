from .config import NMS_THRESH, MIN_CONF, People_Counter
import numpy as np
import cv2

def detect_people(frame, net, ln, personIdx=0):
	# grab the dimensions of the frame and  initialize the list of results
	(H, W) = frame.shape[:2]
	results = []

	# construct a blob from the input frame, perform a forward pass of the YOLO object detector
	blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
		swapRB=True, crop=False)
	net.setInput(blob)
	layerOutputs = net.forward(ln)

	# initialize our lists of detected bounding boxes, centroids, and confidences, respectively
	boxes = []
	centroids = []
	confidences = []

	for output in layerOutputs:
		for detection in output:
			scores = detection[5:]
			classID = np.argmax(scores)
			confidence = scores[classID]

			# filter detections by ensuring that the object detected was a person and that the minimum confidence is met
			if classID == personIdx and confidence > MIN_CONF:
				# scale the bounding box coordinates back relative to the size of the image
				box = detection[0:4] * np.array([W, H, W, H])
				(centerX, centerY, width, height) = box.astype("int")

				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))

				boxes.append([x, y, int(width), int(height)])
				centroids.append((centerX, centerY))
				confidences.append(float(confidence))

	# apply non-maxima suppression to suppress weak, overlapping bounding boxes
	idxs = cv2.dnn.NMSBoxes(boxes, confidences, MIN_CONF, NMS_THRESH)
	#print('Total people count:', len(idxs))
	# compute the total people counter
	if People_Counter:
		human_count = "Human count: {}".format(len(idxs))
		cv2.putText(frame, human_count, (470, frame.shape[0] - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.70, (0, 0, 0), 2)

	# ensure at least one detection exists
	if len(idxs) > 0:
		for i in idxs.flatten():
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])

			# update our results list 
			r = (confidences[i], (x, y, x + w, y + h), centroids[i])
			results.append(r)

	return results
