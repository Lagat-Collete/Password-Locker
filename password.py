class Password:
  '''
class that generates new instances of password
  '''
  password_list = [] #Empty password list

  def __init__(self,plot,password):
      self.plot = plot
      self.password = password

#save method
  def save_password(self):

    '''
    save_password method saves password object into password_list
    '''

    Password.password_list.append(self)