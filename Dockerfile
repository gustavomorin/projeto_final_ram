FROM osrf/ros:foxy-desktop

SHELL ["/bin/bash", "-c"]

# Instala pacotes ROS e dependências
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    ros-foxy-xacro \
    ros-foxy-navigation2 \
    ros-foxy-nav2-bringup \
    ros-foxy-nav2-msgs \
    ros-foxy-robot-localization \
    ros-foxy-tf2-tools \
    ros-foxy-gazebo-ros-pkgs \
    ros-foxy-rmw-cyclonedds-cpp \
    && rm -rf /var/lib/apt/lists/*

# Define implementação padrão do DDS
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

# Sourcing automático do ROS 2
RUN echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc

# Copia o workspace para dentro do container
COPY ./src /root/Projeto_Final/src

# Compila o workspace
WORKDIR /root/Projeto_Final
RUN source /opt/ros/foxy/setup.bash && colcon build

# Sourcing do ambiente do workspace
RUN echo "source /root/Projeto_Final/install/setup.bash" >> ~/.bashrc
