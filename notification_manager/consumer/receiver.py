import json

import pika
import requests


def callback(ch, method, properties, body):
    email_data = json.loads(body)
    response = requests.post(
        url="http://email_service:8004/notification/send-email", json=email_data
    )

    print(f" [x] Email sent, response status: {response.status_code}", flush=True)

    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="rabbitmq", port=5672)
)
channel = connection.channel()

channel.queue_declare(queue="email_queue", durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="email_queue", on_message_callback=callback)

print(" [*] Waiting for tasks. To exit press CTRL+C", flush=True)
channel.start_consuming()
