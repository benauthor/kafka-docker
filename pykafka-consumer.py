import pykafka
import logging
import time

logging.basicConfig(level=logging.DEBUG)

client = pykafka.KafkaClient(hosts="kafka:9092",
                             zookeeper_hosts="zookeeper:2181")
topic = client.topics['test.topic']
consumer = topic.get_balanced_consumer("test.topic")

while True:
    try:
        got = consumer.consume(block=False)
        if got is None:
            logging.debug("waiting")
            time.sleep(0.3)
            continue

        logging.info(got.value)
    except Exception:
        logging.exception("bummer")
