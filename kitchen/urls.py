from django.urls import path

from kitchen.views import index, DishTypeListView, DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishtype/",
        DishTypeListView.as_view(),
        name="dish_type-list",
    ),
    path(
        "dishtype/create/",
        DishTypeCreateView.as_view(),
        name="dish_type-create",
    ),
    path(
        "dishtype/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_type-update",
    ),
    path(
        "dishtype/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_type-delete",
    ),
]