# Social-Distancing-Detection

# Running Instructions
- Install all the required Python dependencies:

pip install -r requirements.txt

- If you would like to use GPU, set 'USE_GPU = True' in the config. options at 'mylib/config.py'.

- Note that you need to build OpenCV with CUDA (for an NVIDIA GPU) support first:

- Download the weights file from here (https://drive.google.com/file/d/1O2zmGIIHLX8SGs24W7mjRyFKvE_CSY8n/view?usp=sharing) and place it in the 'yolo' folder.
  Note that weights have been removed in this file to reduce size of folder.

- To run on a test video file, head into the directory/use the command:
python run.py --input mylib/videos/test.mp4 --output output1.avi --display 1

- To run on an IP camera, Setup your camera url in 'mylib/config.py':

# Enter the ip camera url (e.g., url = '')(Set url = 0 for webcam.)
- Then run with the command:
python run.py


