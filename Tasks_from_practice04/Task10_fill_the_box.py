def fill_the_box(height, length, width, *args):
    total_volume = height * length * width
    cube_volume = 0
    for cube in args:
        if cube == "Finish":
            break
        cube_volume += cube
    if total_volume > cube_volume:
        return f"There is free space in the box. You could put {total_volume - cube_volume} more cubes."
    return f"No more free space! You have {cube_volume - total_volume} more cubes."

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
