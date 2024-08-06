from vision.Zed_Wrapper import Zed
import cv2
import os
from datetime import datetime

'''
Joshua Van Doren & Joe Lofrese
2/26/2023
Display video data from zed with opencv and save images to a user defined folder
Have ZED SDK and its python-api installed
pip install opencv-python
'''

#save image
def save_image(image, image_label, folder_path):
    img_path = os.path.join(folder_path, str(image_label) + ".jpg")
    cv2.imwrite(img_path, image)
    print(f"Image number {image_label} is now stored in {folder_path}")


def main():
    zed = Zed()
    zed.open()
    
    folder_path = "datasets/"  # these folder placeholder formats are correct


    frame_counter = 0
    saving_interval = 0  #frame interval of images being taken when mode is activated
    video_mode = "video"
    image_label = len(os.listdir(folder_path))
    video_output = cv2.VideoWriter(str(len(os.listdir(folder_path))) + '.avi', -1, 20.0, (640,480))
    cam = "color"
    image_iteration = 0



    while True:
        # create image objesct
        if cam == "color":
            image = zed.get_color_image()
        else:
            image = zed.get_depth_image()
        cv2.imshow("Zed-Cam", image)

        # wait for user to press 'c' or 't' key to capture image or 'q' key to quit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c') and video_mode == "single":
            #capture single image
            save_image(image, image_label, folder_path)
            image_label += 1
        if key == ord("m") and video_mode != "video":
            #change video_mode
            video_mode = "video"
            saving_interval = int(input("Enter the frame interval for image capture: "))
            print(f"video_mode set to {video_mode} with frame interval of {saving_interval}")
        elif key == ord("m") and video_mode != "single":
            video_mode = "single"
            print(f"video_mode set to {video_mode}")
        elif video_mode == "video" and image_iteration % saving_interval == 0:
            save_image(image, image_label, folder_path)
            image_label += 1
            print(f"Image number {image_label} is now stored in {folder_path}")
        image_iteration += 1
        if key == ord("v"):
            video_mode == "true_video"
            video_output.write(image)
        
        if key == ord("d"):
            if cam == "color":
                cam = "depth"
                print("Switching to depth camera")
            else:
                cam = "color"
                print("Switching to color camera")

        # quit
        elif key == ord('q'):
            print("Closing window")
            # user has quit, release camera and close display window
            cv2.destroyAllWindows()
            zed.close()
            break
            frame_counter += 1

if __name__ == "__main__":
    main()