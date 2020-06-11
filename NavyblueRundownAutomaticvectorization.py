def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name + ", Be Welcome.")
  return new_list

print(add_greetings(["Owen", "Max", "Sophie"]))

def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

print(divisible_by_ten([20,35,40,50,80,90,55,45,]))

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))