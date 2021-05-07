"""Classes for melon orders."""

## Create supur class: AbstractMelonOrder(). Other classes inherit from super class.
# Recognize what methods to move to the super class.
# Recognize which attributes that belong to international vs national.


class AbstractMelonOrder:
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        if self.species == "Christmas melon":
            base_price = 10
        else:
            base_price = 5

        shipping = 0
        if self.qty < 10 and self.order_type == "international":
            shipping = 3
        total = (1 + self.tax) * self.qty * base_price + shipping

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)
        """Initialize melon order attributes."""


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)
        """Initialize melon order attributes."""
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
