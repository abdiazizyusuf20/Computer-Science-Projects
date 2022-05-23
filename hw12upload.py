import random
class Character:
    '''
    Purpose:represents a base character template for all of the specialization
    classes to build off of
    Instance variables: (What are the instance variables for this class,
    and what does each represent in a few words?)
    self.name: the name of a character
    self.color: the color of a charcter
    self.alive: a boolean representing whether the Character is currently alive,
    which should be initialized to True.
    self.role: a string representing whether the Character is a good role or an evil
    role, which should be initialized to 'Good'
    self.task_list: a list representing the tasks the Character must complete on the
    ship that will be of length num_tasks
    Methods: (What methods does this class have, and what does each do in a few words?)
    Constructor: The Character class constructor should have the following signature:
    __init__(self,name,color,num_tasks)
    __repr__(self):
    You must override the repr() method (similar to the str() method, except that it
     also changes what is output when you pass the object directly to the interpreter)
      so that it returns a string of the format below. Current status is ‘Alive’ if
       self.alive is True and ‘Ghost’ if self.alive is False:
    get_identity(self):
    This method takes no parameters (other than self) and simply returns 'Character'.
    '''

    def __init__(self,name,color,num_tasks):
        self.name = name
        self.color = color
        self.alive = True
        self.role = 'Good'
        possible_tasks = ['Stabilize drill', 'Calibrate distributor',
    'Map course', 'Clear out O2 filter', 'Download files',
    'Redirect power', 'Empty garbage', 'Repair wiring',
    'Fill engines tanks', 'Inspect laboratory', 'Record temperature',
    'Sign in with ID', 'Enable manifolds', 'Upload files']
        self.task_list = random.sample(possible_tasks, num_tasks )
    def __repr__(self):
        if self.alive == True:
            return str(self.name+': '+ self.color+ ' - '+ 'Health Status'+': '+ 'Alive')
        if self.alive == False:
            return str(self.name+': '+ self.color+ ' - '+ 'Health Status'+': '+ 'Ghost')
    def get_identity(self):
        return 'Character'
class Crewperson(Character):
    '''
    Purpose: represents a possible specialization for a Character, inherited class of charcter
    Instance variables: inherits all variables from character

    Methods:Override the get_identity(self) method from Character to instead return 'Crewperson'
    complete_task(self):
    The complete_task method takes no parameters (other than self) and removes the first item in the task_list.
    It also prints the following statement:
    <Name> has completed task: <task>.
    If the Crewpersons’ task list is empty, instead print the following statement:
    <Name> has completed all their tasks.
    '''

    def get_identity(self):
        return 'Crewperson'
    def complete_task(self):
        if len(self.task_list)>0:
                #self.task_list.pop(0)
            print (self.name + ' has completed task: ' + self.task_list[0]+'.')
            self.task_list.pop(0)
        else:
            print (self.name + ' has completed all their tasks.')
class Pretender(Character):
    '''
    Purpose: represents a possible specialization for a Character, inherited class of charcter
    Instance variables: inherits all variables from character
    Methods: The Pretender constructor must take the same parameters as its superclass
    (Character) constructor and pass them into the superclass constructor.The constructor
     must set the instance variable self.role to 'Evil'

    eliminate(self,target)
    The eliminate method takes as a parameter another Character object target and changes
    the .alive status of target to False. The method will also print the following string:
    <Name> eliminated <Target’s name>.
    '''

    def get_identity(self):
        return 'Pretender'
    def __init__(self,name,color,num_tasks):
        Character.__init__(self,name,color,num_tasks)
        self.role='Evil'
    def eliminate(self,target):
        target.alive = False
        print (self.name + ' eliminated ' + str(target.name)+'.')
            #print(self.name)
