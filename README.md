# illuminometer_pub [![build-test](https://github.com/CIT-Autonomous-Robot-Lab/illuminometer_pub/actions/workflows/action.yml/badge.svg)](https://github.com/CIT-Autonomous-Robot-Lab/illuminometer_pub/actions)

## Overview
ROSで照度計(IWS660-CS)を動かすためのパッケージです。

## Requirement
* Ubuntu 20.04
* ROS noetic
## Sensor
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
1. ``apt install libusb-dev``を実行する。
2. [td-usb](https://github.com/tokyodevices/td-usb)をcloneする。
3. permissionを設定する。  
   ``/etc/udev/rules.d/99-usb-tokyodevices.rules``を作成し、以下の行を含むファイルを作成してください。
   ```
   SUBSYSTEM=="usb", ATTR{idVendor}=="16c0", ATTR{idProduct}=="05df", MODE="0666"
   ```
   16c0と05dfは、使用する必要があるデバイスの VID/PID に置き換えてください。
   
4. td-usbの実行ファイルを``/usr/local/bin``に移動する。  
     ``sudo mv /path/to/td-usb /usr/local/bin/``
     
5. ```
   roslaunch illuminometer_pub illuminometer_pub.launch
   ```
   
## Topic
|  |  |  |
| - | - | - |
| 名前 | 型 | 説明 |
| luminous_intensity | std_msgs::Float64 | iws660から照度をpublish |

## Author
  臼井温希  
  千葉工業大学 先進工学部 未来ロボティクス学科  
  kmmm13037@gmail.com

## Lincense
"illuminometer_pub" is under [Apache License 2.0](https://github.com/CIT-Autonomous-Robot-Lab/illuminometer_pub/blob/main/LICENSE)