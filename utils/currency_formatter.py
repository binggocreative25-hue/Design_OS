class CurrencyFormatter:

    @staticmethod
    def usd(amount: int):

        return f"${amount:,}"

    @staticmethod
    def idr(amount: int):

        return f"Rp {amount:,}".replace(
            ",",
            "."
        )