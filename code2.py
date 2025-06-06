<gazebo reference="lider_1">
    <material>${body_color}</material>
    <mu1>0.2</mu1>
    <mu2>0.2</mu2>
    <selfCollide>true</selfCollide>
    <sensor name="lidar_sensor" type="ray">
      <pose>0.1 0.1 0 0 0 0</pose>
      <update_rate>20</update_rate>
      <ray>
        <scan>
          <horizontal>
            <samples>360</samples>
            <resolution>1</resolution>
            <min_angle>-1.5708</min_angle>
            <max_angle>1.5708</max_angle>
          </horizontal>
        </scan>
        <range>
          <min>0.12</min>
          <max>10.0</max>
          <resolution>0.01</resolution>
        </range>
      </ray>
      <plugin name="gazebo_ros_gpu_laser" filename="libgazebo_ros_laser.so">
        <topicName>/scan</topicName>
        <frameName>lider_1</frameName>
      </plugin>
    </sensor>
  </gazebo>

  <gazebo reference="camera_1">
    <material>${body_color}</material>
    <mu1>0.2</mu1>
    <mu2>0.2</mu2>
    <selfCollide>true</selfCollide>
    <sensor name="camera_sensor" type="camera">
      <pose>0 0 0 0 0 0</pose>
      <update_rate>30</update_rate>
      <camera>
        <horizontal_fov>1.047</horizontal_fov>
        <image>
          <width>640</width>
          <height>480</height>
          <format>R8G8B8</format>
        </image>
        <clip>
          <near>0.1</near>
          <far>100</far>
        </clip>
      </camera>
      <plugin name="gazebo_ros_camera" filename="libgazebo_ros_camera.so">
        <imageTopicName>/camera/image_raw</imageTopicName>
        <cameraName>camera_1</cameraName>
        <frameName>camera_1</frameName>
      </plugin>
    </sensor>
  </gazebo>



  <gazebo>
    <plugin name="differential_drive_controller" filename="libgazebo_ros_diff_drive.so">

      <!-- Plugin update rate in Hz -->
      <updateRate>100</updateRate>

      <!-- Name of left joint, defaults to `left_joint` -->
      <leftJoint>Revolute 2</leftJoint>

      <!-- Name of right joint, defaults to `right_joint` -->
      <rightJoint>Revolute 1</rightJoint>

      <!-- The distance from the center of one wheel to the other, in meters, defaults to 0.34 m -->
      <wheelSeparation>0.2</wheelSeparation>

      <!-- Diameter of the wheels, in meters, defaults to 0.15 m -->
      <wheelDiameter>0.1</wheelDiameter>

      <!-- Wheel acceleration, in rad/s^2, defaults to 0.0 rad/s^2 -->
      <wheelAcceleration>1.0</wheelAcceleration>

      <!-- Maximum torque which the wheels can produce, in Nm, defaults to 5 Nm -->
      <wheelTorque>50</wheelTorque>

      <!-- Topic to receive geometry_msgs/Twist message commands, defaults to `cmd_vel` -->
      <commandTopic>cmd_vel</commandTopic>

      <!-- Topic to publish nav_msgs/Odometry messages, defaults to `odom` -->
      <odometryTopic>odom</odometryTopic>

      <!-- Odometry frame, defaults to `odom` -->
      <odometryFrame>odom</odometryFrame>

      <!-- Robot frame to calculate odometry from, defaults to `base_footprint` -->
      <robotBaseFrame>base_link</robotBaseFrame>

      <!-- Odometry source, 0 for ENCODER, 1 for WORLD, defaults to WORLD -->
      <odometrySource>1</odometrySource>

      <!-- Set to true to publish transforms for the wheel links, defaults to false -->
      <publishWheelTF>true</publishWheelTF>

      <!-- Set to true to publish transforms for the odometry, defaults to true -->
      <publishOdom>true</publishOdom>

      <!-- Set to true to publish sensor_msgs/JointState on /joint_states for the wheel joints, defaults to false -->
      <publishWheelJointState>true</publishWheelJointState>

      <!-- Set to true to swap right and left wheels, defaults to true -->
      <legacyMode>false</legacyMode>
    </plugin>
  </gazebo>
