import pika
import json


params = pika.URLParameters('amqps://pmziknme:f3cWxF4lPVoxG6UBBbEPHlySIXvZWMGN@cow.rmq2.cloudamqp.com/pmziknme')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='microservice', body=json.dumps(body), properties=properties)
