// SPDX-FileCopyrightText: 2023 Atsuki Usui <kmmm13037@gmail.com>
// SPDX-License-Identifier: Apache-2.0

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <ros/ros.h>
#include <std_msgs/Float64.h>

int main(int argc, char **argv) {
  ros::init(argc, argv, "td_usb_publisher");
  ros::NodeHandle nh;
  ros::Publisher pub =
      nh.advertise<std_msgs::Float64>("luminous_intensity", 1000);

  FILE *pipe = popen("td-usb iws660 get read --loop=500", "r");
  if (!pipe) {
    ROS_ERROR("Failed to execute command");
    return 1;
  }

  char buffer[128];
  while (fgets(buffer, 128, pipe)) {
    std::string str(buffer);
    double data = std::stod(str);
    std_msgs::Float64 msg;
    msg.data = data;
    pub.publish(msg);
    ROS_INFO("Published data: %f", data);
  }

  pclose(pipe);
  return 0;
}