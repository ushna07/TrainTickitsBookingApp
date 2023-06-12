class Passenger:
    name = ""
    age = 0
    phone_no = ""
    email = ""

    # constructor
    def __init__(self, n, a, p, e):
        self.name = n
        self.age = a
        self.phone_no = p
        self.email = e

    def tostring(self):
        return "Name: " + self.name + " Age: " + str(self.age) + \
            "\nPhone.No: " + str(self.phone_no) + " Email: " + self.email
