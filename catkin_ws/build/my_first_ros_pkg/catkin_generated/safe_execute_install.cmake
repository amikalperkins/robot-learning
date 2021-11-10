execute_process(COMMAND "/home/amikalperkins/git_workspace/robot-learning/catkin_ws/build/my_first_ros_pkg/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/amikalperkins/git_workspace/robot-learning/catkin_ws/build/my_first_ros_pkg/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
