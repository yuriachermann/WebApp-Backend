import pika

params = pika.URLParameters('amqps://pmziknme:f3cWxF4lPVoxG6UBBbEPHlySIXvZWMGN@cow.rmq2.cloudamqp.com/pmziknme')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='backend')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='backend', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
