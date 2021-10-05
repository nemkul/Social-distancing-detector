import cv2, threading, queue
 # Threading removes OpenCV's internal buffer and reduces the frame lag
class ThreadingClass:
  def __init__(self, name):
    self.cap = cv2.VideoCapture(name)
	# define an empty queue and thread
    self.q = queue.Queue()
    t = threading.Thread(target=self._reader)
    t.daemon = True
    t.start()

  # read the frames as soon as they are available, discard any unprocessed frames;
  def _reader(self):
    while True:
      (ret, frame) = self.cap.read() 
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()
        except queue.Empty:
          pass
      self.q.put(frame) # store them in a queue (instead of the buffer)

  def read(self):
    return self.q.get()