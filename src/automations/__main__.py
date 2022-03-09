import importlib
import os
import sys
import time

import schedule

from .keep_alive import keep_alive


keep_alive()


# Import all the tasks
TASKS_DIR = os.path.join(os.getcwd(), "src", "automations", "tasks")
tasks = []

sys.path.append(TASKS_DIR)
for task in os.listdir(TASKS_DIR):
    file_extn = ".py"
    if task.endswith(file_extn):
        module_name = task[: -len(file_extn)]
        task_module = importlib.import_module(module_name)
        tasks.append(task_module)

# Do the thing.
while 1:
    schedule.run_pending()
    time.sleep(1)
