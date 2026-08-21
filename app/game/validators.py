VALID_OPERATIONS = [
  "addition", "subtraction",
  "multiplication", "division"
]

VALID_DIFFICULTIES = [
  "easy", "medium", "hard"
]

def validate_game_data(data):
  
  operation = data["operation"]
  difficulty = data["difficulty"]
  
  if operation not in VALID_OPERATIONS:
    return True, "Invalid operation"
  
  if difficulty not in VALID_DIFFICULTIES:
    return True, "Invalid difficulty"
  
  return True, None