#Write a python program by considering Baseclass as TeamMember and Derived
#class as TeamLeader  use multiple inheritance concept to demonstrate the code.

class TeamMember:
    def member_info(self):
        print("I am a Team Member.")

class Project:
    def project_info(self):
        print("This is a Project.")

class TeamLeader(TeamMember, Project):
    def leader_info(self):
        print("I am the Team Leader.")

leader = TeamLeader()
leader.member_info()    
leader.project_info()   
leader.leader_info()    
