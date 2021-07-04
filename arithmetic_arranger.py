import re

def arithmetic_arranger(problems, *args):
  operations = []
  if len(problems) > 5:
    return "Error: Too many problems."
  for operation in problems:
    #    We test if we have indesirable character
    if ("*" in operation) or ("/" in operation) :
      return "Error: Operator must be '+' or '-'."
    elif re.search(r'[^0-9 +-]', operation):
      return "Error: Numbers must only contain digits."
    element = re.split(r'([0-9]+)', operation.strip())
    if len(element[1]) > 4 or len(element[3]) > 4 :
      return "Error: Numbers cannot be more than four digits."
    # Here we will have a element of list that will be tuple example ('32','+','8')
    operations.append((element[1], element[2].strip(), element[3]))
  #    We store each line of the result in variable
  result_line1 = ""
  result_line2 = ""
  result_line3 = ""
  result_line4 = ""
  #    We construct the result string here
  for operation in operations:
    length_number1 = len(operation[0])
    length_number2 = len(operation[2])
    if length_number1 >= length_number2:
      result_line1 += " " * 2 + operation[0] + " " * 4
      result_line2 += operation[1] + " " * (length_number1 - length_number2 + 1) + operation[2] + " " * 4
      result_line3 += "-" * (length_number1 + 2) + " " * 4
    else:
      result_line1 += " " * (length_number2 - length_number1 + 2) + operation[0] + " " * 4
      result_line2 += operation[1] + " " + operation[2] + " " * 4
      result_line3 += "-" * (length_number2 + 2) + " " * 4
    if True in args:
      result = eval(operation[0] + operation[1] + operation[2])
      result_line4 += " " * (max(length_number1, length_number2) + 2 - len(str(result))) + str(result) + " " * 4
  arranged_problems = result_line1.rstrip() + "\n" + result_line2.rstrip() + "\n" + result_line3.rstrip()
  if result_line4 != "":
    arranged_problems += "\n" + result_line4.rstrip()

  return arranged_problems
