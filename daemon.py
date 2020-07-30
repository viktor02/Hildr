import configparser
from time import sleep

from GTracker import GTracker

config = configparser.ConfigParser()
config.read('config.ini')

# Process verification period
wait_time = config.getint('settings', 'wait_time')
path_to_db = config.get('settings', 'path_to_db')
path_to_games = config.get('settings', 'path_to_games')

tracker = GTracker.GTracker(path_to_db, path_to_games)

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

    # tracker.timer += time.time() - target.create_time()
    # May give bugs with fantastic values

    print("{} was launched for {:.2f} seconds".format(tracker.game, tracker.timer))
    tracker.save_result()

    # Reset timer and target for next game
    target = None
    tracker.timer = 0
