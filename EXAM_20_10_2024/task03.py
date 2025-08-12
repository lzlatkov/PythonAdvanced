# Read user input
def list_roman_emperors(*emperors, **emperor_rule_length):
    successful = []
    unsuccessful = []

    for name, success in emperors:
        rule_length = emperor_rule_length[name]
        if success:
            successful.append((name, rule_length))
        else:
            unsuccessful.append((name, rule_length))

    sorted_successful = sorted(successful, key=lambda x: (-x[1], x[0]))
    sorted_unsuccessful = sorted(unsuccessful, key=lambda x: (x[1], x[0]))

    result = []
    all_emperors = len(successful) + len(unsuccessful)
    result.append(f"Total number of emperors: {all_emperors}")
    if sorted_successful:
        result.append("Successful emperors:")
        for name, length in sorted_successful:
            result.append(f"****{name}: {length}")
    if sorted_unsuccessful:
        result.append("Unsuccessful emperors:")
        for name, length in sorted_unsuccessful:
            result.append(f"****{name}: {length}")

    return "\n".join(result)
# Print output
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
