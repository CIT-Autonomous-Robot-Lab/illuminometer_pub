# illuminometer_pub

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
