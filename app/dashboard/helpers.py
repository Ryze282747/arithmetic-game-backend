def get_best_time(attempts):
  
  times = [attempt.time for attempt in attempts]
  
  return min(times)

def get_total_points(attempts):
  
  points = [attempt.score for attempt in attempts]
  
  return sum(points)

def get_accuracy(attempts):
  
  correct_answers = [attempt.correct_answers for attempt in attempts]
  total_questions = [attempt.total_questions for attempt in attempts]
  
  accuracy = sum(correct_answers) / sum(total_questions) * 100
  
  return accuracy