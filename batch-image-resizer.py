import cv2
import glob
import os.path


#Creates a list of files that has extension jpg, jpeg and png in the current dir.
jpg = glob.glob("*.jpg")
jpeg = glob.glob("*.jpeg")
png = glob.glob("*.png")
images = jpg + png + jpeg

#max image size in bytes
max_size = 2000000

for image in images:
    while True:
        if (os.path.getsize(image) > max_size):
            curr_img = cv2.imread(image, 1)
            
            #Keep the aspect ration
            re = cv2.resize(curr_img, (int(curr_img.shape[1]/1.5), int(curr_img.shape[0]/1.5)))
            cv2.imshow("checking", re)

            cv2.waitKey(500)
            cv2.destroyAllWindows()

            cv2.imwrite(image, re)
        else:
            break
