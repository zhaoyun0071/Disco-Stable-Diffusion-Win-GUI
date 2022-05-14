
Disco-Diffusion-Local V2.0 + | [Disco-Diffusion-Local V3.0 +](./README_V3.0.md)

# Disco-Diffusion-Local V2.8

基于 https://github.com/alembics/disco-diffusion  pyside2做了界面（持续更新），Windows 系统电脑可以，推荐6GB以上独显，30系列、20系列N卡最佳，A卡不支持。

# 1、下载
## V2.8下载
链接：https://pan.baidu.com/s/1xOmJER8YnPMPECPQw4JU9w 
提取码：f78y

将网盘里的V2.1或V2.2或更新版本的exe文件拷贝到解压的主目录，另外settings.json这个文件最好要拷贝到主目录覆盖原先文件，以免发生bug，运行对应版本exe就是最新版本了：

### 另外请注意：自己的C:\Users\User\AppData\Local\CrashDumps这个目录，有时候爆显存崩溃会遗留很大文件，删除即可，C:\Users\User\不同电脑不一样。


# 2、更新记录

## V2.8版本：

1、修复cut_ic_pow参数设置小数保存崩溃的bug；

2、修复skip_augs、randomize_class、clip_denoised、clamp_grad参数设置无法保存的bug；

3、修复佩林噪声开启后，重启软件参数设置变灰的bug；

4、加入推荐教程链接的按钮，为新人使用此软件带带路，在线文档链接逐步完善中；

5、中途预览图片，比例按照实际图片比例显示。


## V2.7版本：

1、加入检测更新功能，可以检测当前版本是否最新，调用的GitHub项目地址；

2、cut_innercut、cut_overview、cut_icgray_p这三个参数加入输入格式错误防呆提示；

3、gobig模式设置界面搭建好，但功能还没实现，有些坑要填( ╯□╰ )。

## V2.6版本：

1、修复种子seed设置范围，原先的范围少一倍，修改为0~2^32与官方一致；

2、继续修复2K、4K屏幕设置界面显示不全的问题，主要修复输入框的宽度；

3、增加显卡不支持弹窗，详细的提示信息及解决方案；

4、加入图片尺寸最小64*64保护；

5、加入显存不足的弹窗提示；

6、修复少数电脑识别码改变导致重新激活的bug。

## V2.5版本：

1、修复sat_scale、clip_guidance_scale参数上下限错误；

2、修复2K、4K屏幕设置界面显示不全的问题，现在可以调节窗口大小，不过我没有高分辨率屏，可能还有问题；

3、修复激活码输入多空格的防呆设定，现在激活码多个空格不会报错。

## V2.4版本：

1、修复init_scale上限2000的错误，应该为20000。

## V2.3版本：

1、修复描述词特殊字符导致闪退的bug。

## V2.2版本：

1、修复激活识别码识别不到的bug。

## V2.1版本：

1、加入seed种子在软件下方显示；

2、加入参考图的选择、清除功能；

3、修改和官方参数不一致的两个默认参数；

4、加入激活失败弹窗、复制成功弹窗。


# 3、安装
## 解压
解压pic_disco.zip，生成pic_disco目录，不要解压到C盘。
## 模型文件移动到指定目录
网盘里的models文件夹移动到pic_disco目录中；
vgg16-397923af.pth存到：C:\Users\Administrator\.cache\torch\hub\checkpoints 
注：可能目录前缀（有的是C:\Users\Administrator，有的是C:\Users\User）不一样，但都是用户目录下，创建\.cache\torch\hub目录即可。
## 打开软件
进入软件目录pic_disco，双击打开DD5_V2.0程序即可，软件界面如下所示：
 ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/1.png)
## 软件配置

拥有详细的界面化设置，仅针对静图。
 ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/set1.png)
  ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/set2.png)
   ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/set3.png)
    ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/set4.png)

## 输出图片目录
pic_disco\images_out。

## 过程图片目录
pic_disco\progress.png，每几个step（频率可配置）更新一次图片。

# 4、显卡配置需求
可能需要至少6GB显存，以下为测试情况：
（1）	RTX2060 6G独显，图片尺寸256x512可行；
（2）	RTX1070 8G独显，250steps耗时预估2小时，图片尺寸1280x720；
（3）	RTX2070S 8G独显，450steps耗时预估16分钟，图片尺寸960x448；
（4）	RTX3090 24G独显，450steps耗时预估10分钟，图片尺寸1280x720。

# 5、常见错误
下面这些都是图片设置过大导致的爆显存，或者6GB以下的显卡：
（1）	Unable to find a valid cuDNN algorithm to run convolution
（2）	CUDA out of memory
（3） 生成的图是黑色的，一般1660及以下的老显卡可能有此现象，原因未知，也就是可能无法正常使用

# 6、联系我
 ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/3.jpg)
