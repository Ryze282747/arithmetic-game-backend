import random

def get_range(difficulty):
  
  if difficulty == "easy":
    return (1, 10)
  
  if difficulty == "medium":
    return (11, 50)
  
  if difficulty == "hard":
    return (51, 100)
  
def get_number_from_range(number_range):
  return random.randint(number_range[0], number_range[1])

def get_answer(num1, num2, operation):
  
  if operation == "addition":
    return num1 + num2
  
  if operation == "subtraction":
    
    lower_num = min(num1, num2)
    upper_num = max(num1, num2)
    
    return upper_num - lower_num
  
  if operation == "multiplication":
    return num1 * num2
  
  if operation == "division":
    return num1

def get_question(num1, num2, operation):
  
  if operation == "addition":
    operation = "+"
  
  if operation == "subtraction":
    lower_num = min(num1, num2)
    upper_num = max(num1, num2)
    
    return f"{upper_num} - {lower_num}?"
  
  if operation == "multiplication":
    operation = "×"
  
  if operation == "division":
    
    dividend = num1 * num2
    
    return f"{dividend} ÷ {num2}?"
  
  return f"{num1} {operation} {num2}?"

def get_choices(number_range, answer):
  
  choices = [answer,]
  
  while len(choices) != 4:
    num = answer + get_number_from_range((-10, 10))
    
    if num > 0 and num not in choices:
      choices.append(num)
  
  random.shuffle(choices)
  
  return choices

def get_total_score(raw_scores, quiz):
  
  score_multiplier = {
    "operation": {
      "addition": 1,
      "subtraction": 2,
      "multiplication": 4,
      "division": 5,
    },
    "difficulty": {
      "easy": 1,
      "medium": 2,
      "hard": 3,
    }
  }
  
  multiplier = score_multiplier["operation"][quiz.operation] * score_multiplier["difficulty"][quiz.difficulty]
  
  new_scores = list(map(lambda score: score * multiplier, raw_scores))
  
  return sum(new_scores)
  