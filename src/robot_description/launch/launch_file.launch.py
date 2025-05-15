import launch
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Nós do workspace

    service_server_node = Node(
        package='ros_exercises',
        executable='move_robot_server',
        name='service_server_node',
        output='screen'
    )

    action_server_node = Node(
        package='ros_exercises',
        executable='move_robot_client',
        name='action_server_node',
        output='screen'
    )

    publisher_subscriber_node = Node(
        package='ros_exercises',
        executable='square',
        name='publisher_subscriber_node',
        output='screen'
    )

    # Incluir o launch file da APS1 (robot_simulation.py)
    aps1_launch_file = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('robot_description'),
                'launch',
                'robot_simulation.py'
            )
        )
    )

    return launch.LaunchDescription([
        service_server_node,
        action_server_node,
        publisher_subscriber_node,
        aps1_launch_file,
    ])
