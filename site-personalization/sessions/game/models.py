from django.db import models


class Player(models.Model):
    nikname = models.CharField(max_length=50)

    def __str__(self):
        return self.nikname


class Game(models.Model):
    number = models.IntegerField()
    relationship = models.ManyToManyField(Player, related_name='players', through='PlayerGameInfo')

    def __str__(self):
        return "{}".format(self.number)


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, verbose_name="Игрок", on_delete=models.CASCADE)
    game = models.ForeignKey(Game, verbose_name="Игра", on_delete=models.CASCADE)
    is_autor = models.BooleanField(default=False)

    def __str__(self):
        return "{} & {}".format(self.player, self.game)
