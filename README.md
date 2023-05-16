# illuminometer_pub

## How to use
1. [td-usb](https://github.com/tokyodevices/td-usb)をcloneする。
2. ``roscore``起動
3. td-usbの中で``rosrun illuminometer_pub talker``を実行
   
## Topic
|  |  |  |
| - | - | - |
| 名前 | 型 | 説明 |
| luminous_intensity | std_msgs::Float64 | iws660から反射強度(受光強度)をpublish |

## やること
* どこでも実行できるようにする
* launchファイルを作る