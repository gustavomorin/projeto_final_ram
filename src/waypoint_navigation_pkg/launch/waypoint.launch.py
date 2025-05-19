from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='waypoint_navigation_pkg',
            executable='waypoint_navigator',
            name='waypoint_navigator',
            output='screen'
        )
    ])