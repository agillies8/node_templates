# node_templates
example templates for python ROS nodes

* Creating a package:
  * Assumes you have ROS installed and have created a catkin_ws
  * http://wiki.ros.org/ROS/Tutorials/catkin/CreatingPackage

* Pulling code from github
  * Cd into new package
  * Git init
  * Git origin
  * Git pull
  * cd to catkin_ws && Catkin_make
  * Change file permissions: chmod +x for all python files in /src

* Publisher.py:
  * Review main components
  * Start roscore
  * Launch node
  * Run the node
  * Rostopic echo
  * Change message and observe
  * Add a counter publisher
  * Observe

* Subscriber.py:
  * Review main components
  * Start with publisher
  * Interrogate result
  * Add subscriber to int

* SubNpub.py:
  * Review main components
  * Start node
  * Publish int from command line: “rostopic pub number1 std_msgs/Int16 "1"”
  * View results

* create and use a ros service:
  * Create a service: http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv#Creating_a_srv
  * Create a service server and client: http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29
  * Run and examine

* Call an action server: http://wiki.ros.org/actionlib_tutorials/TutorialsReview the docs: http://wiki.ros.org/actionlib_tutorials/Tutorials
  * Review server: 
  * Review client:
  * Send message and wait for goal
  * Preempt a goal
