class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            raise Exception("cannot change title")
        elif isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception("titles must be strings longer than 0 chars")

    def results(self):
        return [
            result
            for result in Result.all
            if result.game == self and isinstance(result, Result)
        ]

    def players(self):
        allplayers = [result.player for result in self.results()]
        return list(set(allplayers))

    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        return sum(scores) / len(scores) if len(scores) else 0


class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(2, 17):
            self._username = username
        else:
            raise Exception("username must be string between 2-16 chars")

    def results(self):
        return [
            result
            for result in Result.all
            if result.player == self and isinstance(result, Result)
        ]

    def games_played(self):
        allgames = [result.game for result in self.results()]
        return list(set(allgames))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        allgames = [result.game for result in self.results()]
        return allgames.count(game)

    @classmethod
    def highest_scored(cls, game):
        players = game.players()
        if not players:
            return None
        averages = [
            {"player": player, "score": game.average_score(player)}
            for player in players
        ]
        sorted_scores = sorted(averages, key=lambda obj: obj["score"])
        return sorted_scores[-1]["player"]


class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    all = []

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if (
            isinstance(score, int)
            and score in range(1, 5001)
            and not hasattr(self, "score")
        ):
            self._score = score
        else:
            raise Exception("score must be int between 1-5000 and cannot be changed")

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("player must be an instance of Player")

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception("game must be an instance of Game")
