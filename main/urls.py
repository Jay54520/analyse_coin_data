# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('coin_ids/', views.coin_ids),
]