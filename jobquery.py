from application.models import User, JobPost

class Jobquery:
    
    def __init__(self, title, category, email, location, employer_contact):
        self.title = title
        self.category = category
        self.email = email
        self.location = location
        self.employer_contact = employer_contact
    
def convert(given_list):
    obj_list = []
    for i in given_list:
        j = Jobquery(str(i.title), str(i.category), str(i.email), str(i.location), str(i.employer_contact))
        obj_list.append(j)
    return obj_list



