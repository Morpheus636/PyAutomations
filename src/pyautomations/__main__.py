import importlib
import os
import sys
import time

import schedule

from . import web_server

# Import all the tasks
TASKS_DIR = os.path.join(os.getcwd(), "src", "pyautomations", "tasks")
tasks = []
# Ensure the tasks dir exists
if not os.path.isdir(TASKS_DIR):
    os.mkdir(TASKS_DIR)
sys.path.append(TASKS_DIR)
for task in os.listdir(TASKS_DIR):
    file_extn = ".py"
    if task.endswith(file_extn):
        module_name = task[: -len(file_extn)]
        task_module = importlib.import_module(module_name)
        tasks.append(task_module)


# Start the web server.
web_server.start()


# Start the schedule loop.
while 1:
    schedule.run_pending()
    time.sleep(1)
