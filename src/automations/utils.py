import threading


def run_threaded(job_func) -> None:
    """Run job_func in a thread.

    :param job_func: The function to run in a thread
    """
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