class Sheriff(Crewperson):
    '''
    Purpose: represents a possible specialization for a Character, inherited class of charcter
    Instance variables: inherits all variables from character
    Methods: (What methods does this class have, and what does each do in a few words?)
    Override the get_identity(self) method from Character to return the string 'Sheriff'

    encounter(self,target)
    The encounter method takes as a parameter another Character object target. If that
     target is a Pretender, change the .alive status of target to False. The method will also print the following string:
    <Name> eliminated <Target’s name>.
    '''

    def get_identity(self):
        return 'Sheriff'
    def encounter(self,target):
        if target.get_identity()=='Pretender':
            target.alive=False
            print (self.name + ' eliminated ' + str(target.name)+'.')
class Game:
    '''
    Purpose: will keep track of the status of the Game, including which Characters are
    still alive and if a team has won yet.
    Instance variables:self.player_list: stores the list of objects passed in as player_list.
    Methods: __init__(self,player_list)- contructor class sets playerlist to self.player_list
    check_winner(self):This function takes no arguments (other than self), and checks to see if either the Crewpersons or Pretenders have won yet.
    meeting(self):This function takes no arguments (other than self), and executes a meeting amongst the characters
    where they vote to eliminate a player
    play_game(self): and simulates a full round of the game until someone wins
    '''

    def __init__(self,player_list):
            #print(player_list)
        self.player_list=player_list
    def check_winner(self):
        pretenders_number=0
        crewperson_number=0
        crewtasks_number=0
        for players in self.player_list:
                #print(players.task_list)
            if players.role == 'Evil' and players.alive == True:
                pretenders_number+=1
            if players.role == 'Good' and players.alive == True:
                crewperson_number+=1
                if len(players.task_list)>0:
                    crewtasks_number+=1
            #print(pretenders_number)
            # if crewtasks_number==0 and pretenders_number>=crewperson_number:
            #     print('Crewpersons win!')
            #     return 'C'
        if pretenders_number>=crewperson_number:
            print('Pretenders win!')
            return 'P'
        elif pretenders_number==0 or crewtasks_number==0: #and #len(players.task_list==0):
            print('Crewpersons win!')
            return 'C'
        else:
            return '-'
    def meeting(self):
        alive_players=[]
        for players in self.player_list:
            if players.alive == True:
                alive_players.append(players.name)
        eliminated_player=random.choice(alive_players)
        for players in self.player_list:
            if players.alive == True:
                print(players.name + ' voted for ' + eliminated_player+'.')
        print(eliminated_player + ' was voted out and eliminated.')
        for players in self.player_list:
            if players.name==eliminated_player:
                    #print(players)
                players.alive=False
                    #print(Character.__repr__(players))
        return eliminated_player
    def play_game(self):
            #print(self.player_list)
        while self.check_winner()=='-':

            for players in self.player_list:
                    #players.complete_task()
                if type(players) == Crewperson:
                    i = random.randint(1, 3)
                    while i>0:
                            #complete_task(players)
                        (Crewperson.complete_task(players))
                        i=i-1
                elif type(players) == Pretender and players.alive==True:
                        #print(players)
                    target=random.choice(self.player_list)
                    if target.role=='Good' and target.alive==True:
                        Pretender.eliminate(players,target)

                elif type(players) == Sheriff and players.alive==True:
                    target=random.choice(self.player_list)
                    if target.role=='Evil' and target.alive==True:
                        Sheriff.encounter(players,target)

            if self.check_winner() == 'C':
                    #print(self.check_winner())
                return 'C'#self.check_winner()
                    #return self.check_winner()
                #Game.meeting(self)
            if self.check_winner() == 'P':
                return 'P'
            Game.meeting(self)
                # if self.check_winner() == 'C':
                #     #print(self.check_winner())
                #     return 'C'#self.check_winner()
                #     #return self.check_winner()
                # #Game.meeting(self)
                # if self.check_winner() == 'P':
                #     return 'P'
                # Game.meeting(self)
                #     if self.check_winner() != '-':
                #         #print( self.check_winner())
                #     return

                #return Game.play_game(self)
