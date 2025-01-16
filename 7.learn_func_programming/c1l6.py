def get_median_font_size(font_sizes):
    font_sizes_ = sorted(font_sizes) # sort the list in ascending
    n = len(font_sizes_) # length of list
    middle_index = n // 2 # floor division
    #middle_index_even = (n // 2) - 1 # for even use one index behind

    if not font_sizes_: # if n == 0:
        return None
    if n % 2:
        return font_sizes_[middle_index]
    return font_sizes_[middle_index - 1]

### END
run_cases = [
    ([4, 3, 2, 1, 5], 3),
    ([20, 14, 16], 16),
    ([9, 11, 16, 20], 11),
]

submit_cases = run_cases + [
    ([8, 8, 8], 8),
    ([30, 18, 14, 22], 18),
    ([6, 24, 6, 6, 24, 24, 2, 1, 3], 6),
    ([], None),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expected: {expected_output}")
    input_copy = input.copy()
    result = get_median_font_size(input)
    print(f"Actual: {result}")
    if result != expected_output:
        print("Fail")
        return False
    if input != input_copy:
        print(f"Expected font_sizes: {input_copy}")
        print(f"Actual font_sizes: {input}")
        print("font_sizes was modified")
        print("Fail")
        return False
    print("Pass")
    return True


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
