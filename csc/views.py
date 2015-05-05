from django.http import HttpResponse
from django.shortcuts import render
import sys, os, requests, json, os.path, re, django
from django.utils import timezone
#import time, ast

sys.path.append('/home/ubuntu/workspace/csc')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
django.setup()
from csc.models import lastSession, user, accuracy
def mainPage(request):
    return HttpResponse("Deprecated")

steamID = ''

def index(request):
    def getData():
        global steamID
        steamIDDict = {'pB': '76561198055747972', 'joefish': '76561198072165784', 'random': '76561197972495328', 'Popey': '76561198039191886'}
        steamID = steamIDDict['pB']
        key = "21279B77E61B9270D505D812463D1C90"
        URL = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=" + key + "&steamid=" + steamID
        jsondata = json.loads(requests.get(URL).text) #Actual Data
        print("JSON Data Fetched")
        # print(str(jsondata))
        return(jsondata)


    def saveData(data):
        now = timezone.now() #2012-05-28 11:19:42.897000+00:00
        ID = user.objects.get(steam64=steamID)
        
        try:
            lastSession.objects.filter(userID=ID).delete()
        except:
            print("No data to delete")
            
        for item in data['playerstats']['stats']:
            #print("====New item====")
            nm = item['name']
            val = item['value']
            entry = lastSession(userID=ID, date=now, name=nm, value=val)
            entry.save()
            
            
    def accuracyCalc(data):
        now = timezone.now()
        newData = {} # The difference between new data and old data.
        ID = user.objects.get(steam64=steamID)
        for entry in lastSession.objects.filter(userID=ID): # For each item in the users old data
            for item in data['playerstats']['stats']: # For each item in the users new data
                if item['name'] == entry.name:
                    # print(item['name'],"has been matched to", entry.name) # Print matches in the database and the new data
                    newData[item['name']] = item['value'] - entry.value # The subtracty thing
        # print(str(newData)) # Prints the new data
        totalkills = {}
        totalshots = {}
        totalhits = {}
        finalAccuracy = {}
        # Accuracy = hits / shots
        for index, (key, value) in enumerate(newData.items()):
            match = re.search('(^total_shots_)(\w+$)', key)
            if match:
                # print(match.group(2)) # All weapons
                totalshots[match.group(2)] = value
        #print(str(totalshots))
        
        for index, (key, value) in enumerate(newData.items()):
            match = re.search('(^total_hits_)(\w+$)', key)
            if match:
                # print(match.group(2)) # All weapons
                totalhits[match.group(2)] = value
        #print(str(totalhits))
        
        for index, (key, value) in enumerate(newData.items()):
            match = re.search('(^total_kills_)(\w+$)', key)
            if match:
                # print(match.group(2)) # All weapons
                totalkills[match.group(2)] = value
        #print(str(totalkills))
        for index, (key, value) in enumerate(totalhits.items()):
            for index2, (key2, value2) in enumerate(totalshots.items()):
                if key == key2:
                    # calc accuracy
                    if int(value) != 0 and int(value2) != 0:
                        calcedAccuracy = int(value) / int(value2)
                        finalAccuracy[key] = calcedAccuracy
                        #print(key, calcedAccuracy)
                    else:
                        finalAccuracy[key] = 0
        #print(str(finalAccuracy))
        for index, (key, value) in enumerate(finalAccuracy.items()):
            entry = accuracy(userID=ID, date=now, weapon_type=key, weapon_accuracy=value)
            entry.save()
        return finalAccuracy
    data = getData()
    accuracyCalc(data)
    saveData(data)
    saveDataOutput = str(accuracyCalc(data))
    context_dict = {}

    # Render the response and send it back!
    return render(request, 'csc/main.html', context_dict)
    #response = "<h1>Your accuracies since last page load have been recorded:</h1><br>" + saveDataOutput
    #return HttpResponse(response)