from flask import Flask

import os
import s3
import producer

app = Flask(__name__)


@app.route('/')
def wake_up():
    server = os.environ.get('KAFKA_SERVER')
    topic = os.environ.get('KAFKA_TOPIC')
    # available_message = os.environ.get('KAFKA_AVAILABLE_MESSAGE') -- ?

    # aws_key = os.environ.get('AWS_ACCESS_KEY_ID')
    # aws_secret = os.environ.get('AWS_SECRET_ACCESS_KEY')
    # aws_bucket = os.environ.get('AWS_S3_BUCKET_NAME')

    # filesystem = s3.connect(aws_key, aws_secret)
    # s3.save_data(filesystem, aws_bucket, "Hello AIOPS")
    producer.publish_message(server, topic, 'available')
    return 'Hello World!'






if __name__ == '__main__':
    app.run()
