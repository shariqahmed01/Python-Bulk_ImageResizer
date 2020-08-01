from PIL import Image, ImageOps
import cv2
import glob
# Required Size of the image
desired_size = 1024
# For png or other image extensions replace .jpg
images=glob.glob("*.jpg")
for image in images:

    im = cv2.imread(image)
    old_size = im.shape[:2] # old_size is in (height, width) format
    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    # new_size should be in (width, height) format
    im = cv2.resize(im, (new_size[1], new_size[0]))

    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)

    color = [255, 255, 255]
    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
        value=color)

    cv2.imwrite("resized_"+image, new_im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
