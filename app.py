from chalice import Chalice
import threading
import time
from datetime import datetime


app = Chalice(app_name='multithread-test')
app.debug = True


def run_thread(msg):
    app.log.debug(f"Call {msg} and sleep, timestamp {datetime.now()}")
    time.sleep(5)


@app.lambda_function(name='multithread-test')
def handler(event, context):
    thread_list = list()
    for i in range(0, 5):
        msg = f'thread-{i}'
        thread = threading.Thread(target=run_thread, args=(msg,))
        thread_list.append(thread)
        thread.start()

    for t in thread_list:
        t.join()

    return "Done!"
