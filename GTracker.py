import psutil
import sqlite3

import Database


class GTracker:
    def __init__(self):
        self.game = None
        self.timer = 0

    @staticmethod
    def welcome():
        """ Welcome message """
        welcome_message = "Hello, {}\n" \
                          "CPU: {}/{}\n" \
                          "Mem: {}% used\n\n" \
                          "Ready for game!\n".format(psutil.Process().as_dict(attrs=['username'])['username'],
                                                     psutil.cpu_count(logical=False),
                                                     psutil.cpu_count(logical=True),
                                                     psutil.virtual_memory().percent,
                                                     )
        return welcome_message

    @staticmethod
    def get_games():
        """ Get games list """
        g = open('games.txt', 'r')
        lines = g.readlines()
        lines = list(map(str.strip, lines))
        return lines

    def found_target(self):
        """ Found target """
        process = None

        processes = psutil.process_iter(['name', 'create_time'])

        for process in processes:
            if process.name() in self.get_games():
                self.game = process.name()
                return process

    def save_result(self):
        """ Save timings in database """

        db = Database.Connector("GTracker.db")

        db.create_table()

        db.fill_table(self.timer)

        db.commit()
        db.close()
