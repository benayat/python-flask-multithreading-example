from flask import Flask, request
from redis import Redis
from rq import Queue

import time
from background_task import background_task

app = Flask(__name__)

q =Queue(connection=Redis())
print(q)

@app.route("/task")
def index():
    if request.args.get("n"):
        print("running task now")
        queueList={}
        for i in range (8):
            job = q.enqueue(background_task, request.args.get("n"), i)
            queueList[i]=(f"Task ({job.id}) added to queue at {job.enqueued_at}")
        return queueList

    return "No value for count provided"


app.run()