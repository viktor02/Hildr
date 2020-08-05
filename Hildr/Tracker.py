import psutil

from Hildr import Database


class Tracker:
    def __init__(self, path_to_db='Hildr.db', path_to_games='games.txt'):
        self.game = None
        self.timer = 0
        self.path_to_games = path_to_games
        self.path_to_db = path_to_db

    @staticmethod
    def welcome():
        """ Welcome message """
        welcome_message = "Hildr - tracker of your time spent \n" \
                          "================================== \n" \
                          "Hello, {}\n" \
                          "CPU: {}/{}\n" \
                          "Mem: {}% used\n\n" \
                          "Ready for game!\n".format(psutil.Process().as_dict(attrs=['username'])['username'],
                                                     psutil.cpu_count(logical=False),
                                                     psutil.cpu_count(logical=True),
                                                     psutil.virtual_memory().percent,
                                                     )
        return welcome_message

    def get_games(self):
        """ Get games list """
        games_path = self.path_to_games
        g = open(games_path, 'r')
        lines = g.readlines()
        lines = list(map(str.strip, lines))  # remove \r \n from lines
        return lines

    def found_target(self):
        """ Found target """
        process = None

        processes = psutil.process_iter(['name', 'create_time'])

        games = self.get_games()

        for process in processes:
            if process.name() in games:
                self.game = process.name()
                return process

    def save_result(self):
        """ Save timings in database """

        db = Database.Connector(self.path_to_db)

        db.create_table()

        db.fill_table(self.timer, self.game)

        db.commit()
        db.close()
