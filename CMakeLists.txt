cmake_minimum_required(VERSION 3.0.2)
project(illuminometer_pub)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)


catkin_package(
)


include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(talker src/illuminometer_pub.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
add_dependencies(talker ${catkin_EXPORTED_TARGETS})


