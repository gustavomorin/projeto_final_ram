import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from custom_interfaces.srv import StartMission
import math

class WaypointNavigator(Node):
    def __init__(self):
        super().__init__('waypoint_navigator')

        self.waypoints = [
            [6.6349, 0.157894, 0.0],
            [6.6349, 5.77467, 3.14],
            [1.0, 1.0, 1.57]
        ]

        self.client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.service = self.create_service(StartMission, 'start_waypoints', self.start_callback)

    def start_callback(self, request, response):
        self.get_logger().info('Iniciando missão via custom service...')
        self.send_next_waypoint(0)
        response.success = True
        response.message = 'Missão iniciada com sucesso'
        return response

    def send_next_waypoint(self, index):
        if index >= len(self.waypoints):
            self.get_logger().info('Missão completa!')
            return

        x, y, yaw = self.waypoints[index]

        goal = NavigateToPose.Goal()
        goal.pose.header.frame_id = 'map'
        goal.pose.header.stamp = self.get_clock().now().to_msg()
        goal.pose.pose.position.x = x
        goal.pose.pose.position.y = y
        goal.pose.pose.orientation.z = math.sin(yaw / 2.0)
        goal.pose.pose.orientation.w = math.cos(yaw / 2.0)

        self.client.wait_for_server()
        send_goal_future = self.client.send_goal_async(goal)
        send_goal_future.add_done_callback(lambda fut: self.goal_response_callback(fut, index))

    def goal_response_callback(self, future, index):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().error(f'Goal {index+1} rejeitado')
            return
        self.get_logger().info(f'Goal {index+1} aceito.')
        goal_handle.get_result_async().add_done_callback(lambda res: self.result_callback(res, index))

    def result_callback(self, future, index):
        self.get_logger().info(f'Goal {index+1} alcançado.')
        self.send_next_waypoint(index + 1)


def main(args=None):
    rclpy.init(args=args)
    node = WaypointNavigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()