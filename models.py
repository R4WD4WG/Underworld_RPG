# Player-------------------------------------------------------------------------------------
class Player:
    def __init__(self, name):
        # Defines all the player variables
        self.name = name # name
        self.level = 1 # level
        self.str = 1 # strength
        self.df = 1 # defense
        self.speed = 1 # speed
        self.sneak = 1 # sneak
        self.smarts = 1 # smarts
        self.money = 0 # dollars
        self.btc = 0.0 # bitcoin
        self.sp = 3 # skill points - Player gains 3 per level, some from rewards
        self.qp = 0 # quest points
        self.xp = 0 # experience points
        self.loc = None # player location


        # Puts stats into a dictionary, easy to pull later into text box
        self.stats = {
            'Level:': self.level,
            'Strength:': self.str,
            'Defense:': self.df,
            'Speed:': self.speed,
            'Sneak:': self.sneak,
            'Smarts:': self.smarts,
            'Dollars:': self.money,
            'Bitcoin:': self.btc,

        }

        # Quests - UNDER CONSTRUCTION
        # status:
            # 'not started'
            # 'in progress'
            # 'complete'
        # quest_points - assigns quest points value on completion
        self.quests = {
            'Quest 1': {'status': 'Not Started', 
                        'quest_points': 1},
            'Quest 2': {'status': 'Not Started', 
                        'quest_points': 2},
            'Quest 3': {'status': 'Not Started', 
                        'quest_points': 3},
        }


        # Player Inventory
        # Starting inventory is 20 slots
        # Single bag slot that can increase inventory space.
        self.inventory = {
            '1': None,
            '2': None,
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            '7': None,
            '8': None,
            '9': None,
            '10': None,
            '11': None,
            '12': None,
            '13': None,
            '14': None,
            '15': None,
            '16': None,
            '17': None,
            '18': None,
            '19': None,
            '20': None,
        }

    
        # Player's equipment
        self.equipment = {
            'Head:': None,
            'Neck:': None,
            'Chest:': None,
            'Belt:': None,
            'Legs:': None,
            'Feet:': None,
            'Weapon:': None,
            'Off Hand:': None,
            'Hands:': None,
            'Ring 1:': None,
            'Ring 2:': None,
            'Bag:': None,
        }


        # ALL PLAYER EQUIPMENT --------------------------------------------------------------

        # HEAD EQUIPS
        self.head = {
            
        }


        # NECK EQUIPS
        self.neck = {

        }


        # CHEST EQUIPS
        self.chest = {

        }

        
        # BEST EQUIPS
        self.belt = {

        }


        # LEG EQUIPS
        self.legs = {

        }


        # FEET EQUIPS - mmm feet
        self.feet = {

        }


        # WEAPON EQUIPS
        self.weapon = {

        }


        # OFF HAND EQUIPS
        self.off_hand = {

        }


        # HANDS EQUIPS
        self.hands = {

        }


        # RINGS EQUIPS
        self.rings = {

        }

        
        # BAG EQUIPS
        self.bags = {

        }


        # Game Locations
        self.locations = [
            # Undercity Start Locations
            'Undercity_Start', # 0 Starting Location (Market)
            'Undercity_Start_North', # 1 Start --> North (UNDER CONSTRUCTION)
            'Undercity_Start_South', # 2 Start --> South (UNDER CONSTRUCTION)
            'Undercity_Start_East', # 3 Start --> East (UNDER CONSTRUCTION)
            'Undercity_Start_West', # 4 Start --> West (UNDER CONSTRUCTION)

        ]

    
# Player End---------------------------------------------------------------------------------        

