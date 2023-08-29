# STADE-CDNet: Spatial-temporal attention with difference enhancement-based Network for remote sensing image change detection
## <img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/1%20(2).png" width="45" height="45">Requirements
<img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15">
                
                Python 3.8.0
                pytorch 1.10.1
                torchvision 0.11.2
                einops  0.3.2
                
<img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15">
## <img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/5.png" width="45" height="45">Installation
Clone this repo:
```python
git clone https://github.com/LiLisaZhi/STADE-CDNet.git cd STADE-CDNet

 ```

                
## <img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/7.png" width="45" height="45"> Dataset Preparation


```
"""
Change detection data set with pixel-level binary labels;
                ├─A
                ├─B
                ├─label
                └─list
"""
```
`A`:image of pro-image;
`B`:image of post-image;
`label`:label maps;
`list`:contains train.txt, val.txt and test.txt, each file records the image names (XXX.png) in the change detection dataset.

## <img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/66.png" width="45" height="45">Links to download processed datsets
- LEVIR-CD:[`click here to download`](https://justchenhao.github.io/LEVIR/)
- DSIFN-CD: [`click here to download`](https://github.com/GeoZcx/A-deeply-supervised-image-fusion-network-for-change-detection-in-remote-sensing-images/tree/master/dataset)
## <img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/7.png" width="45" height="45"> References 
Appreciate the work from the following repositories:
```
https://github.com/justchenhao/BIT_CD 
```
<img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15"><img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/33.png" width="15" height="15">
```
https://github.com/wgcban/ChangeFormer
```

(The code implementation of our STADE-CDNet method references these code repoistories)
## <img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/16.png" width="45" height="45"> Contact
<img src="https://github.com/Lilith-ZZZ/STADE-CDNet_V1/blob/main/image/55.jpg" width="25" height="25">lisa_zhi@foxmail.com

