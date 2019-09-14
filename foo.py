class Bar:
    def some_method_renamed(self):
        print("Called some_method")

    def add_one(self, value: int) -> int:
        return value + 1


class Foo:
    def __init__(self, bar: Bar):
        self._bar = bar

    def run(self):
        self._bar.some_method_renamed()

    def get_increased_value(self, value):
        return self._bar.add_one(value)
