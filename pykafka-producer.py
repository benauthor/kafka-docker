import pykafka
import logging
import time
import datetime

logging.basicConfig()

client = pykafka.KafkaClient(hosts="kafka:9092")
topic = client.topics['test.topic']
producer = topic.get_producer()


while True:
    try:
        now = datetime.datetime.utcnow().isoformat()
        producer.produce(now)
        time.sleep(1)
        logging.info("published at %s" % now)
    except Exception:
        logging.exception("bummer")
