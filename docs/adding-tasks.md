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
