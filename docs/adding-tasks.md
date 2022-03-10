# How to add automations
Automations, or "tasks", live in python files in the src/morphtomations/tasks/ directory. 
All python files in that directory will be imported when the program is started. 

## Scheduled tasks
Creating scheduled tasks is baked-in already. Use the `schedule` package to create the scheduled task, and
`__main__.py` will run it when it's time.
### Example: 
```python
import schedule

def myfunc():
    print("I want to run every 10 minutes!")

schedule.every(10).minutes.do(myfunc)
```

For best results, use `utils.run_threaded()` to run the automation in a thread. This prevents it from 
blocking other scheduled automations from running.
### Example:
```python
from .. import utils
import schedule

def myfunc():
    print("I want to run every 10 minutes!")

schedule.every(10).minutes.do(utils.run_threaded, myfunc)
```

## Webhooks
Webhooks can be created by calling the `web_server.create_webhook()` function, and passing it the following arguments:
- name: the name of the webhook, used in creating the route.
- job_func: a function which will be run in a thread and passed the request's [args](https://flask.palletsprojects.com/en/2.0.x/api/#:~:text=property%20args%3A%20werkzeug.datastructures.MultiDict%5Bstr%2C%20str%5D%C2%B6)
as the only arguments.

The URL to the created webhook will be created based off of the name and the WEBHOOK_SECRET environment variable like
this: `https://example.com/$WEBHOOK_SECRET/name`

### Example:
```python
from .. import web_server

def myfunc(args):
    print("I want to run every time the webhook is called!")

web_server.create_webhook("mytask", myfunc)
```