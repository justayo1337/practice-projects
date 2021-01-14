def arithmetic_arranger(problems,*args):
  if len(problems)<=5:
    for i in problems:
      aSplit = i.split()
      arranged_values=" " + f"\t{aSplit[0].strip()}\n{aSplit[1].strip()}\t{aSplit[2].strip()}\n"
      arranged_problems= arranged_values + ("-" * len(arranged_values))

      print(arranged_problems)
  else: 
    return "Error: Too many problems."



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
