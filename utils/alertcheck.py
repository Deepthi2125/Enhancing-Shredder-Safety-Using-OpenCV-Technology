import cv2
from playsound import playsound
import pandas as pd

#crossed=0

def drawboxtosafeline(image_np,p1,p2,Line_Position2,Orientation):
    
    #global crossed 
    if(Orientation=="bt"):
     bounding_mid=(int((p1[0]+p2[0])/2),int(p1[1]))   
     if(bounding_mid):
         cv2.line(img=image_np, pt1=bounding_mid, pt2=(bounding_mid[0],Line_Position2), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
         distance_from_line=bounding_mid[1]-Line_Position2
    elif(Orientation=="tb"):
     bounding_mid=(int((p1[0]+p2[0])/2),int(p2[1]))   
     if(bounding_mid):
         cv2.line(img=image_np, pt1=bounding_mid, pt2=(bounding_mid[0],Line_Position2), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
         distance_from_line=Line_Position2-bounding_mid[1]
    elif(Orientation=="lr"):
     bounding_mid=(int(p2[0]),int((p1[1]+p2[1])/2))   
     if(bounding_mid):
         cv2.line(img=image_np, pt1=bounding_mid, pt2=(Line_Position2,bounding_mid[1]), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
         distance_from_line=Line_Position2-bounding_mid[0]     
    elif(Orientation=="rl"):
     bounding_mid=(int(p1[0]),int((p1[1]+p2[1])/2))
     if(bounding_mid):
         cv2.line(img=image_np, pt1=bounding_mid, pt2=(Line_Position2,bounding_mid[1]), color=(255, 0, 0), thickness=1, lineType=8, shift=0)
         distance_from_line=bounding_mid[1]-Line_Position2
    
    if (distance_from_line <= 0) :
            
             #crossed+=1
             posii=int(image_np.shape[1]/2)        
             cv2.putText(image_np, "ALERT", (posii, 50),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0,0), 2)
			 #sound = os.path.join()
             playsound(r"C:\Users\NARLA DINATH REDDY\PycharmProjects\hand_detection\utils\emergency-alarm.wav")
             cv2.rectangle(image_np, (posii-20,20), (posii+85,60), (255,0,0), thickness=3, lineType=8, shift=0)
             #to write into xl-sheet            
             return 1
    else:
        return 0
    
   


