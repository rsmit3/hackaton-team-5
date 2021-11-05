import os
from functools import lru_cache
from pydantic import BaseSettings
from loguru import logger

class Settings(BaseSettings):
    lidar_settings_key = 'lidar_settings'

    use_default = False
    lidar_settings = {}

    ADJUSTMENT_DEGREES = 0
    DISTANCE_CAR_HAS_TO_COME_CLOSER = 0
    ITERATIONS_CAR_HAS_TO_COME_CLOSER = 0
    START_RANGE_ANGLE_LOW = 0
    START_RANGE_ANGLE_HIGH = 0
    SEARCH_IN_BETWEEN_START = True
    START_RANGE_DISTANCE_LOW = 0
    START_RANGE_DISTANCE_HIGH = 0
    DATA_POINTS_TO_START = 0
    LENGTH_BACKLOG_START = 0
    NUMBER_ABOVE_THRESHOLD_TO_START = 0
    CLOSE_ENOUGH_THRESHOLD = 0
    VEHICLE_IN_GATE_RANGE_ANGLE_LOW = 0
    VEHICLE_IN_GATE_RANGE_ANGLE_HIGH = 0
    SEARCH_IN_BETWEEN_VEHICLE_IN_GATE = True
    VEHICLE_IN_GATE_RANGE_DISTANCE_LOW = 0
    VEHICLE_IN_GATE_RANGE_DISTANCE_HIGH = 0
    DATA_POINTS_VEHICLE_IN_GATE = 0
    SEARCH_IN_BETWEEN_DOOR_CLOSED = True
    DOOR_CLOSED_RANGE_ANGLE_LOW = 0
    DOOR_CLOSED_RANGE_ANGLE_HIGH = 0
    DOOR_CLOSED_RANGE_DISTANCE_LOW = 0
    DOOR_CLOSED_RANGE_DISTANCE_HIGH = 0
    DATA_POINTS_DOOR_CLOSED = 0
    SLEEP = 0
    USE_CARTESIAN_COORDINATES = True

    ys_and_xs = {}

    dmax: int = 800  # max distance of plot in MM
    imin: int = 0  # to make the plot
    imax: int = 50  # to make the plot

    postfix_mac = '.json'
    file_to_read = '../data/high_lidar_forwards_sample1_scanmode_2.json'  # if platform is mac fill this in
    percentage_cut_off_json_front = 0
    percentage_cut_off_json_end = 0

    file_to_visualize = '../data/LidarData.json'
    folder_to_save_plots = '../data/plots/'

    continue_lidar = False
    start_lidar = False
    end_lidar = False
    platform = 'jetson'

    use_continue = False
    use_end = False

    scan_mode = 2

    source_path = '/'.join(os.path.abspath(os.getcwd()).split('/')[:-1])
    path_to_save_test = os.path.join(source_path, 'output')
    test_description = 'test'

    class Config:
        """Location of the .env file."""

        env_file = ".env"


