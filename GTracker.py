import configparser

import psutil


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
        """ Get games """
        g = open('games.txt', 'r')
        lines = g.readlines()
        return lines

    def found_target(self):
        """ Found target """
        process = None

        processes = psutil.process_iter(['name', 'create_time'])

        for process in processes:
            if process.name() in self.get_games():
                self.game = process.name()
                return process

    @staticmethod
    def get_results(game):
        game_results = configparser.ConfigParser()
        game_results.read("config.ini")
        return game_results.get(game, "timer")

    def save_result(self):
        """ Save timings in file """
        game_results = configparser.ConfigParser()

        game_results.read("config.ini")

        if game_results.has_section(self.game):
            old_res = game_results.getfloat(self.game, "timer")
            new_res = old_res + self.timer
            game_results.set(self.game, "timer", str(new_res))
        else:
            game_results.add_section(self.game)
            game_results.set(self.game, "timer", str(self.timer))

        with open('config.ini', 'w') as configfile:
            game_results.write(configfile)
