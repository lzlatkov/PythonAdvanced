def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for cheese_name, quantity_list in sorted_cheeses:
        result += f"{cheese_name}\n"
        sorted_qty_list = sorted(quantity_list, reverse=True)
        result += "\n".join([str(el) for el in sorted_qty_list]) + "\n"
    return result

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
