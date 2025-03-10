from django.contrib.auth import views as auth_views
from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView, DishTypeDeleteView, IngredientListView, IngredientCreateView, IngredientUpdateView,
    IngredientDeleteView, DishListView, DishDetailView, DishCreateView, DishUpdateView, DishDeleteView, CookListView,
    CookDetailView, CookDeleteView, toggle_assign_to_car, register_view, UserLoginView,
    logout_view, UserPasswordChangeView, UserPasswordResetView, UserPasswrodResetConfirmView, CookUpdateView,
)
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
path(
        "ingredient/",
        IngredientListView.as_view(),
        name="ingredients-list",
    ),
    path(
        "ingredient/create/",
        IngredientCreateView.as_view(),
        name="ingredient-create",
    ),
    path(
        "ingredient/<int:pk>/update/",
        IngredientUpdateView.as_view(),
        name="ingredient-update",
    ),
    path(
        "ingredient/<int:pk>/delete/",
        IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),
    path(
        "dish/",
        DishListView.as_view(),
        name="dish-list",
    ),
    path(
        "dish/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dish/create/",
        DishCreateView.as_view(),
        name="dish-create"
    ),
    path(
        "dish/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dish/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path(
        "dish/<int:pk>/toggle-assign/",
        toggle_assign_to_car,
        name="toggle-car-assign",
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "cooks/<int:pk>/update/",
        CookUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete"
    ),
    path('accounts/register/', register_view, name="register"),
    path('accounts/login/', UserLoginView.as_view(), name="login"),
    path('accounts/logout/', logout_view, name="logout"),
    path('accounts/password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/accounts/password-change-done.html'
    ), name="password_change_done"),
    path('accounts/password_reset/', UserPasswordResetView.as_view(), name="password_reset"),
    path('accounts/password_reset-confirm/<uidb64>/<token>/',
         UserPasswrodResetConfirmView.as_view(), name="password_reset_confirm"
         ),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/accounts/password-reset-done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/accounts/password-reset-complete.html'
    ), name='password_reset_complete'),
]