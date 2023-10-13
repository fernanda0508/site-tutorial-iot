from django.contrib import admin
from iot.models import Card, Circuito, MateriaisExperimento, MensagemDeContato


class CircuitoInline(admin.StackedInline):
    model = Circuito
    extra = 1


class MateriaisExperimentoInline(admin.StackedInline):
    model = MateriaisExperimento
    extra = 1


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    inlines = [CircuitoInline, MateriaisExperimentoInline]


admin.site.register(Circuito)
admin.site.register(MateriaisExperimento)
admin.site.register(MensagemDeContato)
