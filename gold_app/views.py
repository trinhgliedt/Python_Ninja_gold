from django.shortcuts import render, redirect
import random

# index function initiates the gold count, activity log, and renders our html file
def index(request):
    
    if "gold" not in request.session:
        request.session["gold"] = 0
        request.session["history"] = []
        request.session["location_history"] = []
        request.session["num_moves"] = 0
        request.session["did_win"] = False
        request.session["did_lose"] = False
    
    return render(request, "index.html")

# process_money function calculates how much gold is earned
def process_money(request, location):
    # location is a route variable (from URL)
    if location == "farm":
        earned_gold = random.randint(10,20)
    elif location == "cave":
        earned_gold = random.randint(5,10)
    elif location == "house":
        earned_gold = random.randint(2,5)
    elif location == "casino":
        earned_gold = random.randint(-50,50)
    
    request.session["gold"] += earned_gold
    
    request.session["history"].append(earned_gold)
    request.session["location_history"].append(location)

    request.session["num_moves"] += 1
    
    return redirect("/")

def reset(request):
    request.session.clear()

    return redirect("/")

def store_data(request):
    request.session["num_moves_goal"] = request.POST["num_of_moves"]
    request.session["gold_goal"] = request.POST["amount_of_gold"]
    
    return redirect("/check")

def check_result(request):
    if "num_moves" in request.session and "gold_goal" in request.session:
        if request.session["num_moves"] > int(request.session["num_moves_goal"]):
            request.session["did_lose"] = True
            return redirect("/")
        if request.session["num_moves"] <= int(request.session["num_moves_goal"]) and request.session["gold"] >= int(request.session["gold_goal"]):
            request.session["did_win"] = True
    
    return redirect("/")

# def farm(request):
#     earned_gold = random.randint(10,20)
#     request.session["gold"] += earned_gold
#     request.session["history"].append(earned_gold)
#     request.session["num_moves"] += 1

#     return redirect("/")

# def cave(request):
#     earned_gold = random.randint(5,10)
#     request.session["gold"] += earned_gold
#     request.session["history"].append(earned_gold)
#     request.session["num_moves"] += 1

#     return redirect("/")

# def house(request):
#     earned_gold = random.randint(2,5)
#     request.session["gold"] += earned_gold
#     request.session["history"].append(earned_gold)
#     request.session["num_moves"] += 1

#     return redirect("/")

# def casino(request):
#     earned_gold = random.randint(-50,50)
#     request.session["gold"] += earned_gold
#     request.session["history"].append(earned_gold)
#     request.session["num_moves"] += 1

#     return redirect("/")
