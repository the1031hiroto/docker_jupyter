# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'home/jovyan'))
	print(os.getcwd())
except:
	pass
#%%
import cv2
import matplotlib.pyplot as plt
import glob
from IPython.display import display, Image

def check_img_shape(img):
    # 画像を読み込んでリサイズする
    img1 = cv2.imread(img)
    img2 = cv2.imread(img)
    forcrop = cv2.imread(img)

    plt.subplot(1,4,1)
    plt.imshow(img1)

    # グレースケールにする
    gray = cv2.cvtColor(img1 ,cv2.COLOR_BGR2GRAY)

    # ブラーと２値化
    gray = cv2.GaussianBlur(gray,(7,7),0)
    im2 = cv2.threshold(gray, 170,240,cv2.THRESH_BINARY_INV)[1]

    # 二値化した画像を左にプロット
    plt.subplot(1,4,2)
    plt.imshow(im2,cmap="gray")

    #輪郭を検出
    cnts = cv2.findContours(im2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[0]

    for cnt in cnts:
        x,y,w,h = cv2.boundingRect(cnt)
        # 幅が40以下のものをスキップ
        if w < 40:
            continue

        # crop the image
        cropped = forcrop[y:(y + h), x:(x + w)]
        cv2.drawContours(img1, cnt, -1, (0, 0, 225), 2)  # contour

        # 輪郭の近似
        epsilon = 0.001 * cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        cv2.drawContours(img2, [approx], -1, (0, 255, 0), 3)

    # 輪郭抽出の結果を右にプロット
    plt.subplot(1,4,3)
    plt.imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
    plt.subplot(1,4,4)
    plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB))
    plt.show()

imgs = glob.glob(os.getcwd() + "/img/*.png")

for img in imgs:
    check_img_shape(img)



# %%
