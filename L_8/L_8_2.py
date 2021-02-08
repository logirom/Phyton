class DvsNull(Exception):
     def __str__(self):
        return f"деление на 0"


def null_dev(divider, denominator):
    if denominator == 0:
        raise DvsNull()
    return divider / denominator

try:
    print(null_dev(19, 5))
except DvsNull as e:
    print(e)