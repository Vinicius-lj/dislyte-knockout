# Register your models here.

from django.contrib import admin

from .models import Esper, Player, Player_esper

class PlayerEsperInline(admin.TabularInline):
    model = Player_esper
    extra = 10

class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": [("name", "server", "guild")]})
    ]
    inlines = [PlayerEsperInline]
    list_display = ["name", "server", "guild"]
    list_filter = ["server", "guild"]
    search_fields = ["name"]

class EsperAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": [("name", "role")]}),
        (None, {"fields": [("classe", "rarity")]}),
        (None, {"fields": ["leader_effect"]}),
    ]
    list_display = ["name", "classe", "role", "rarity", "leader_effect"]
    list_filter = ["role", "classe", "rarity"]
    search_fields = ["name"]

class Player_esperAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": [("ressonance", "team", "ifleader", "esper_id", "player_id", "version")]})
    ]
    list_display = ["player_id", "esper_id", "ressonance", "team", "ifleader", "version"]

admin.site.register(Player, PlayerAdmin)
admin.site.register(Esper, EsperAdmin)
admin.site.register(Player_esper, Player_esperAdmin)