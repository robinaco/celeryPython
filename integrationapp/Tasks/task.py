from celery import shared_task
from celery.utils.log import get_task_logger
import time
import requests
from integration_payment_provider.celery import app
import pika
import json
logger = get_task_logger(__name__)

app.conf.task_routes = {'Tasks.tasks.*': {'queue': 'celery'}}


@shared_task
def upload_payload(payload):
    time.sleep(5)


@shared_task(bind=False)
def consume_queue():

    connection_params = (pika.ConnectionParameters(host='localhost', 
                                                   port='5672',
                                                   virtual_host='/',
                                                   credentials=pika.
                                                   PlainCredentials
                                                   ('guest', 'guest')))
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Declarar la cola desde la que vas a consumir
    channel.queue_declare(queue='celery', durable=True)

    def callback(ch, method, properties, body):
        print("Received message: %r" % properties)
        # Aquí puedes procesar el mensaje o retornarlo
        # Vamos a retornar el cuerpo del mensaje para este ejemplo
        ch.basic_ack(delivery_tag=method.delivery_tag)

        return properties

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='celery', on_message_callback=callback)

    print('Waiting for messages...')
    channel.start_consuming()
