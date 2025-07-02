class Interpreter:
    def __init__(self):
        self.stack = []

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def ADD_TWO_VALUES(self):
        first_num = self.stack.pop()
        second_num = self.stack.pop()
        sum_result = first_num + second_num
        self.stack.append(sum_result)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def run_code(self, what_to_execute):
        instructions = what_to_execute["instructions"]
        numbers = what_to_execute["numbers"]

        for step in instructions:
            instructions, argument = step

            if instructions == "LOAD_VALUE":
                number = numbers[argument]
                self.LOAD_VALUE(number)

            if instructions == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()

            if instructions == "PRINT_ANSWER":
                self.PRINT_ANSWER()


what_to_execute = {
    "instructions": [
        ("LOAD_VALUE", 0),
        ("LOAD_VALUE", 1),
        ("ADD_TWO_VALUES", None),
        ("LOAD_VALUE", 2),
        ("ADD_TWO_VALUES", None),
        ("PRINT_ANSWER", None),
    ],
    "numbers": [7, 5, 8],
}


interpreter = Interpreter()
interpreter.run_code(what_to_execute)
