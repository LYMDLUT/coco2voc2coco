from pycocotools.coco import COCO
import skimage.io as io
import matplotlib.pyplot as plt
import pylab, os, cv2, shutil
import os.path as osp
import numpy as np
import os

SelectedCats=['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train',
        'truck', 'boat', 'traffic_light', 'fire_hydrant', 'stop_sign',
        'parking_meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep',
        'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella',
        'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard',
        'sports_ball', 'kite', 'baseball_bat', 'baseball_glove', 'skateboard',
        'surfboard', 'tennis_racket', 'bottle', 'wine_glass', 'cup', 'fork',
        'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
        'broccoli', 'carrot', 'hot_dog', 'pizza', 'donut', 'cake', 'chair',
        'couch', 'potted_plant', 'bed', 'dining_table', 'toilet', 'tv',
        'laptop', 'mouse', 'remote', 'keyboard', 'cell_phone', 'microwave',
        'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
        'scissors', 'teddy_bear', 'hair_drier', 'toothbrush']



def showbycv(coco, img_prefix, img, classes, SelectedCats=None):

    annIds = coco.getAnnIds(imgIds=img['id'], iscrowd=None)
    anns = coco.loadAnns(annIds)
    objs = []
    count=0
    for ann in anns:
        name = classes[ann['category_id']]
        #if name in SelectedCats:
        if 'bbox' in ann:
            bbox = ann['bbox']
            #if ann['area']<16:
            if bbox[2]*bbox[3] <=4096 :
                xmin = int(bbox[0])
                ymin = int(bbox[1])
                xmax = int(bbox[2] + bbox[0])
                ymax = int(bbox[3] + bbox[1])
                #obj = [name, 1.0, xmin, ymin, xmax, ymax]
                #objs.append(obj)
                #TT = cv2.imread(os.path.join(img_prefix, img['file_name']))
                #cv2.rectangle(TT, (xmin, ymin), (xmax, ymax), (255, 0, 0))
                #cv2.putText(TT, name, (xmin, ymin), 3, 0.5, (0, 0, 255))
                #count=count+1
    #if count>0:
                I = cv2.imread(os.path.join(img_prefix, img['file_name']))
                I=I[ymin:ymax,xmin:xmax]
                biaoding="./train"
                #II=function_hconcat(TT, I)
                II=I
                #cv2.imshow("img", II)
                #cv2.waitKey(0) #0表示等待键盘按键
                #pathna=str(area[0])+"x"+str(area[1])
                #pathna1=os.path.join(biaoding,pathna)
                #pathna1 = os.path.join(biaoding,str(name))
                pathna1=os.path.join(biaoding,name)
                if not os.path.exists(pathna1):
                    os.makedirs(pathna1)
                img_out =pathna1
                filename=img['file_name'].split('.')[0]+"--"+name+"----宽x高-"+'{:.3f}'.format(bbox[0])+"x"+'{:.3f}'.format(bbox[1])+"--"+"面积is-"+'{:.2f}'.format(bbox[2]*bbox[3])+".png"
                cv2.imwrite(os.path.join(img_out,filename),II)

def catid2name(coco):
    classes = dict()
    for cat in coco.dataset['categories']:
        classes[cat['id']] = cat['name']
        # print(str(cat['id'])+":"+cat['name'])
    return classes

if __name__=="__main__":
    annFile = './annotations/instances_train2017.json'
    img_prefix='./train2017'
    coco = COCO(annFile)
    coco_catid2name = catid2name(coco)
    fig = plt.figure()
    plt.ion()  # matplotlib interactivate mode 当交互模式打开后，plt.show()不会阻断运行

    for img_id in coco.imgs:
        img=coco.imgs[img_id]
        # showimg(coco,img_prefix,img,SelectedCats)
        # 通多opencv交互显示图像和标注；按下键盘回车或者空格自动显示下一张图像
        # showbycv(coco,img_prefix,img,coco_catid2name,SelectedCats)
        # 通过matplotlib.pylot交互显示图像和标注；点击鼠标或者键盘自动显示下一张图像
        #showbyplt(coco, img_prefix, img, coco_catid2name, SelectedCats,fig=fig)
        showbycv(coco, img_prefix, img, coco_catid2name, SelectedCats)
    print("ok")
