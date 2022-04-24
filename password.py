


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
  
#delete method
  def delete_password(self):
    '''
    delete_password method deletes a saved password from the password_list
    '''
    Password.password_list.remove(self)

    #find method
  @classmethod
  def find_by_plot(cls,plot):
    '''
    method that takes  in plot and returns a password that matches the plot
    Args:
        plot:plot to search
    Returns:
        passord of that plot matches
    '''

    for password in cls.password_list:
      if password.plot == plot:
        return password