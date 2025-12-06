class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, x, y):
        return x + y

calculator = Calculator()
result = calculator.add(5, 10)
print("Result:", result)

# Bug: Calling a non-callable value
calculator = 42
result = calculator.add(5, 10)
print("Result:", result)

#adding comment to trigger commit


import tempfile

filename = tempfile.NamedTemporaryFile(delete=False)
tmp_file = open(filename, "w+")



def fpn(a):
  return i + a       # Noncompliant
