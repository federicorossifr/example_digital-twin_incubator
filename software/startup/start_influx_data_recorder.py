import time

from incubator.config.config import load_config, config_logger
from digital_twin.data_access.dbmanager.incubator_state_influx_recorder import IncubatorDataRecorderInflux


def start_influx_data_recorder(ok_queue=None):
    config_logger("logging.conf")
    config = load_config("startup.conf")

    recorder = IncubatorDataRecorderInflux()
    recorder.setup(rabbitmq_config=config["rabbitmq"], influxdb_config=config["influxdb"])

    if ok_queue is not None:
        ok_queue.put("OK")

    recorder.start_recording()


if __name__ == '__main__':
    while True:
        try:
            start_influx_data_recorder()
        except KeyboardInterrupt:
            exit(0)
        except Exception as exc:
            print("Error: ")
            print(exc)
            print("Attempting to reconnect...")
            time.sleep(1.0)
