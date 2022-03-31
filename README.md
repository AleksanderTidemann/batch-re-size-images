<<<<<<< HEAD
# Batch re-size your images 

Oh, how annoying size limitations on image uploads are.. This script re-sizes (almost) all types of images until they are within a certian size threshold. The script favors correct aspect ratios over precice image sizes. However, you can easily override this by changing ```cv2.resize(curr_img, (int(curr_img.shape[1]/1.5), int(curr_img.shape[0]/1.5)))``` to something like ```cv2.resize(curr_img, (800, 600))```. You can also keep the aspect ratio and get closer to the size threshold by changing the division calculation in ```curr_img.shape[0]/1.5``` to something like ```curr_img.shape[0]/1.1```, or something.. 

NB the script will delete the original images.. This can be avoided by adding custom image names to the ```cv2.imwrite(image, re)```.


Enjoy!
=======
# Batch re-size your images 

Oh, how annoying size limitations on image uploads are.. This script re-sizes (almost) all types of images until they are within a certian size threshold. The script favors correct aspect ratios over precice image sizes. However, you can easily override this by changing ```cv2.resize(curr_img, (int(curr_img.shape[1]/1.5), int(curr_img.shape[0]/1.5)))``` to something like ```cv2.resize(curr_img, (800, 600))```. You can also keep the aspect ratio and get closer to the size threshold by changing the division calculation in ```curr_img.shape[0]/1.5``` to something like ```curr_img.shape[0]/1.1```, or something.. 

Enjoy!
>>>>>>> 273952cc477e19d1617ee216e1184aab8d385d52
