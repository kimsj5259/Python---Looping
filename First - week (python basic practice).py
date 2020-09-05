
#For loop Assignment
#Input 으로 주어진 리스트에서 오직 한번만 나타나는 값 (unique value)을 가지고 있는 요소는 출력해주세요.

my_list = [s for s in input().split()]

ur_list = []

for a in my_list:
  if a not in ur_list:
    ur_list.append(a)
  else:
    ur_list.remove(a)

print(ur_list)

#While Loop Assignment
#find_smallest_integer_divisor 라는 이름의 함수를 구현해 주세요.
#find_smallest_integer_divisor 함수는 하나의 parameter를 받습니다.
#Parameter 값은 integer만 주어집니다. 
#find_smallest_integer_divisor 주어진 parameter 값을 나눌 수 있는
#1을 제외한 최소의 양의 정수를 리턴하여야 합니다.

def find_smallest_integer_divisor(numb):
  x = 2
  
  while numb % x != 0:
    x += 1 
  return x

find_smallest_integer_divisor(58)

#Looping Dictionary Assignment
#Input으로 주어진 list의 각 요소(element)가 해당 list에 몇번 나타나는지 수를
#dictionary로 만들어서 리턴해주세요.  Dictionary의 key는 list의 요소 값이며
#value는 해당 요소의 총 빈도수 입니다.

def get_occurrence_count(my_list):
  # 이 함수를 구현 해주세요
  dict = {}
  for each_key in my_list:
    dict[each_key] = my_list.count(each_key)
    
  return dict
  
print(get_occurrence_count(["one",2,3,2,"one"]))

#Complex Function Assignment
#함수 2개를 구현해주세요. 함수의 이름은 다음과 같아야 합니다.
#sum_of_numbers
#what_is_my_full_name
#함수 sum_of_numbers는 arugment로 주어지는 모든 수를 합한 값을 리턴해야 합니다.
def sum_of_numbers(*args):
  return sum(args)

sum_of_numbers(1,2,3)

def what_is_my_full_name(**kwargs):
  print(kwargs.keys())
  if "first_name" in kwargs and "last_name" in kwargs:
    return f"""{kwargs["last_name"]} {kwargs["first_name"]}"""
  elif "first_name" in kwargs and "last_name" not in kwargs:
    return f"""{kwargs["first_name"]}"""
  elif "first_name" not in kwargs and "last_name" in kwargs:
    return f"""{kwargs["last_name"]}"""
  else:
    return "Nobody"

#Nested Function(중첩) Assignment
#Decorator를 구현해보세요.closure를 한단계 더 나아가 사용하는 고급 기능입니다.
def name_decorator(name):
  def decorator(func):
    def wrapper():
      result = func() 
      return result + name
    return wrapper
  return decorator
#@name_decorator
def greeting():
  return "Hello, "
  
print(greeting())

a = 9
def shadowing():
    a = 1
    print(a)

shadowing()
print(a)

#Scope 아래 코드를 바꿔서 parameter 상관 없이 무조건 63 출력.

what_is_my_scope = 7

def scope_test(what_is_my_scope):
  some_number = 9
  def inner_scope_test(what_is_my_scope):
    return some_number * what_is_my_scope
  return inner_scope_test(what_is_my_scope)
print(scope_test(1))
===========================================
what_is_my_scope = 7

def scope_test(what_is_my_scope):
  some_number = 9
  
  def inner_scope_test(what_is_my_scope):
    what_is_my_scope = 7
    return some_number * what_is_my_scope
    
  return inner_scope_test(what_is_my_scope)
  
print(scope_test(1))



  
    
      

    
   
