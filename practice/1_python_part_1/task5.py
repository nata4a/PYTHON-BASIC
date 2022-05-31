"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""


def remove_duplicated_words(line: str) -> str:
    if len(line) == 0 or line is None:
        return

    line = line.split()
    el_list = []
    result = ' '

    for el in line:
        if el not in el_list:
            el_list.append(el)
    return (result.join(el_list))

print(remove_duplicated_words('cat cat dog 1 dog 2'))
print(remove_duplicated_words('cat cat cat'))
print(remove_duplicated_words('1 2 3'))