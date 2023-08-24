from django.urls import path
from . import views

urlpatterns = [
    path("weather/", views.weather, name="weather"),
    path("risk-analyzer/", views.risk_analyzer, name="risk_analyzer"),
    path("auction-house/", views.auction_house, name="auction_house"),
    path(
        "immunization-compliance/",
        views.immunization_compliance,
        name="immunization_compliance",
    ),
    path("starving-steve/", views.starving_steve, name="starving_steve"),
    path("epic-tanks/", views.epic_tanks, name="epic_tanks"),
    path("battle-vessel/", views.battle_vessel, name="battle_vessel"),
]
