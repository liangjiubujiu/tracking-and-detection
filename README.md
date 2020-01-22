# Tracking and detection

several preliminary experiments for videl tracking task.

# Tracking
## Installation Requirements
* Linux (Ubuntu 18)
* Python ≥ 3.6
* Opencv-contrib-python > 4.1.0 recommended

Take CSRT algorithm as an example, run tracking.py with:

```
python tracking.py --video tracking.mp4 --algorithm CSRT
```
## Dataset 
Dataset is from [deep-dental-image](https://github.com/IvisionLab/deep-dental-image).


# Detection
All the preliminary experiments are based on pretrained models and opensource packages.
## Installation Requirements
* Cuda 10.1 [guidance 1](https://medium.com/@exesse/cuda-10-1-installation-on-ubuntu-18-04-lts-d04f89287130) [guidance 2](https://oldtang.com/2486.html) [guidance3](http://blog.jeffhaluska.com/adventures-in-installing-pytorch-in-ubuntu-18-04/).
* Facebook [detectron 2](https://github.com/facebookresearch/detectron2).
* Git [shape_to_coco](https://github.com/waspinator/pycococreator).

  tips:
  - Driver, cuda and pytorch should be matched perfectly. 
  ![version](/images/CUDAToolkitDocumentation.png)
  - Create new conda env to manage this repository.
```
conda create -n mypython3 python=3.6
conda activate mypython3
conda info --envs
conda list
conda deactivate
```
## Dataset
Git [tooth dataset](https://github.com/IvisionLab/deep-dental-image).
  
  
  
  
Ps: All therepository is made by the detailed markdown [guidance](https://guides.github.com/features/mastering-markdown/)
