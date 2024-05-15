from FavouriteThings.fav_things import *
from Status.status import Status
from HelperComponents.RandomAccessMemory.RAM import RAMConnector


class SelfActions:

    def __init__(self, stress_level=0):
        self.stress_level = stress_level 
        # this should impact the input in a certain way.
        

    def read_book(self, book_title="", genre=""): # yeah i know the arg is kinda insane like what 
        # and how am i possibly have a good enuf way to have an appropriate
        # reaction to the book when it could be anything . use LLM ???
        happy = 1
        calm = 1
        # can add fuzzy similarity below
        happy = happy + 1 if book_title in favourite_books else happy
        happy = happy + 1 if genre in favourite_book_genres else happy
        if self.stress_level>2:
            self.stress_level+=1
            return
        status = Status.create()
        status.update_happy(happy)
        status.update_calm(calm)
        RAM_CONN = RAMConnector.create()
        RAM_CONN.event(key="book", val=f"Read {book_title}")

    def analyze_book(self, book_title="", genre=""):
        happy = 1
        smart = 1
        # can add fuzzy similarity below
        smart = smart + 1 if book_title in difficult_books else smart
        if self.stress_level>2:
            self.stress_level+=1
            return
        status = Status.create()
        status.update_happy(happy)
        status.update_smart(smart)
        RAM_CONN = RAMConnector.create()
        RAM_CONN.event(key="book", val=f"Analyzed {book_title}")

    def write_book(self, book_title="", book_type="", success=0):
        happy = 1
        smart = 2
        # can add fuzzy similarity below
        if self.stress_level>2:
            self.stress_level+=1
            return
        status = Status.create()
        status.update_happy(happy)
        if success>3:
            status.update_smart(smart)
        RAM_CONN = RAMConnector.create()
        RAM_CONN.event(key="book", val=f"Wrote {book_type} book called {book_title}")
    

    def play_video_game(self, game=""):
        # again the arg is insane, maybe i can compare against my list of fav
        # games and have an appropriate response. 
        # and if i play a game enough i should probably add it to
        # my new favs. I need a fav things class for sure
        happy = 3
        # can add fuzzy similarity below
        
        if self.stress_level>2:
            self.stress_level+=1
            return
        status = Status.create()
        status.update_happy(happy)
        RAM_CONN = RAMConnector.create()
        RAM_CONN.event(key="Game", val=f"Played {game}")    


    def make_video_game(self, game=""):
        # again the arg is insane, maybe i can compare against my list of fav
        # games and have an appropriate response. 
        # and if i play a game enough i should probably add it to
        # my new favs. I need a fav things class for sure
        pass
    

    def nap(self):
        # this should help regulate my current statuses slightly
        pass
    
 
    def sleep(self):
        # this should update my current statuses entirely
        pass
    
     
    def work(self, work_location):
        pass
    
     
    def paint(self, style):
        pass
    
     
    def listen_to_music(self, genre):
        pass
    
     
    def create_music(self, genre):
        pass
    
     
    def watch_movie(self, movie_title):
        #same as book
        pass
    
     
    def analyze_movie(self, movie_title):
        pass
    
    
    def eat(self, food_type):
        # i need a health object
        pass
    
    def exercise(self, duration):
        # so many type hints to add
        # also exercise who is she
        pass
    
        