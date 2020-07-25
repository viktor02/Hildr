import configparser
from time import sleep

import time
import GTracker

config = configparser.ConfigParser()
config.read('config.ini')

# Process verification period
wait_time = config.getint('settings', 'wait_time')

tracker = GTracker.GTracker()

print(tracker.welcome())
while True:
    while tracker.found_target() is None:
        print("Target not found. Waiting.")
        sleep(wait_time)

    target = tracker.found_target()

    print("Target found is {}".format(tracker.game))

    while target.is_running():
        sleep(wait_time)
    tracker.timer += time.time() - target.create_time()

    print("{} was launched for {:.2f} seconds".format(tracker.game, tracker.timer))
    tracker.save_result()

    # Reset timer and target for next game
    target = None
    tracker.timer = 0
