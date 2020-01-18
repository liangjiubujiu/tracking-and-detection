import os
import random
import shutil

def getData(root,ratio,freeze=True):
    '''
    
    :param dirPath:  the current root path for dataset, it shows as follows
    :param ratio:    the ratio between the train parts and the whole data
    \train
        \annotations
            train2007.json
            val2007.json
        \images
            train
            val

    :return: a new val dataset that has the same orgazination 
                as the original train (dirpath) dataset.    
    the standard  namespace for all path is with '/' in the end of a string
                '''
    dirPath=root+'/coco_tooth/'#,todo
    subDirs = os.listdir(dirPath)#subDirs=[annos,imgs]
    subDirs = [i for i in subDirs if not ('.' in i)]#remove files rather directories in the file path list.
    catDirs = os.listdir(dirPath+subDirs[0])
    valDir = root+'/val/'
    trainDir = root+'/train/'
    #
    # todo
    if os.path.exists(valDir):
        shutil.rmtree(valDir)
    if os.path.exists(trainDir):
        shutil.rmtree(trainDir)
    os.mkdir(valDir)
    os.mkdir(trainDir)
    # for dir in subDirs:
    if subDirs[0]=='annotations':
        ann=subDirs[0]
    else:
        img=subDirs[0]
        ann=subDirs[1]

    val_ann_dir=valDir + ann + '/'
    val_img_dir = valDir + img + '/'

    train_ann_dir=trainDir+ ann+'/'
    train_img_dir=trainDir+ img+'/'

    dirPath_ann_dir=dirPath+ ann+'/'
    dirPath_img_dir=dirPath+img+'/'

    if not os.path.exists(val_ann_dir):
        os.mkdir(val_ann_dir)
        os.mkdir(val_img_dir)
    if not os.path.exists(train_ann_dir):
        os.mkdir(train_ann_dir)
        os.mkdir(train_img_dir)
    for catdir in catDirs:
        val_ann_tempDir=val_ann_dir+catdir+'/'
        val_img_tempDir=val_img_dir+catdir+'/'

        train_ann_tempDir=train_ann_dir+catdir+'/'
        train_img_tempDir=train_img_dir +catdir+'/'

        dirPath_ann_tempDir=dirPath_ann_dir+catdir+'/'
        dirPath_img_tempDir=dirPath_img_dir+catdir+'/'

        if not os.path.exists(val_ann_tempDir):
            os.mkdir(val_ann_tempDir)
            os.mkdir(val_img_tempDir)
        if not os.path.exists(train_ann_tempDir):
            os.mkdir(train_ann_tempDir)
            os.mkdir(train_img_tempDir)

        ans = os.listdir(dirPath_ann_tempDir)
        ind_list=[i for i in range(1,len(ans)+1)]

        if freeze:
            random.seed(4)#　get same results everytime calling the random shuffle function.
        random.shuffle(ind_list)
        le = int(len(ans) * ratio)  # 这个可以修改划分比例
        for f in ind_list[le:]:
            shutil.copy(dirPath_ann_tempDir + str(f)+'.bmp',val_ann_tempDir)
            shutil.copy(dirPath_img_tempDir + str(f) + '.jpg', val_img_tempDir)
        for f in ind_list[:le]:
            shutil.copy(dirPath_ann_tempDir + str(f)+'.bmp',train_ann_tempDir)
            shutil.copy(dirPath_img_tempDir + str(f) + '.jpg', train_img_tempDir)

root=os.getcwd()

ratio=0.8
getData(root,ratio)
