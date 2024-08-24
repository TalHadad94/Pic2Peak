© 2024 Tal. All rights reserved.

This project is licensed under the MIT License - see the LICENSE file for details.

# Pic2Peak

Artificial intelligence system called "Pic2Peak". This system knows how to turn a two-dimensional landscape image into a three-dimensional environment. Using CNN model of TensorFlow, Python, and Blender.

![image](https://user-images.githubusercontent.com/93497035/180607993-0e301b94-9cae-4154-9cd6-c0d8a53423fc.png)
![image](https://user-images.githubusercontent.com/93497035/180607995-015f159b-c241-4788-a419-115db04e953e.png)
![image](https://user-images.githubusercontent.com/93497035/180608000-1599e287-57e8-4ad2-896f-b0661c4cba6a.png)

* For more information you can download "Pic2Peak Project Book" from this repository, and read it (written in Hebrew).

# How to use Pic2Peak (From this repository):
1) Open "ImageDetectedPic2Peak.ipynb" and run it on Google Colab. This code do Image detection on picture from URL addresses. And generete for you at the end CSV file with all the data that the model found.

* We upload the result file to this repository, You can open "DataTable.csv" and see the output CSV file.
* For customization: Replace "image_urls" (In [21]) to your image URL and select it when "detect_img" (In [22]) is running.
  
2) For this part you will need Blender on your computer - https://www.blender.org/. In Blender open a "Text Editor" window and copy "Pic2PeakForBlender.py" to it. make sure that the path to the CSV file is correct (line 23). then you can run it from "Run Script" button in the window, and the environment will be built.
