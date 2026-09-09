def validate_game_data(data):
  
  VALID_OPERATIONS = [
    "addition", "subtraction",
    "multiplication", "division"
  ]
  
  VALID_DIFFICULTIES = [
    "easy", "medium", "hard"
  ]
  
  operation = data["operation"]
  difficulty = data["difficulty"]
  
  if operation not in VALID_OPERATIONS:
    return False, "Invalid operation"
  
  if difficulty not in VALID_DIFFICULTIES:
    return False, "Invalid difficulty"
  
  return True, None

def validate_answers(data):
  
  answers = data["answers"]
  time = data["time"]
  
  if not isinstance(answers, dict):
    return False, "Invalid answers"
  
  if not isinstance(time, float):
    return False, "Invalid time"
  
  for answer in answers.values():
    if not isinstance(answer, int):
      return False, "Invalid answers"
    
  
  return True, None