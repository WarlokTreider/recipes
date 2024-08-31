from django.shortcuts import render
from django.http import HttpResponse
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}


def recipe_view(request, recipe_name):
    recipe = DATA.get(recipe_name)

    if not recipe:
        return HttpResponse("Рецепт не найден", status=404)

    servings_str = request.GET.get('servings', '1')
    try:
        servings = int(servings_str)
        if servings <= 0:
            raise ValueError
    except ValueError:
        return HttpResponse("Некорректное значение servings", status=400)

    scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    context = {
        'recipe_name': recipe_name,
        'recipe': scaled_recipe,
    }

    return render(request, 'calculator/recipe.html', context)