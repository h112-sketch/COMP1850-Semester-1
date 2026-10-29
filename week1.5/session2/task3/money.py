class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        if not isinstance(pounds, int):
            raise TypeError("Pounds must be an integer")
        if pounds < 0:
            raise ValueError("Pounds cannot be negative")
        if not isinstance(pence, int):
            raise TypeError("Pence must be an integer")
        if pence < 0 or pence > 99:
            raise ValueError("Pence must be between 0 and 99")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other):
        if not isinstance(other, Money):
            raise TypeError("Can only add Money objects")

        total_pence = (
            self.pounds * 100 + self.pence
            + other.pounds * 100 + other.pence
        )

        pounds = total_pence // 100
        pence = total_pence % 100

        return Money(pounds, pence)