import threading
import time

class ThreadLifeCycle:

    @staticmethod
    def worker_thread(name):
        # Thread has started running
        print(f"Thread {name}: Running")

        # Simulate a blocked state (sleep represents waiting)
        print(f"Thread {name}: Sleeping")
        time.sleep(2)

        # Thread finishes its work
        print(f"Thread {name}: Done")

    @staticmethod
    def demonstrate():
        # NEW: Create the thread object
        print("1. NEW: Creating thread object")
        thread = threading.Thread(
            target=ThreadLifeCycle.worker_thread,
            args=("Worker-1",)
        )

        # READY: start() makes the thread ready/runnable
        print("2. READY: Starting thread")
        thread.start()

        # RUNNING
        print("3. RUNNING: Thread is executing")

        # BLOCKED
        print("4. BLOCKED: Thread may be sleeping or waiting")
        time.sleep(1)

        # Check if thread is alive
        print("5. Check if thread is alive")
        print(f"Thread is alive: {thread.is_alive()}")

        # TERMINATED
        print("6. TERMINATED: Wait for thread to finish")
        thread.join()
        print(f"Thread is alive: {thread.is_alive()}")

ThreadLifeCycle.demonstrate()