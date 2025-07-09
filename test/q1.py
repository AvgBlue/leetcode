# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(temperatures):
    # Implement your solution here
    len_temperatures = len(temperatures)
    result = 0
    for night_i in range(1, len_temperatures, 2):
        is_warm = (
            temperatures[night_i] >= temperatures[night_i - 1] - 5
            and temperatures[night_i] >= temperatures[night_i + 1] - 5
        )
        if is_warm:
            result += 1
    return result


test_cases = [
    # ↘  Minimal length (N = 2)
    # 1. Warm because night is only 4 °C colder than first day
    ([10, 6, 9], 1),
    # 2. Not warm: 6 °C drop (fails the “≤ 5” rule)
    ([10, 4, 9], 0),
    # ↘  Exactly 5 °C below both days (border case)
    ([20, 15, 20], 1),
    # ↘  Mixed negatives; only the first night qualifies
    ([-5, -5, 0, -7, -1], 1),
    # ↘  First night qualifies, second doesn’t (fails on “next day” side)
    ([30, 25, 25, 21, 30], 1),
    # ↘  Three consecutive warm nights
    ([5, 0, 0, -5, -5, -10, -10], 3),
    # ↘  Extreme low temperatures, still warm
    ([-25, -20, -25], 1),
    # ↘  Alternating decline then rise; both nights warm
    ([0, -5, -10, -6, -1], 2),
    # ↘  Night is *strictly* more than 5 °C colder than the *first* day only ⇒ not warm
    ([30, 24, 25], 0),
    # ↘  All nights fail (each > 5 °C below at least one neighbour)
    ([40, 30, 20, 9, 0], 0),
]

# Test runner
pass_count = 0

for i, (input_data, expected) in enumerate(test_cases):
    result = solution(input_data)
    passed = result == expected
    if passed:
        pass_count += 1
    print(f"Test case {i+1}: {'PASS' if passed else 'FAIL'}")
    print(f"  Input: {input_data}")
    print(f"  Expected: {expected}, Got: {result}\n")

print(f"Passed {pass_count} out of {len(test_cases)} test cases.")
