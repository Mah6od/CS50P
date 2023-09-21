class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookies = []

    def __str__(self):
        return "🍪" * len(self._cookies)

    def deposit(self, n):
        if len(self._cookies) + n > self._capacity:
            raise ValueError("Exceeds the cookie jar's capacity")
        self._cookies.extend(["🍪"] * n)

    def withdraw(self, n):
        if len(self._cookies) < n:
            raise ValueError("Not enough cookies in the jar")
        for _ in range(n):
            self._cookies.pop()

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return len(self._cookies)
