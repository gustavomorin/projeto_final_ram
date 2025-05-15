from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    nav2_bringup_dir = get_package_share_directory('nav2_bringup')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time', default_value='true',
            description='Use simulation time'
        ),
        DeclareLaunchArgument(
            'params_file',
            default_value=LaunchConfiguration('params_file'),
            description='Path to the Nav2 parameters YAML file'
        ),
        DeclareLaunchArgument(
            'map',
            default_value='/root/Projeto_Final/src/rm_localization/map/meu_mapa.yaml',
            description='Full path to map yaml file to load'
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
            ),
            launch_arguments={
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                'params_file': LaunchConfiguration('params_file'),
                'map': LaunchConfiguration('map')
            }.items()
        ),
    ])
