# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),


## [1.0.0] - 2020-01-22
### Added
- Model pretrained codes for the application of detectron2 and tooth dataset.
- Segmentation and Classification results with many errors are uploaded.

### Todo
- compare the precision of train and val datasets.
- compare the visual performance of train and val datasets.
If these compared performances have huge gaps, that means, the pretrained model is severely **overfitting**.  
Expercted intepretation:  
Considering that fix the model weights, that is only change the training and evaluated dataset, the focused performance change is related to data strongly. According to experience, complex models with small size and small quantity results in overfitting.


