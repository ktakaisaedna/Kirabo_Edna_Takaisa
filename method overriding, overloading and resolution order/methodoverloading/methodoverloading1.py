class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return sum(args)

calc = Calculator()
print(f"Add 2 numbers: {calc.add(5, 3)}")
print(f"Add 3 numbers: {calc.add(5, 3, 2)}")
print(f"Add many numbers: {calc.add(1, 2, 3, 4, 5)}")