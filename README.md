Disco-Diffusion-Local V3.0 + | [Disco-Diffusion-Local V2.0 +](./README_V2.md)


# Disco-Diffusion-Local V3.4

基于 https://github.com/alembics/disco-diffusion  pyside2做了界面（持续更新），Windows 系统电脑可以，推荐6GB以上独显，30系列、20系列N卡最佳，AMD显卡不支持。

# 1、下载

## V3.4下载

## 提供多种方式下载

（1）百度网盘链接：链接：https://pan.baidu.com/s/1B0g4MPFe_drP_hRjgEnKGg 提取码：95kh

（2）天翼网盘链接：https://cloud.189.cn/t/ZZ7vuyZrMvmm (访问码:7dn8)

（3）谷歌网盘链接：https://drive.google.com/drive/folders/1mBtw3oz9rCsQflt5xzDw08Z9VRMDoB_T?usp=sharing

## 后续更新将网盘里的V3.1或V3.2或更新版本的zip文件解压到主目录，运行对应版本exe就是最新版本了。

## V2.0 +用户过度到3.0用户注意，pic_disco.zip这个压缩包要重新下载最新的，因为架构有所改变，C盘用户文件夹下的vgg16-397923af.pth模型移动到models文件夹即可，models文件夹其他模型两个版本没有变化。

### 另外请注意：自己的C:\Users\User\AppData\Local\CrashDumps这个目录，有时候爆显存崩溃会遗留很大文件，删除即可，C:\Users\User\不同电脑不一样。


# 2、更新记录

## V3.4版本：2022-06-12  
1、图片转3D支持时长和摄像机位移设置，原图尺寸输出视频，清晰度更高；

2、AI高清放大，实测6G显存1920×1080的图用x4模型放大4倍也不会超显存了，因为可以设置tile_size（拼图大小）参数；

3、加入目前挺火的像素PIXEL DD绘画模式https://github.com/KaliYuga-ai/Pixel-Art-Diffusion ，这个模型占用显存不大，小显存诸如6G能上1200×600，参数设置里提供两种绘图Diffusion模型引擎选择，原版DD和像素版DD；

4、参数设置界面记忆上次拉伸界面，不同分辨率显示器不用每次都拉伸界面了；

5、加入use_secondary_model这个选项，如果关闭此选项，DD将使用常规（大型）扩散模型，开启此选项则使用二级模型更快且显存占用小–一位用户报告渲染速度提高了50%！然而，二次模型要小得多，可能会降低图像质量和细节；

6、加入clamp_max参数设置，clamp_max设置clamp grad的上限，数值范围0-0.3。默认0.05在图像中提供更平滑、更柔和的着色，但设置更高的值（0.15-0.3）可以提供有趣的对比度和活力。

## V3.3版本：2022-06-01  V3.3视频说明：https://www.bilibili.com/video/BV1aU4y197tW/

1、新增图片转3D模式，基于 https://github.com/vt-vl-lab/3d-photo-inpainting 项目，实现图片批量转换成3D效果的视频，支持jpg、png格式图片，图片转3D比较慢，耐心等待转换过程；

2、新增中译英翻译，文字描述旁边的中译英按钮即可实现；

3、加入关于软件界面，更加显得正式，哈哈。

## V3.2版本：2022-05-27

1、新增队列模式，也就是批量参数画图模式，此功能可以实设置诸如不同描述词，进行批量绘制，详情参见视频：https://www.bilibili.com/video/bv1ZZ4y1t7wW ；

2、eta默认值由0.5改为0.8，和官方保持一致；

3、参数设置界面的参考图设置、图像质量设置都加入到基本设置里，更方便高效设置；

4、参数设置界面整体配色更加护眼；

5、文字描述默认改为：a beautiful painting of winter, trending on artstation；

6、绘制图片轮数n_batches改为1；每轮中间保存数改为1；

