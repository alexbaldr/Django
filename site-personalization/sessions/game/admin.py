from django.contrib import admin
from game.forms import PostForm
from game.models import Player,Game, PlayerGameInfo


class GameAdmin(admin.ModelAdmin):
    pass

class PlayerAdmin(admin.ModelAdmin):
    pass
    
class PlayerGameInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerGameInfo, PlayerGameInfoAdmin)