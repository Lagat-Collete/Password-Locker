
class Password:
   '''
   class that generates new instances of password
   '''
   def __init__(self, site, password):
       self.site = site
       self.password = password

   passwords_list = [] #Empty passwords list

  #save method
   def save_site(self):
    '''
    This function save new sites and passwords
    '''
    Password.passwords_list.append(self)
  
  #delete method
   def delete_site(self):
    '''
    delete_site method deletes a saved site from the passwords_list
    '''
    Password.passwords_list.remove(self)

  #find method
   @classmethod
   def find_by_site(cls, site_find):
    '''
    method that a user look for password using site name
    '''
    for sitefind in cls.passwords_list:
      if sitefind.site == site_find:
        return sitefind

    #method for displaying all the passwords
   @classmethod
   def display_sites(cls):
      '''
      method that returns the site
      '''
      return cls.passwords_list

    #check if it exist
   @classmethod
   def site_exist(cls, site_find):
        for sitefind in cls.passwords_lists:
          if sitefind.site == site_find:
            return sitefind
        return False
