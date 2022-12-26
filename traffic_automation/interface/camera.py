import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        # self.video = cv2.resize(self.video,(840,640))
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
       
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
