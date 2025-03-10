from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView, PasswordResetConfirmView
from django.contrib.auth import logout
from kitchen.forms import DishForm, RegistrationForm, LoginForm, UserPasswordChangeForm, \
    UserPasswordResetForm, UserSetPasswordForm, CookUpdateForm
from kitchen.models import Cook, Ingredient, DishType, Dish

from django.shortcuts import render


def index(request):
    """View function for the home page of the site."""

    num_cooks = Cook.objects.count()
    num_ingredients = Ingredient.objects.count()
    num_dish_types = DishType.objects.count()
    num_dish = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_ingredients": num_ingredients,
        "num_dish_types": num_dish_types,
        "num_dish": num_dish,
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dishtype_list"
    template_name = "kitchen/Dish_type_list.html"
    paginate_by = 5


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_type-list")
    template_name = "kitchen/dishtype_form.html"

class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_type-list")
    template_name = "kitchen/dishtype_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish_type-list")
    template_name = "kitchen/dishtype_delete.html"

class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    context_object_name = "ingredient_list"
    template_name = "kitchen/ingredient_list.html"
    paginate_by = 7


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredients-list")
    template_name = "kitchen/ingredient_form.html"


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredients-list")
    template_name = "kitchen/ingredient_form.html"


class IngredientDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredients-list")
    template_name = "kitchen/ingredient_delete.html"

class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 15


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish

class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'kitchen/dish_form.html'
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_delete.html"

class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    template_name = "kitchen/cook_update_form.html"


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "kitchen/cook_delete.html"
    success_url = reverse_lazy("kitchen:cook-list")


@login_required
def toggle_assign_to_car(request, pk):
    cooks = Cook.objects.get(id=request.user.id)
    if (
        Dish.objects.get(id=pk) in cooks.prepared_dishes.all()
    ):
        cooks.prepared_dishes.remove(pk)
    else:
        cooks.prepared_dishes.add(pk)
    return HttpResponseRedirect(reverse_lazy("kitchen:dish-detail", args=[pk]))


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("Account created successfully!")
            form.save()
            return redirect('/accounts/login/')
        else:
            print("Registration failed!")
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'registration/accounts/sign-up.html', context)


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/accounts/sign-in.html'


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'registration/accounts/pas++sword-change.html'
    form_class = UserPasswordChangeForm


class UserPasswordResetView(PasswordResetView):
    template_name = 'registration/accounts/forgot-password.html'
    form_class = UserPasswordResetForm


class UserPasswrodResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/accounts/reset-password.html'
    form_class = UserSetPasswordForm


@login_required
def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')