7、增设项目名称，默认TimeToDisco，也就是原来图片的都会在软件目录【images_out/TimeToDisco】文件夹下，现在比如设置项目名称为【我的项目】，则图片都会保存软件目录【images_out/我的项目】文件夹下。


## V3.1版本：2022-05-20

1、加入开源AI超分辨率项目功能，此项目很优秀，可以对二次元、三次元图进行2~4倍高清放大，见主界面【AI高清放大】按钮，支持批量选择图片，在参数设置界面的【Real-ESRGAN画质增强】tab下可以设置放大倍数和模型选择；
调用项目：https://github.com/xinntao/Real-ESRGAN

2、skip_steps最大不能超过steps-1，防止有部分小伙伴设置steps和skip_steps相同导致不画图；

3、软件主界面的【生成】按钮改名为【开始AI作画】；

4、n_batches默认由5改为2，这样一套参数默认画两张图了；

5、默认图片尺寸由256×256修改为128×128；

6、加入主界面几个按钮的帮助提示；

7、更改软件图标，鸣谢图标设计者B站主页：https://space.bilibili.com/22936830/channel/series 。

## V3.0版本：2022-05-14

1、相比V2.0版本，引入新的内核架构，测试性能提升5%~10%；

2、上个版本爆显存的弹窗指示不够完善，删掉此功能，爆显存依然通过黑窗CUDA OUT OF MEMORY查看；

3、启动时，黑窗的引起误会的warning去除掉了；

4、简化V2.0版本的安装要求，将移动到C盘用户文件夹下的vgg16-397923af.pth模型，也归属到models文件夹，现在安装就很简单了，两部操作：解压到pic_disco文件夹；models文件夹移动到pic_disco文件夹即可完成安装。


# 3、安装（视频教程1分钟后开始：https://www.bilibili.com/video/BV1aU4y197tW ）
## 解压
解压pic_disco.zip，生成pic_disco目录，不要解压到C盘。
## 模型文件移动到指定目录
网盘里的models文件夹移动到pic_disco目录中；

## 打开软件
进入软件目录pic_disco，双击打开DD5_V3.0程序即可，软件界面如下所示
：
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

## 停止绘图
目前没有实现停止绘图功能，主要是显存没有释放干净，关闭黑窗，就关闭软件，释放显存了，然后重新打开软件即可。

# 4、显卡配置需求
可能需要至少6GB显存，以下为测试情况：

（1）	RTX2060 6G独显，图片尺寸256x512可行；

（2）	RTX1070 8G独显，250steps耗时预估2小时，图片尺寸1280x720；

（3）	RTX2070S 8G独显，450steps耗时预估16分钟，图片尺寸960x448；

（4）	RTX3090 24G独显，450steps耗时预估10分钟，图片尺寸1280x720。


注：默认参数因为选了3个CLIP模型，如果想要尺寸更大，少选几个模型即可，但效果肯定有所影响，诸如6G独显的2060显卡，之选如下第一个模型，尺寸768×512都没问题：

  ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/clip.png)

# 5、常见错误
下面这些都是图片设置过大导致的爆显存，或者6GB以下的显卡：

（1）	Unable to find a valid cuDNN algorithm to run convolution


（2）	CUDA out of memory


（3） 生成的图是黑色的，目前发现的1060、1660、1660ti都有问题，原因是中途生成NAN数据，解决方案正在寻找。



# 6、离线版生成图展示

下均是网友利用离线版V2.0+版本生成的图，供各位参考：

（1）默认参数下，仅尺寸改为1280×720，RTX3090生成

  ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/1.jpg)
  
（2）默认参数下，仅尺寸改为768×448，RTX3070-8G独显笔记本版生成

  ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/12.jpg)


（3）默认参数下，仅尺寸改为1280×512，RTX3090生成

  ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/122.jpg)

（4）默认参数下，仅尺寸改为1280×512，RTX3090生成

  ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/3.jpg)


# 7、联系我

 ![image](https://github.com/zhaoyun0071/Disco-Diffusion-Local/blob/main/images/扫码_搜索联合传播样式-标准色版.png)
