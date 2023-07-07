import rosbag
from std_msgs.msg import Float64
import sys

# コマンドライン引数からbag_file_pathを取得
if len(sys.argv) < 2:
    print("Usage: python average_luminous_intensity.py <bag_file_path>")
    sys.exit(1)
bag_file_path = sys.argv[1]

topic_name = "/luminous_intensity"

# メッセージの総数と合計値を初期化
count = 0
total_illumination = 0.0

# rosbagファイルを開く
bag = rosbag.Bag(bag_file_path)

# 指定したトピックのメッセージをイテレーション
for topic, msg, t in bag.read_messages(topics=[topic_name]):
    illumination = msg.data  # Float64メッセージのデータフィールドから値を取得
    total_illumination += illumination
    count += 1

# 平均値を計算
if count > 0:
    average_illumination = total_illumination / count
    rounded_illumination = round(average_illumination, 0)
    integer_illumination = int(rounded_illumination)
    print("Average Luminous Intensity:", integer_illumination)
else:
    print("No messages found on the", topic_name, "topic.")

# rosbagファイルを閉じる
bag.close()