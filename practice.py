import sys


def mortal_fibonacci(n: int, m: int) -> int:
    """Return the number of rabbit pairs after n months with an m-month lifespan."""
    if n < 1 or m < 1:
        raise ValueError("n and m must be positive integers")

    ages = [0] * m
    ages[0] = 1

    for _ in range(1, n):
        newborns = sum(ages[1:])
        ages = [newborns] + ages[:-1]

    return sum(ages)


def main() -> None:
    values = sys.stdin.read().split()
    if len(values) != 2:
        raise SystemExit("Expected two integers: n m")

    n, m = map(int, values)
    print(mortal_fibonacci(n, m))


if __name__ == "__main__":
    main()
