import launch
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Nó do Servidor de Ação (responsável por girar o robô)
    rotation_server_node = Node(
        package='ros_exercises',
        executable='rotation_server',
        name='rotation_server_node',
        output='screen'
    )

    # Nó Principal (controla a navegação e chama a ação)
    main_node = Node(
        package='ros_exercises',
        executable='main_node',
        name='main_node',
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
        aps1_launch_file,
        rotation_server_node,
        main_node,
    ])
