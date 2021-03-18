# node_templates
example templates for python ROS nodes

* Creating a package:
  * Assumes you have ROS installed and have created a catkin_ws
  * http://wiki.ros.org/ROS/Tutorials/catkin/CreatingPackage

* Pulling code from github
  * Cd into new package you created above
  * enter: git clone https://github.com/agillies8/node_templates
  * cd to catkin_ws && Catkin_make
  * Change file permissions: chmod +x for all python files in /src

* publisher.py:
  * Review main components
  * Start roscore
  * run the node: rosrun node_templates publisher.py
  * Rostopic echo mymessage in new terminal
  * Change message and observe
  * Add a counter publisher
  * Observe as above with rostopic echo

* subscriber.py:
  * Review main components
  * make sure roscore is still running
  * run the publisher as above
  * run the subscriber: rosrun node_templates subscriber.py
  * Interrogate result
  * Add int to subscriber

* SubNpub.py:
  * Review main components
  * Start node
  * Publish int from command line: “rostopic pub number1 std_msgs/Int16 "1"”
  * View results

* create and use a ros service:
  * Create a service: http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv#Creating_a_srv
  * Create a service server and client: http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29
  * Run and examine:
    * rosrun node_templates serviceServer.py
    * rosrun node_templates serviceClient.py 2 3

* Call an action server: http://wiki.ros.org/actionlib_tutorials/TutorialsReview the docs: http://wiki.ros.org/actionlib_tutorials/Tutorials
  * Review server: 
  * Review client: http://docs.ros.org/en/jade/api/actionlib/html/classactionlib_1_1simple__action__client_1_1SimpleActionClient.html
  * Send message and wait for goal
  * Preempt a goal
  * interrogate an action while is is executing
