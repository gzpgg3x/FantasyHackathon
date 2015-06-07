import os

def populate():
#     python_cat = add_cat('Python', views=128, likes=64)

#     add_page(cat=python_cat,
#         title="Official Python Tutorial",
#         url="http://docs.python.org/2/tutorial/")

    first_game = add_game('First Prize',
        kickoff_time="2015-06-07 17:00:04",        
        weight=1,
        totalscore=1, 
        season="2015")

    add_team(game=first_game,      
        team="Team SmartBall",
        win=0, 
        display_name="Team SmartBall")

    add_team(game=first_game,       
        team="Team What's Cookin",
        win=0, 
        display_name="Team What's Cookin")

    add_team(game=first_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")          

    amazon_game = add_game('Amazon Web Services Prize',
        kickoff_time="2015-06-07 17:00:04",        
        weight=1,
        totalscore=1, 
        season="2015")

    add_team(game=amazon_game,      
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")

    add_team(game=amazon_game,       
        team="Team RocketEmail",
        win=0, 
        display_name="Team RocketEmail")

    add_team(game=amazon_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")           

    clusterpoint_game = add_game('Clusterpoint Prize',
        kickoff_time="2015-06-07 17:00:04",        
        weight=1,
        totalscore=1, 
        season="2015")

    add_team(game=clusterpoint_game,      
        team="Team Embeddit",
        win=0, 
        display_name="Team Embeddit")

    add_team(game=clusterpoint_game,       
        team="Team Facetrax",
        win=0, 
        display_name="Team Facetrax")

    add_team(game=clusterpoint_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")           

    ibm_game = add_game('IBM Bluemix and FlowThings.IO Prize',
        kickoff_time="2015-06-07 17:00:04",        
        weight=1,
        totalscore=1, 
        season="2015")

    add_team(game=ibm_game,      
        team="Team Kangaroo",
        win=0, 
        display_name="Team Kangaroo")

    add_team(game=ibm_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon") 

    add_team(game=ibm_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")      

    hp_game = add_game('HP Prize',
        kickoff_time="2015-06-07 17:00:04",        
        weight=1,
        totalscore=1, 
        season="2015")

    add_team(game=hp_game,      
        team="Team hayhay",
        win=0, 
        display_name="Team hayhay")

    add_team(game=hp_game,       
        team="Team Strollwith.me",
        win=0, 
        display_name="Team Strollwith.me")

    add_team(game=hp_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")           

    branch_game = add_game('Branch Metrics Prize',
        kickoff_time="2015-06-07 17:00:04",        
        weight=1,
        totalscore=1, 
        season="2015")

    add_team(game=branch_game,      
        team="Team loginAnalytics",
        win=0, 
        display_name="Team loginAnalytics")

    add_team(game=branch_game,       
        team="Team crossroadsx",
        win=0, 
        display_name="Team crossroadsx")

    add_team(game=branch_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")      

    linode_game = add_game('Linode Prize',
        kickoff_time="2015-06-07 17:00:04",        
        weight=1,
        totalscore=1, 
        season="2015")

    add_team(game=linode_game,      
        team="Team Scope App",
        win=0, 
        display_name="Team Scope App")

    add_team(game=linode_game,       
        team="Team Whereisit?",
        win=0, 
        display_name="Team Whereisit?") 

    add_team(game=linode_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")      

    sparkPost_game = add_game('SparkPost Prize',
        kickoff_time="2015-06-07 17:00:04",        
        weight=1,
        totalscore=1, 
        season="2015")

    add_team(game=sparkPost_game,      
        team="Team HD Search",
        win=0, 
        display_name="Team HD Search")

    add_team(game=sparkPost_game,       
        team="Team SentiMatch",
        win=0, 
        display_name="Team SentiMatch")

    add_team(game=sparkPost_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")           

    thalmic_game = add_game('Thalmic Labs Prize',
        kickoff_time="2015-06-07 17:00:04",        
        weight=1,
        totalscore=1, 
        season="2015")

    add_team(game=thalmic_game,      
        team="Team BookerX",
        win=0, 
        display_name="Team BookerX")

    add_team(game=thalmic_game,       
        team="Team Linode Distributed Computing Platform",
        win=0, 
        display_name="Team Linode Distributed Computing Platform") 

    add_team(game=thalmic_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")      

    respoke_game = add_game('Respoke Prize',
        kickoff_time="2015-06-07 17:00:04",        
        weight=1,
        totalscore=1, 
        season="2015")

    add_team(game=respoke_game,      
        team="Team Campus Tour Guide",
        win=0, 
        display_name="Team Campus Tour Guide")

    add_team(game=respoke_game,       
        team="Team The Holy Grade",
        win=0, 
        display_name="Team The Holy Grade") 

    add_team(game=respoke_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")      

    twitter_game = add_game('Twitter Prize',
        kickoff_time="2015-06-07 17:00:04",        
        weight=1,
        totalscore=1, 
        season="2015")

    add_team(game=twitter_game,      
        team="Team Follow Plants",
        win=0, 
        display_name="Team Follow Plants")

    add_team(game=twitter_game,       
        team="Team Fantasy",
        win=0, 
        display_name="Team Fantasy") 

    add_team(game=twitter_game,       
        team="Team Fantasy Hackathon",
        win=0, 
        display_name="Team Fantasy Hackathon")                                             
 
    # add_game(game="Amazon Web Services Prize",
    #     # kickoff_time="2015-06-07 02:00:00",
    #     kickoff_time="2015-06-07 17:00:04",        
    #     weight=1,
    #     totalscore=1, 
    #     season="2015")

    # add_game(game="Clusterpoint Prize",
    #     # kickoff_time="2015-06-07 02:00:00",
    #     kickoff_time="2015-06-07 17:00:02",        
    #     weight=1,
    #     totalscore=1, 
    #     season="2015") 

    # add_game(game="IBM Bluemix and FlowThings.IO Prize",
    #     # kickoff_time="2015-06-07 02:00:00",
    #     kickoff_time="2015-06-07 17:00:02",        
    #     weight=1,
    #     totalscore=1, 
    #     season="2015") 

    # add_game(game="HP Prize",
    #     # kickoff_time="2015-06-07 02:00:00",
    #     kickoff_time="2015-06-07 17:00:02",        
    #     weight=1,
    #     totalscore=1, 
    #     season="2015") 

    # add_game(game="Branch Metrics Prize",
    #     # kickoff_time="2015-06-07 02:00:00",
    #     kickoff_time="2015-06-07 17:00:02",        
    #     weight=1,
    #     totalscore=1, 
    #     season="2015") 

    # add_game(game="Linode Prize",
    #     # kickoff_time="2015-06-07 02:00:00",
    #     kickoff_time="2015-06-07 17:00:02",        
    #     weight=1,
    #     totalscore=1, 
    #     season="2015") 

    # add_game(game="SparkPost Prize",
    #     # kickoff_time="2015-06-07 02:00:00",
    #     kickoff_time="2015-06-07 17:00:02",        
    #     weight=1,
    #     totalscore=1, 
    #     season="2015") 

    # add_game(game="Thalmic Labs Prize",
    #     # kickoff_time="2015-06-07 02:00:00",
    #     kickoff_time="2015-06-07 17:00:02",        
    #     weight=1,
    #     totalscore=1, 
    #     season="2015") 

    # add_game(game="Respoke Prize",
    #     # kickoff_time="2015-06-07 02:00:00",
    #     kickoff_time="2015-06-07 17:00:02",        
    #     weight=1,
    #     totalscore=1, 
    #     season="2015") 

    # add_game(game="Twitter Prize",
    #     # kickoff_time="2015-06-07 02:00:00",
    #     kickoff_time="2015-06-07 17:00:02",        
    #     weight=1,
    #     totalscore=1, 
    #     season="2015")                                                                             

    # add_page(cat=python_cat,
    #     title="How to Think like a Computer Scientist",
    #     url="http://www.greenteapress.com/thinkpython/")

    # add_page(cat=python_cat,
    #     title="Learn Python in 10 Minutes",
    #     url="http://www.korokithakis.net/tutorials/python/")

    # django_cat = add_cat("Django", views=64, likes=32)

    # add_page(cat=django_cat,
    #     title="Official Django Tutorial",
    #     url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    # add_page(cat=django_cat,
    #     title="Django Rocks",
    #     url="http://www.djangorocks.com/")

    # add_page(cat=django_cat,
    #     title="How to Tango with Django",
    #     url="http://www.tangowithdjango.com/")

    # frame_cat = add_cat("Other Frameworks", views=32, likes=16)

    # add_page(cat=frame_cat,
    #     title="Bottle",
    #     url="http://bottlepy.org/docs/dev/")

    # add_page(cat=frame_cat,
    #     title="Flask",
    #     url="http://flask.pocoo.org")

    # # Print out what we have added to the user.
    # for c in Category.objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print "- {0} - {1}".format(str(c), str(p))

def add_game(game, kickoff_time, weight, totalscore, season):
    g = Game.objects.get_or_create(game=game, kickoff_time=kickoff_time, weight=weight, totalscore=totalscore, season=season)[0]
    return g

def add_team(game, team, win, display_name):
    t = Team.objects.get_or_create(game=game,team=team,win=win,display_name=display_name)[0]
    return t

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bowlgames.settings')
    from picks.models import Game, Team, UserPicks
    populate()









# import os

# def populate():
#     python_cat = add_cat('Python', views=128, likes=64)

#     add_page(cat=python_cat,
#         title="Official Python Tutorial",
#         url="http://docs.python.org/2/tutorial/")

#     add_page(cat=python_cat,
#         title="How to Think like a Computer Scientist",
#         url="http://www.greenteapress.com/thinkpython/")

#     add_page(cat=python_cat,
#         title="Learn Python in 10 Minutes",
#         url="http://www.korokithakis.net/tutorials/python/")

#     django_cat = add_cat("Django", views=64, likes=32)

#     add_page(cat=django_cat,
#         title="Official Django Tutorial",
#         url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

#     add_page(cat=django_cat,
#         title="Django Rocks",
#         url="http://www.djangorocks.com/")

#     add_page(cat=django_cat,
#         title="How to Tango with Django",
#         url="http://www.tangowithdjango.com/")

#     frame_cat = add_cat("Other Frameworks", views=32, likes=16)

#     add_page(cat=frame_cat,
#         title="Bottle",
#         url="http://bottlepy.org/docs/dev/")

#     add_page(cat=frame_cat,
#         title="Flask",
#         url="http://flask.pocoo.org")

#     # Print out what we have added to the user.
#     for c in Category.objects.all():
#         for p in Page.objects.filter(category=c):
#             print "- {0} - {1}".format(str(c), str(p))

# def add_page(cat, title, url, views=0):
#     p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
#     return p

# def add_cat(name, views=0, likes=0):
#     c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
#     return c

# # Start execution here!
# if __name__ == '__main__':
#     print "Starting Rango population script..."
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
#     from rango.models import Category, Page
#     populate()    