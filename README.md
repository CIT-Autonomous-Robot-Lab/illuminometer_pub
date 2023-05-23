# illuminometer_pub

## Overview
ROSで照度計(IWS660-CS)を動かすためのパッケージです。

## 使用センサ
* [IWS660-CS](https://tokyodevices.com/items/228)

#### 仕様
|  |  |  |  |
| - | - | - | - |
| 項目 | 値 | 単位 | 説明 |
| 測定レンジ　最小 | 10 | lx |  |
| 測定レンジ　最大 | 100,000 | lx |  |
| 分解能 | 900 | ticks | 10～100,000lx に対して 900 段階で対数的変化 |
| 通信規格 |  |  | USB1.1 / HID プロファイル |
| 使用温度範囲 | -10~50 | ℃ |  |

## Build & Install
```
mkdir catkin_ws/src -p
git clone git@github.com:CIT-Autonomous-Robot-Lab/illuminometer_pub.git
cd catkin_ws
catkin build
source devel/setup.bash
```
## How to use
1. [td-usb](https://github.com/tokyodevices/td-usb)をcloneする。
2. td-usbの実行ファイルを``/usr/local/bin``に移動する。  
     ``sudo mv /path/to/td-usb /usr/local/bin/``
     
3. ``roslaunch illuminometer_pub illuminometer_pub.launch``
   
## Topic
|  |  |  |
| - | - | - |
| 名前 | 型 | 説明 |
| luminous_intensity | std_msgs::Float64 | iws660から照度をpublish |
