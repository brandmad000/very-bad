# This is the main file where you control your bot's strategy

from util.objects import *
from util.routines import *
from util.tools import *
# Hi! Corbin here. Note the line below says GoslingUtils in the videos.
# DO NOT change the line below. It's no longer compatible with GoslingUtils so we renamed it.
# There are a few places like this where the code that you started with (the code you downloaded) might
# look different than the videos. THAT'S OK! Don't change it. We've made it better over time.
# Just follow along with the videos and it will all work the same.
class Bot(BotCommandAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self): 
        if self.get_intent() is not None: 
            return
        d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        d2 = abs(self.me.location.y - self.foe_goal.location.y)
        is_infront_of_ball = d1 > d2 
        is_good_retreat = abs(self.ball.location.y - self.me.location.y)  
        ground_shot_y = abs(self.ball.location.y - self.foe_goal.location.y) 
        ground_shot_x = abs(self.ball.location.x - self.foe_goal.location.x) 
        ball_location = self.ball.location  
        ball_velo = self.ball.velocity.magnitude() 
        ball_to_goal_distance =  abs(self.ball.location - self.foe_goal.location).magnitude() 
        intercept_time = ball_to_goal_distance / ball_velo    

        if self.kickoff_flag: 
        # set_intent tells the bot what it's trying to do 
            self.set_intent(kickoff()) 
            return
        # if infront of ball retreat 
        if is_infront_of_ball or is_good_retreat == 200: 
            self.set_intent(goto(self.friend_goal.location)) 
            return  
        if int(ground_shot_y) <= 800 and int(ground_shot_x) <= 800 and self.ball.location.z > 120 : 
            self.set_intent(aerial_shot(ball_location, intercept_time, self.foe_goal.location, find_slope)) 
            print ("working")
    
    
        self.set_intent(short_shot(self.foe_goal.location))  