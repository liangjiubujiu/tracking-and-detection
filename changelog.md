# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),


## [1.0.0] - 2020-01-22
### Added
- Model pretrained codes for the application of detectron2 and tooth dataset.
- Segmentation and Classification results with many errors are uploaded.
## Questions
- For each testing sample, the predicted categories are all **cat8**, however **cat7** is  the largest partial in the whole dataset.
- More than one predicted annotations are shown in one image.
### Todo
- compare the precision of train and val datasets.
- compare the visual performance of train and val datasets.
- Realize detection of category No.7.
If these compared performances have huge gaps, that means, the pretrained model is severely **overfitting**.  
Expercted intepretation:  
Considering that fix the model weights, that is only change the training and evaluated dataset, the focused performance change is related to data strongly. According to experience, complex models with small size and small quantity results in overfitting.

## [1.0.0] - 2020-01-22
### Added
- Realize detection for only one category. 
  The predicted categories are all **cat7** with accuracy **100%**, however all the sampled ground truth are **cat6**.  
  The predicted categories are all **cat8** with accuracy **100%**, however all the sampled ground truth are **cat7**.  
  The predicted categories are all **cat9** with accuracy **100%**, however all the sampled ground truth are **cat8**.  
  The predicted categories are all **cat10** with accuracy **100%**, however all the sampled ground truth are **cat9**.  
  But there is no annotaion**cat10**.
## Questions
- When changing the totoal quantity of data, the totoal time is fixed.  
-For each testing sample, the predicted categories are all **cat7**, however **cat6** is the largest partial in the whole dataset.
