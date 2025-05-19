from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory



def generate_launch_description():
    rm_localization_dir = get_package_share_directory('rm_localization')
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(rm_localization_dir, 'launch', 'amcl.launch.py')
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(rm_localization_dir, 'launch', 'ekf.launch.py')
            )
        ),
    ])
