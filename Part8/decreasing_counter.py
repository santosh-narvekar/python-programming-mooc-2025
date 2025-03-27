# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.decreased_by = 0

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1
            self.decreased_by += 1
        return 0
    # Write the rest of the methods here!

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.value + self.decreased_by
