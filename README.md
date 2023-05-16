# illuminometer_pub

## How to use
1. [td-usb](https://github.com/tokyodevices/td-usb)をcloneする。
2. td-usbの実行ファイルを``/usr/local/bin``に移動する。  
     ``sudo mv /path/to/td-usb /usr/local/bin/``
     
3. ``roslaunch illuminometer_pub illuminometer_pub.launch``
   
## Topic
|  |  |  |
| - | - | - |
| 名前 | 型 | 説明 |
| luminous_intensity | std_msgs::Float64 | iws660から反射強度(受光強度)をpublish |
