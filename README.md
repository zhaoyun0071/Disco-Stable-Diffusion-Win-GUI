# Disco-Diffusion-Local

基于 https://github.com/alembics/disco-diffusion  pyqt5做了初步的界面（后续还会更新），Windows 系统电脑可以，推荐6GB以上独显，30系列、20系列N卡最佳，A卡不支持。


## 下载
百度网盘: https://pan.baidu.com/s/190x0G3_O1F12iAIxpQaLSA  
提取码：dm4i

## 安装
### 解压
解压pic_disco.zip，生成pic_disco目录。
### 模型文件移动到指定目录
网盘里的models文件夹移动到pic_disco目录中；
vgg16-397923af.pth存到：C:\Users\Administrator\.cache\torch\hub\checkpoints 
注：可能目录前缀（有的是C:\Users\Administrator，有的是C:\Users\User）不一样，但都是用户目录下，创建\.cache\torch\hub目录即可。
## 打开软件
进入软件目录pic_disco，双击打开DD5.exe程序即可，软件界面如下所示：
 ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/1.png)
## 软件配置
### 作图配置
主目录pic_disco文件夹的ini.json就是作图配置文件，可以打开方式选择文本文档打开。如下图简单说明几个关键配置点：
  ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/2.png)
### 输出图片目录
pic_disco\images_out。

### 过程图片目录
pic_disco\progress.png，每几个step（频率可配置）更新一次图片。

## 显卡配置需求
可能需要至少6GB显存，以下为测试情况：
（1）	RTX2060 6G独显，图片尺寸256*512可行；
（2）	RTX1070 8G独显，250steps耗时预估2小时，图片尺寸1280*720；
（3）	RTX2070S 8G独显，450steps耗时预估16分钟，图片尺寸960*448；
（4）	RTX3090 24G独显，450steps耗时预估10分钟，图片尺寸1280*720。

## 常见错误
下面这些都是图片设置过大导致的爆显存，或者6GB以下的显卡：
（1）	Unable to find a valid cuDNN algorithm to run convolution
（2）	CUDA out of memory
（3） 生成的图是黑色的，一般1660以下的老显卡可能有此现象，也就是可能无法正常使用

## 联系我
 ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/%E6%89%AB%E7%A0%81_%E6%90%9C%E7%B4%A2%E8%81%94%E5%90%88%E4%BC%A0%E6%92%AD%E6%A0%B7%E5%BC%8F-%E6%A0%87%E5%87%86%E8%89%B2%E7%89%88.png)