def retrieve_settings():
    settings = Settings()
    # settings.ADJUSTMENT_DEGREES = lidar_settings.get("adjustment_degrees", 352)  # 352
    # settings.DISTANCE_CAR_HAS_TO_COME_CLOSER = lidar_settings.get("distance_car_has_to_come_closer", 50)
    # settings.ITERATIONS_CAR_HAS_TO_COME_CLOSER = lidar_settings.get("iterations_car_has_to_come_closer", 5)
    # settings.START_RANGE_ANGLE_LOW = lidar_settings.get("start_range_angle_low", 0)
    # settings.START_RANGE_ANGLE_HIGH = lidar_settings.get("start_range_angle_high", 2000)
    # settings.SEARCH_IN_BETWEEN_START = lidar_settings.get("search_in_between_start", True)
    # settings.START_RANGE_DISTANCE_LOW = lidar_settings.get("start_range_distance_low", -5000)
    # settings.START_RANGE_DISTANCE_HIGH = lidar_settings.get("start_range_distance_high", -1300)
    # settings.DATA_POINTS_TO_START = lidar_settings.get("data_points_to_start", 10)
    # settings.LENGTH_BACKLOG_START = lidar_settings.get("length_backlog_start", 5)
    # settings.NUMBER_ABOVE_THRESHOLD_TO_START = lidar_settings.get("number_above_threshold_to_start", 4)
    # settings.CLOSE_ENOUGH_THRESHOLD = lidar_settings.get("close_enough_threshold", -3000)
    # settings.VEHICLE_IN_GATE_RANGE_ANGLE_LOW = lidar_settings.get("vehicle_in_gate_range_angle_low", 90)
    # settings.VEHICLE_IN_GATE_RANGE_ANGLE_HIGH = lidar_settings.get("vehicle_in_gate_range_angle_high", 315)
    # settings.SEARCH_IN_BETWEEN_VEHICLE_IN_GATE = lidar_settings.get("search_in_between_vehicle_in_gate", False)
    # settings.VEHICLE_IN_GATE_RANGE_DISTANCE_LOW = lidar_settings.get("vehicle_in_gate_range_distance_low", 500)
    # settings.VEHICLE_IN_GATE_RANGE_DISTANCE_HIGH = lidar_settings.get("vehicle_in_gate_range_distance_high", 1000)
    # settings.DATA_POINTS_VEHICLE_IN_GATE = lidar_settings.get("data_points_vehicle_in_gate", 150)
    # settings.SEARCH_IN_BETWEEN_DOOR_CLOSED = lidar_settings.get("search_in_between_door_closed", True)
    # settings.DOOR_CLOSED_RANGE_ANGLE_LOW = lidar_settings.get("door_closed_range_angle_low", -200)
    # settings.DOOR_CLOSED_RANGE_ANGLE_HIGH = lidar_settings.get("door_closed_range_angle_high", 2000)
    # settings.DOOR_CLOSED_RANGE_DISTANCE_LOW = lidar_settings.get("door_closed_range_distance_low", -1300)
    # settings.DOOR_CLOSED_RANGE_DISTANCE_HIGH = lidar_settings.get("door_closed_range_distance_high", -900)
    # settings.DATA_POINTS_DOOR_CLOSED = lidar_settings.get("data_points_door_closed", 100)
    # settings.SLEEP = lidar_settings.get('sleep', 5)
    # settings.USE_CARTESIAN_COORDINATES = lidar_settings.get('use_cartesian_coordinates', True)

    settings.ys_and_xs = {
        'start':
            {
                'in_between': settings.SEARCH_IN_BETWEEN_START,
                'y_low': settings.START_RANGE_ANGLE_LOW,
                'y_high': settings.START_RANGE_ANGLE_HIGH,
                'x_low': settings.START_RANGE_DISTANCE_LOW,
                'x_high': settings.START_RANGE_DISTANCE_HIGH
            },
        'vehicle_in_gate':
            {
                'in_between': settings.SEARCH_IN_BETWEEN_VEHICLE_IN_GATE,
                'y_low': settings.VEHICLE_IN_GATE_RANGE_ANGLE_LOW,
                'y_high': settings.VEHICLE_IN_GATE_RANGE_ANGLE_HIGH,
                'x_low': settings.VEHICLE_IN_GATE_RANGE_DISTANCE_LOW,
                'x_high': settings.VEHICLE_IN_GATE_RANGE_DISTANCE_HIGH
            },
        'door_closed':
            {
                'in_between': settings.SEARCH_IN_BETWEEN_DOOR_CLOSED,
                'y_low': settings.DOOR_CLOSED_RANGE_ANGLE_LOW,
                'y_high': settings.DOOR_CLOSED_RANGE_ANGLE_HIGH,
                'x_low': settings.DOOR_CLOSED_RANGE_DISTANCE_LOW,
                'x_high': settings.DOOR_CLOSED_RANGE_DISTANCE_HIGH
            }
    }

    return settings