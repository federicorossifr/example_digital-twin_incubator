from config.config import load_config, config_logger
from digital_twin.models.physical_twin_models.physical_twin_simulator4 import PhysicalTwinSimulator4Params

def start_simulator(ok_queue=None):
    config_logger("logging.conf")
    config = load_config("startup.conf")
    simulator = PhysicalTwinSimulator4Params(rabbitmq_config=config["rabbitmq"], influxdb_config=config["influxdb"])

    simulator.setup()

    if ok_queue is not None:
        ok_queue.put("OK")

    simulator.start_serving()


if __name__ == '__main__':
    start_simulator()
