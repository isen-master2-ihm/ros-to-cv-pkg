import rclpy
from rclpy.node import Node

import sys 
import cv2

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
window_name = "POC"

class Image_converter(Node):

    def __init__(self):
        super().__init__('image_converter')
        self.image_pub = self.create_publisher(Image, 'output_image', 10)
        self.image_sub = self.create_subscription(Image, 'image_raw', self.image_processing, 10)
        
        self.bridge = CvBridge()
        
        self.image_sub
        
    def image_processing(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
            
    	# Convert to grayscale
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_classifier.detectMultiScale(gray, 1.15, 10)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(cv_image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        	
        # Display
        cv2.imshow(window_name, cv_image)
        cv2.waitKey(3)
        
        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
        except CvBridgeError as e:
            print(e)
      
            
            
def main(args=None):
    rclpy.init(args=args)
    
    ic = Image_converter()
    
    rclpy.spin(ic)
    
    minimal_subscriber.destroy_node()
    rclpy.shutdown()
    
    
if __name__ == '__main__':
    main()

