import configparser
from time import sleep

from colorama import Fore, init

from Hildr import Tracker

# Init colorama
init()

config = configparser.ConfigParser()
config.read('config.ini')

# Process verification period
wait_time = config.getint('settings', 'wait_time')
path_to_db = config.get('settings', 'path_to_db')
path_to_games = config.get('settings', 'path_to_games')

tracker = Tracker.Tracker(path_to_db, path_to_games)


print(Fore.MAGENTA)
print(tracker.welcome())
print(Fore.RESET)
while True:
    while tracker.found_target() is None:
        print("Target not found. Waiting.")
        sleep(wait_time)

    target = tracker.found_target()

    print(Fore.GREEN)
    print("Target found is {}".format(tracker.game))

    while target.is_running():
        tracker.timer += wait_time
        sleep(wait_time)

    print("{} was launched for {:.2f} seconds".format(tracker.game, tracker.timer))
    print(Fore.RESET)
    tracker.save_result()

    # Reset timer and target for next game
    target = None
    tracker.timer = 0
