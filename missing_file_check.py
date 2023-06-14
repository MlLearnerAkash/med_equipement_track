import os
import glob
import ntpath
import shutil
import os

img_jpg_path = '/media/depak/BinariHDD/share/22-4-2023'
img_png_path = '/media/depak/BinariHDD/share/YOLODataset/images/all_images_22042023'
missing_file_dir= '/media/depak/BinariHDD/share/YOLODataset/images/missing_files_22042023'
COPY_MISSING_FILE = True
# Get list of all jpg files in first folder
jpg = sorted(glob.iglob(os.path.join(img_jpg_path, '*.jpg')))

# Loop through all jpg files in first folder and check if they exist in second folder
missing_num = 0
for img1 in jpg:
    fullname_jpg = ntpath.split(img1)[-1]
    img2 = os.path.join(img_png_path, fullname_jpg.replace('.jpg', '.png'))
    if not os.path.isfile(img2):
        print(f'{fullname_jpg} is missing in {img_png_path}')
        if COPY_MISSING_FILE:
            shutil.copyfile(os.path.join(img_jpg_path, fullname_jpg), os.path.join(missing_file_dir, fullname_jpg))
            shutil.copyfile(os.path.join(img_jpg_path, fullname_jpg.split('.')[0]+ '.json'), os.path.join(missing_file_dir, fullname_jpg.split('.')[0]+ '.json'))
            
        missing_num+=1

print("Total number of files missing is: ", missing_num)


