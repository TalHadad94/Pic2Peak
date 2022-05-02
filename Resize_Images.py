import os
import glob
import cv2

def resize_images(raw_dir,save_dir,ext,width,height):

    fnames = glob.glob(os.path.join(raw_dir, "*.{}".format(ext)))
    os.makedirs(save_dir, exist_ok=True)
    print("{} files to resize from directory `{}` to target size:{}".format(len(fnames), raw_dir, width, height))
    
    for i, fname in enumerate(fnames):
        print(".", end="", flush=True)
        img = cv2.imread(fname)
        img_small = cv2.resize(img, (width, height))
        new_fname = "{}.{}".format(str(i), ext)
        small_fname = os.path.join(save_dir, new_fname)
        cv2.imwrite(small_fname, img_small)
        
    print("\nDone resizing {} files.\nSaved to directory: `{}`".format(len(fnames), save_dir))

# resize_images('/content/data','/content/updateData','jpg',800,600)