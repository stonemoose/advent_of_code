import re


def is_nice(word):
    vowels = r'[aeiou].*[aeiou].*[aeiou]'
    illegal = r'ab|cd|pq|xy'
    twice = r'([a-z])\1'
    return (
        bool(re.search(vowels, word))
        and not bool(re.search(illegal, word))
        and bool(re.search(twice, word))
    )


def is_nice_v2(word):
    double_pair = r'([a-z]{2}).*\1'
    twice = r'([a-z])[a-z]\1'
    return bool(re.search(double_pair, word)) and bool(re.search(twice, word))


if __name__ == '__main__':
    with open('input') as f:
        words = f.readlines()
        print(f'Part 1: {sum([is_nice(word) for word in words])}')
        print(f'Part 2: {sum([is_nice_v2(word) for word in words])}')
