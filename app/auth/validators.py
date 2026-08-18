def validate_signup(data):
  
  username = data["username"].replace(" ", "")
  password = data["password"].replace(" ", "")
  confirm_password = data["confirmPassword"].replace(" ", "")
  
  if len(username) == 0:
    return {
      "msg":"Username is required."
    }, 400
  
  if len(password) < 8:
    return {
      "msg":"Password is too short."
    }, 400
  
  if password != confirm_password:
    return {
      "msg":"Password do not match."
    }, 400
  
  return None