import unittest


def cube(x):
    return x * x * x


def sum_three(a, b, c):
    return a + b + c


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def reverse_list(numbers, accumulator=None):
    if accumulator is None:
        accumulator = []

    if len(numbers) == 0:
        return accumulator

    return reverse_list(numbers[1:], [numbers[0]] + accumulator)


def count_element(numbers, element, accumulator=0):
    if len(numbers) == 0:
        return accumulator

    if numbers[0] == element:
        accumulator = accumulator + 1

    return count_element(numbers[1:], element, accumulator)


def normalize(numbers):
    maximum = max(numbers)

    if maximum == 0:
        return numbers.copy()

    return list(map(lambda x: x / maximum, numbers))


def sum_list_loop(numbers):
    result = 0

    for x in numbers:
        result = result + x

    return result


def sum_list_tail(numbers, accumulator=0):
    if len(numbers) == 0:
        return accumulator

    return sum_list_tail(numbers[1:], accumulator + numbers[0])


def add(x, numbers):
    new_list = numbers.copy()
    new_list.append(x)
    return new_list


class TestLaboratoryWork(unittest.TestCase):

    def test_5_1_cube(self):
        x = 3
        expected = 27
        result = cube(x)
        self.assertEqual(result, expected)

    def test_5_2_sum_three(self):
        a = 1
        b = 2
        c = 3
        expected = 6
        result = sum_three(a, b, c)
        self.assertEqual(result, expected)

    def test_5_3_factorial(self):
        n = 5
        expected = 120
        result = factorial(n)
        self.assertEqual(result, expected)

    def test_5_4_reverse_empty_list(self):
        numbers = []
        expected = []
        result = reverse_list(numbers)
        self.assertEqual(result, expected)

    def test_5_4_reverse_list(self):
        numbers = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        result = reverse_list(numbers)
        self.assertEqual(result, expected)

    def test_5_5_element_several_times(self):
        numbers = [1, 2, 2, 3, 2, 4]
        element = 2
        expected = 3
        result = count_element(numbers, element)
        self.assertEqual(result, expected)

    def test_5_5_element_once(self):
        numbers = [1, 2, 3, 4]
        element = 3
        expected = 1
        result = count_element(numbers, element)
        self.assertEqual(result, expected)

    def test_5_5_element_absent(self):
        numbers = [1, 2, 3, 4]
        element = 10
        expected = 0
        result = count_element(numbers, element)
        self.assertEqual(result, expected)

    def test_5_6_normalize_regular(self):
        numbers = [2, 4, 6, 8]
        original = numbers.copy()
        expected = [0.25, 0.5, 0.75, 1.0]

        result = normalize(numbers)

        self.assertEqual(result, expected)
        self.assertEqual(numbers, original)

    def test_5_6_normalize_max_zero(self):
        numbers = [-2, -1, 0]
        original = numbers.copy()
        expected = [-2, -1, 0]

        result = normalize(numbers)

        self.assertEqual(result, expected)
        self.assertEqual(numbers, original)

    def test_5_6_normalize_one_element(self):
        numbers = [5]
        original = numbers.copy()
        expected = [1.0]

        result = normalize(numbers)

        self.assertEqual(result, expected)
        self.assertEqual(numbers, original)

    def test_5_7_sum_list(self):
        numbers = [1, 2, 3, 4, 5]
        expected = 15

        loop_result = sum_list_loop(numbers)
        tail_result = sum_list_tail(numbers)

        self.assertEqual(loop_result, expected)
        self.assertEqual(tail_result, expected)
        self.assertEqual(loop_result, tail_result)

    def test_5_8_result_length(self):
        numbers = [1, 2, 3]
        x = 4
        result = add(x, numbers)
        self.assertEqual(len(result), 4)

    def test_5_8_original_not_changed(self):
        numbers = [1, 2, 3]
        original = numbers.copy()
        x = 4

        add(x, numbers)

        self.assertEqual(numbers, original)


if __name__ == "__main__":
    unittest.main(verbosity=2)