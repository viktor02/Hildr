import configparser
from time import sleep
import GTracker

config = configparser.ConfigParser()
config.read('config.ini')

wait_time = int(config['settings']['wait_time'])

tracker = GTracker.GTracker()

print(tracker.welcome())
while True:
    while tracker.found_target() is None:
        print("Target not found. Waiting.")
        sleep(wait_time)

    target = tracker.found_target()

    print("Target found is {}".format(tracker.game))

    while target.is_running():
        tracker.timer += wait_time
        sleep(wait_time)

    print("{} was launched for {} seconds".format(tracker.game, tracker.timer))
    tracker.save_result()

    target = None
