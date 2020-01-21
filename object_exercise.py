class Person:

    
    
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.greeting_count = 0
         self.people_greeted = []
         

    def greet(self, other_person):
         print('Hello {}, I am {}!'.format(other_person.name, self.name))
         if other_person not in self.people_greeted:
             self.people_greeted.append(other_person)
         self.greeting_count += 1
    def print_contact_info(self):
        print("Name: {} Contact Info: Email:  {}  Phone: {}".format(self.name, self.email, self.phone))
    def add_friend(self, friend):
        self.friends.append(friend)
    def num_friends(self):
        return len(self.friends)
    def __str__(self):
     return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
    def num_unique_people_greeted(self):
         print(len(self.people_greeted))



#instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny. Instantiate another person named Jordan.

sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')

jordan = Person('Jordan', 'jordan.aol.com','495,586,3456')

# Have sonny greet jordan using the greet method.
# Have jordan greet sonny using the greet method.



sonny.greet(jordan)
jordan.greet(sonny)


print("Name: {} Contact Info: Email:  {}  Phone: {}".format(sonny.name, sonny.email, sonny.phone))

print("Name: {} Contact Info: Email:  {}  Phone: {}".format(jordan.name, jordan.email, jordan.phone))

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        print("{} {} {}".format(self.make,self.model,self.year))
 


car = Vehicle('Nissan', 'Leaf', 2015)

print(car.make, car.model, car.year)
# Add a print_info method to the Vehicle class. It will print out the vehicle's information like so:
car.print_info()

# Go back to the Person class. Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person. You will use it thus:

# sonny.print_contact_info()


jordan.friends.append(sonny)
# sonny.friends.append(jordan)
    

# print(jordan.friends)

# print(len(jordan.friends))


# jordan.add_friend("Bert")

# print(len(jordan.friends))

print(jordan.num_friends())
print(jordan.greeting_count)


print(str(jordan))

# Keep track of the number of unique people a person has greeted, and be able to report that number via the num_unique_people_greeted method:

jordan.num_unique_people_greeted()
