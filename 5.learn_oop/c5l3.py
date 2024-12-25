class Rectangle:
    def overlaps(self, rect):
        if rect.get_left_x() <= self.get_right_x():
            if rect.get_right_x() >= self.get_left_x():
                if rect.get_top_y() >= self.get_bottom_y():
                    if rect.get_bottom_y() <= self.get_top_y():
                        return True
        return False

    # ALT solution:
    """
    return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )
    """
    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"

### END
run_cases = [
    (Rectangle(0, 0, 4, 4), Rectangle(3, 3, 6, 6), True),
    (Rectangle(0, 0, 4, 4), Rectangle(5, 5, 8, 8), False),
    (Rectangle(1, 1, 2, 2), Rectangle(2, 3, 3, 4), False),
]

submit_cases = run_cases + [
    (Rectangle(0, 0, 4, 4), Rectangle(4, 4, 8, 8), True),
    (Rectangle(6, 6, 9, 9), Rectangle(5, 5, 8, 8), True),
    (Rectangle(0, 0, 1, 1), Rectangle(4, 4, 5, 5), False),
    (Rectangle(1, 1, 4, 4), Rectangle(2, 2, 3, 3), True),
    (Rectangle(1, 1, 2, 2), Rectangle(0, 0, 4, 4), True),
]


def test(rect1, rect2, expected_overlap):
    print("---------------------------------")
    print(f"Overlap: {rect1} and {rect2}")
    print(f" - Expected overlap: {expected_overlap}")

    result = rect1.overlaps(rect2)
    print(f" - Actual overlap: {result}")

    if result == expected_overlap:
        print("Pass")
        return True
    else:
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
