<launch>
  <!-- 1. 載入你的機器人 URDF/Xacro -->
  <param name="robot_description"
         command="$(find xacro)/xacro --inorder '$(find s1100853_description)/urdf/s1100853.xacro'"/>
  <node pkg="robot_state_publisher"
        type="robot_state_publisher"
        name="robot_state_publisher"
        output="screen">
    <param name="publish_frequency" value="50.0" />
  </node>

  <node pkg="tf"
        type="static_transform_publisher"
        name="tf_lidar"
        args="0 0 0 0 0 0 base_link lider_1 100"/>

  <!-- 4. Spawn 到 Gazebo -->
  <include file="$(find gazebo_ros)/launch/shapes_world.launch">
  </include>
  <node pkg="gazebo_ros" type="spawn_model" name="spawn_urdf" output="screen"
        args="-param robot_description -urdf -model s1100853 -x 0 -y 0 -z 0.1"/>
</launch>