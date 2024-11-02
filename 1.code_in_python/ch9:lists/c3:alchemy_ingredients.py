"""
Assignment:

Finish the check_ingredient_match function by looping over the recipe list.
The function should calculate and return a percentage of ingredients the
character has, as well as a list of missing or wrongly ordered ingredients
from the recipe. The order of the ingredients matter! They must be in the
same index as the recipe to match. The missing ingredients must also be in
the same order as they appear in the recipe list.
"""
## CODE BELOW ##

def check_ingredient_match(recipe, ingredients):
    matching_ingredients = 0
    missing_ingredients = []
    for i in range(len(recipe)):
        if ingredients[i] == recipe[i]:
            matching_ingredients += 1
        else:
            missing_ingredients.append(recipe[i])
    total = (matching_ingredients / len(recipe)) * 100
    return total, missing_ingredients

## TEST CODE ##

run_cases = [
    (
        [
            "Dragon Scale",
            "Unicorn Hair",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        [
            "Dragon Scale",
            "Goblin Ear",
            "Phoenix Feather",
            "Elf Dust",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        (75.0, ["Unicorn Hair", "Troll Tusk"]),
    ),
    (
        [
            "Dragon Scale",
            "Unicorn Hair",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
        ],
        [
            "Dragon Scale",
            "Unicorn Hair",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
        ],
        (100.0, []),
    ),
]

submit_cases = run_cases + [
    (
        [
            "Dragon Scale",
            "Unicorn Hair",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
        ],
        [
            "Goblin Ear",
            "Elf Dust",
            "Griffin Feather",
            "Mermaid Tear",
            "Goblin Ear",
            "Phoenix Feather",
            "Troll Tusk",
        ],
        (
            0.0,
            [
                "Dragon Scale",
                "Unicorn Hair",
                "Phoenix Feather",
                "Troll Tusk",
                "Mandrake Root",
                "Griffin Feather",
                "Elf Dust",
            ],
        ),
    ),
    (
        [
            "Dragon Scale",
            "Unicorn Hair",
            "Phoenix Feather",
            "Troll Tusk",
            "Mandrake Root",
            "Griffin Feather",
            "Elf Dust",
            "Goblin Ear",
        ],
        [
            "Unicorn Hair",
            "Dragon Scale",
            "Phoenix Feather",
            "Troll Tusk",
            "Griffin Feather",
            "Mandrake Root",
            "Goblin Ear",
            "Elf Dust",
        ],
        (
            25.0,
            [
                "Dragon Scale",
                "Unicorn Hair",
                "Mandrake Root",
                "Griffin Feather",
                "Elf Dust",
                "Goblin Ear",
            ],
        ),
    ),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:\nrecipe: {input1}\ngathered_ingredients: {input2}")
    print(f"Expecting: {expected_output}")
    result = check_ingredient_match(input1, input2)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
