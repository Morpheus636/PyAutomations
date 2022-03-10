from threading import Thread
from typing import Callable
import os

import werkzeug.datastructures
import flask


app = flask.Flask("")
webhooks = {}


@app.route("/")
def home():
    return "Web Server Online and pinging"


def call_job_func(job_func):
    t = Thread(target=job_func, args=[flask.Request.args])
    t.start()


@app.route(f"/{os.environ['WEBHOOK_PREFIX']}/<webhook_name>")
def run_job_func(webhook_name):
    try:
        job_func = webhooks[webhook_name]
        t = Thread(target=job_func, args=[flask.request.args])
        t.start()
        return "200 - OK"
    except KeyError:
        flask.abort(404)


def create_webhook(name: str, job_func: Callable[[werkzeug.datastructures.MultiDict], None]) -> None:
    """Creates a webhook with path /$WEBHOOK_PREFIX/name, which calls job_func in a thread when accessed.

    :param name: The name of the webhook. Used in creating the route (/$WEBHOOK_PREFIX/name)
    :param job_func: The function to call (in a thread) when the webhook is accessed. Must take a MultiDict
    from flask.Request.args as it's only argument.
    :return: None
    """
    global webhooks
    webhooks[name] = job_func


def start():
    t = Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 8080})
    t.start()
