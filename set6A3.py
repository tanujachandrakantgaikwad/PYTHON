#Write a python program to make use of issubclass () or isinstance() functions
#to check the relationships of two classes and instances. 
# Base class
class TeamMember:
    pass

# Derived class
class TeamLeader(TeamMember):
    pass

# Create an instance
leader = TeamLeader()

# Check class relationship using issubclass()
print(issubclass(TeamLeader, TeamMember))  # True
print(issubclass(TeamMember, TeamLeader))  # False

# Check instance relationship using isinstance()
print(isinstance(leader, TeamLeader))      # True
print(isinstance(leader, TeamMember))      # True
print(isinstance(leader, object))          # True
