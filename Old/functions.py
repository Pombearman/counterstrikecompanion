import sys, os
#import urllib.request
import requests
import json, os.path, time, ast
from tabulate import tabulate

def resolveVanity(name):
  #data = requests.get('https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=' + "21279B77E61B9270D505D812463D1C90" + '&vanityurl=' + name).text
  data = '{"response":{"steamid":"76561198039191886","success":1}}'
  jdata = json.loads(data)
  p = []
  [p.extend([k,v]) for k,v in jdata.items()]
  return(p[1]['steamid'])

def resetData():
  global steamID, key, gameID, URL, l, totalshots, totalhits, totalkills, accuracy, overallAcc
  global farray, fileData, tempmax, laststats
  steamID = ""
    #joefish 76561198072165784
    #pB 76561198055747972
    #random 76561197972495328
  key = "21279B77E61B9270D505D812463D1C90"
  gameID = "730" #730 = CS:GO
  URL = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=" + gameID + "&key=" + key + "&steamid=" + steamID
  l = [] #JSON Data
  totalshots, totalhits, totalkills  = [], [], [] #Array of weapon name + data
  accuracy = [] #Array of weapon name + accuracy with gun
  overallAcc = 0
  farray = [] #[fsteamid, ftimestamp, foveraccuracy, fgunaccuracy] - from file all with same steam ID
  fileData = [] #Similar to farray, except with all steam ID's in the file
  tempmax = 0 #Temporary variable used to find the last time stamp.
  laststats = [] #Array that holds the last data of the player

def urlRequest(urlname):
  #data = requests.get(URL).text
  data = '{"playerstats":{"steamID":"76561198039191886","gameName":"ValveTestApp260","stats":[{"name":"total_kills","value":3177},{"name":"total_deaths","value":2553},{"name":"total_time_played","value":157404},{"name":"total_planted_bombs","value":37},{"name":"total_defused_bombs","value":18},{"name":"total_wins","value":864},{"name":"total_damage_done","value":456277},{"name":"total_money_earned","value":4612700},{"name":"total_kills_knife","value":35},{"name":"total_kills_hegrenade","value":1},{"name":"total_kills_glock","value":74},{"name":"total_kills_deagle","value":61},{"name":"total_kills_elite","value":72},{"name":"total_kills_fiveseven","value":44},{"name":"total_kills_xm1014","value":52},{"name":"total_kills_mac10","value":61},{"name":"total_kills_ump45","value":266},{"name":"total_kills_p90","value":155},{"name":"total_kills_awp","value":61},{"name":"total_kills_ak47","value":293},{"name":"total_kills_aug","value":108},{"name":"total_kills_famas","value":132},{"name":"total_kills_g3sg1","value":110},{"name":"total_kills_m249","value":41},{"name":"total_kills_headshot","value":1139},{"name":"total_kills_enemy_weapon","value":80},{"name":"total_wins_pistolround","value":68},{"name":"total_wins_map_de_cbble","value":1},{"name":"total_wins_map_de_dust2","value":373},{"name":"total_wins_map_de_inferno","value":161},{"name":"total_wins_map_de_train","value":151},{"name":"total_weapons_donated","value":127},{"name":"total_broken_windows","value":8},{"name":"total_kills_enemy_blinded","value":35},{"name":"total_kills_knife_fight","value":1},{"name":"total_kills_against_zoomed_sniper","value":124},{"name":"total_dominations","value":140},{"name":"total_domination_overkills","value":278},{"name":"total_revenges","value":34},{"name":"total_shots_hit","value":13609},{"name":"total_shots_fired","value":62841},{"name":"total_rounds_played","value":1706},{"name":"total_shots_deagle","value":327},{"name":"total_shots_glock","value":2476},{"name":"total_shots_elite","value":807},{"name":"total_shots_fiveseven","value":387},{"name":"total_shots_awp","value":211},{"name":"total_shots_ak47","value":5331},{"name":"total_shots_aug","value":1421},{"name":"total_shots_famas","value":3202},{"name":"total_shots_g3sg1","value":703},{"name":"total_shots_p90","value":4484},{"name":"total_shots_mac10","value":1256},{"name":"total_shots_ump45","value":5628},{"name":"total_shots_xm1014","value":1425},{"name":"total_shots_m249","value":989},{"name":"total_hits_deagle","value":117},{"name":"total_hits_glock","value":473},{"name":"total_hits_elite","value":362},{"name":"total_hits_fiveseven","value":138},{"name":"total_hits_awp","value":64},{"name":"total_hits_ak47","value":986},{"name":"total_hits_aug","value":332},{"name":"total_hits_famas","value":576},{"name":"total_hits_g3sg1","value":192},{"name":"total_hits_p90","value":810},{"name":"total_hits_mac10","value":302},{"name":"total_hits_ump45","value":1192},{"name":"total_hits_xm1014","value":371},{"name":"total_hits_m249","value":131},{"name":"total_rounds_map_de_cbble","value":1},{"name":"total_rounds_map_de_dust2","value":685},{"name":"total_rounds_map_de_inferno","value":320},{"name":"total_rounds_map_de_train","value":319},{"name":"last_match_t_wins","value":5},{"name":"last_match_ct_wins","value":13},{"name":"last_match_wins","value":2},{"name":"last_match_max_players","value":10},{"name":"last_match_kills","value":4},{"name":"last_match_deaths","value":19},{"name":"last_match_mvps","value":0},{"name":"last_match_favweapon_id","value":13},{"name":"last_match_favweapon_shots","value":56},{"name":"last_match_favweapon_hits","value":13},{"name":"last_match_favweapon_kills","value":2},{"name":"last_match_damage","value":800},{"name":"last_match_money_spent","value":46150},{"name":"last_match_dominations","value":0},{"name":"last_match_revenges","value":0},{"name":"total_mvps","value":164},{"name":"total_rounds_map_de_lake","value":10},{"name":"total_rounds_map_de_safehouse","value":11},{"name":"total_rounds_map_de_sugarcane","value":2},{"name":"total_rounds_map_de_stmarc","value":39},{"name":"total_TR_defused_bombs","value":1},{"name":"total_gun_game_rounds_won","value":71},{"name":"total_gun_game_rounds_played","value":117},{"name":"total_wins_map_ar_monastery","value":4},{"name":"total_rounds_map_ar_shoots","value":20},{"name":"total_rounds_map_ar_baggage","value":8},{"name":"total_wins_map_ar_shoots","value":14},{"name":"total_wins_map_ar_baggage","value":4},{"name":"total_wins_map_de_lake","value":8},{"name":"total_wins_map_de_stmarc","value":28},{"name":"total_wins_map_de_safehouse","value":4},{"name":"total_matches_won","value":82},{"name":"total_matches_played","value":219},{"name":"total_gg_matches_won","value":31},{"name":"total_gg_matches_played","value":146},{"name":"total_progressive_matches_won","value":49},{"name":"total_trbomb_matches_won","value":1},{"name":"total_contribution_score","value":2459},{"name":"last_match_contribution_score","value":8},{"name":"last_match_rounds","value":18},{"name":"total_kills_hkp2000","value":101},{"name":"total_shots_hkp2000","value":2304},{"name":"total_hits_hkp2000","value":512},{"name":"total_hits_p250","value":188},{"name":"total_kills_p250","value":12},{"name":"total_shots_p250","value":679},{"name":"total_kills_sg556","value":125},{"name":"total_shots_sg556","value":1832},{"name":"total_hits_sg556","value":343},{"name":"total_hits_scar20","value":200},{"name":"total_kills_scar20","value":107},{"name":"total_shots_scar20","value":862},{"name":"total_shots_ssg08","value":48},{"name":"total_hits_ssg08","value":17},{"name":"total_kills_ssg08","value":8},{"name":"total_shots_mp7","value":1739},{"name":"total_hits_mp7","value":538},{"name":"total_kills_mp7","value":102},{"name":"total_kills_mp9","value":87},{"name":"total_shots_mp9","value":2510},{"name":"total_hits_mp9","value":512},{"name":"total_hits_nova","value":559},{"name":"total_kills_nova","value":76},{"name":"total_shots_nova","value":1830},{"name":"total_hits_negev","value":718},{"name":"total_kills_negev","value":58},{"name":"total_shots_negev","value":3810},{"name":"total_shots_sawedoff","value":1420},{"name":"total_hits_sawedoff","value":337},{"name":"total_kills_sawedoff","value":64},{"name":"total_shots_bizon","value":2362},{"name":"total_hits_bizon","value":693},{"name":"total_kills_bizon","value":91},{"name":"total_kills_tec9","value":62},{"name":"total_shots_tec9","value":594},{"name":"total_hits_tec9","value":224},{"name":"total_shots_mag7","value":1215},{"name":"total_hits_mag7","value":355},{"name":"total_kills_mag7","value":55},{"name":"total_gun_game_contribution_score","value":3815},{"name":"last_match_gg_contribution_score","value":0},{"name":"total_kills_m4a1","value":477},{"name":"total_kills_galilar","value":185},{"name":"total_kills_molotov","value":1},{"name":"total_shots_m4a1","value":8827},{"name":"total_shots_galilar","value":4161},{"name":"total_shots_taser","value":1},{"name":"total_hits_m4a1","value":1833},{"name":"total_hits_galilar","value":774},{"name":"total_rounds_map_ar_monastery","value":7},{"name":"total_matches_won_train","value":5},{"name":"total_matches_won_shoots","value":14},{"name":"total_matches_won_baggage","value":4},{"name":"total_matches_won_lake","value":8},{"name":"total_matches_won_stmarc","value":16},{"name":"total_matches_won_safehouse","value":4},{"name":"GI.lesson.csgo_instr_explain_buymenu","value":16},{"name":"GI.lesson.csgo_instr_explain_buyarmor","value":16},{"name":"GI.lesson.csgo_instr_explain_plant_bomb","value":16},{"name":"GI.lesson.csgo_instr_explain_bomb_carrier","value":1},{"name":"GI.lesson.bomb_sites_A","value":1},{"name":"GI.lesson.defuse_planted_bomb","value":1},{"name":"GI.lesson.csgo_instr_explain_follow_bomber","value":1},{"name":"GI.lesson.csgo_instr_explain_pickup_bomb","value":1},{"name":"GI.lesson.csgo_instr_explain_prevent_bomb_pickup","value":1},{"name":"GI.lesson.Csgo_cycle_weapons_kb","value":16},{"name":"GI.lesson.csgo_instr_explain_zoom","value":16},{"name":"GI.lesson.csgo_instr_explain_reload","value":16},{"name":"GI.lesson.tr_explain_plant_bomb","value":16},{"name":"GI.lesson.bomb_sites_B","value":1},{"name":"GI.lesson.version_number","value":16},{"name":"GI.lesson.find_planted_bomb","value":1},{"name":"GI.lesson.csgo_instr_rescue_zone","value":1},{"name":"GI.lesson.csgo_instr_explain_inspect","value":32}],"achievements":[{"name":"WIN_BOMB_PLANT","achieved":1},{"name":"KILL_ENEMY_LOW","achieved":1},{"name":"KILL_ENEMY_MED","achieved":1},{"name":"KILL_BOMB_DEFUSER","achieved":1},{"name":"WIN_BOMB_DEFUSE","achieved":1},{"name":"BOMB_PLANT_IN_25_SECONDS","achieved":1},{"name":"WIN_ROUNDS_LOW","achieved":1},{"name":"WIN_ROUNDS_MED","achieved":1},{"name":"GIVE_DAMAGE_LOW","achieved":1},{"name":"GIVE_DAMAGE_MED","achieved":1},{"name":"KILLING_SPREE","achieved":1},{"name":"KILL_WITH_OWN_GUN","achieved":1},{"name":"KILL_TWO_WITH_ONE_SHOT","achieved":1},{"name":"EARN_MONEY_LOW","achieved":1},{"name":"EARN_MONEY_MED","achieved":1},{"name":"KILL_ENEMY_ELITE","achieved":1},{"name":"KILL_ENEMY_FIVESEVEN","achieved":1},{"name":"KILL_ENEMY_FAMAS","achieved":1},{"name":"KILL_ENEMY_G3SG1","achieved":1},{"name":"KILL_ENEMY_UMP45","achieved":1},{"name":"KILL_ENEMY_TEAM","achieved":1},{"name":"LAST_PLAYER_ALIVE","achieved":1},{"name":"KILL_ENEMY_LAST_BULLET","achieved":1},{"name":"HEADSHOTS","achieved":1},{"name":"DAMAGE_NO_KILL","achieved":1},{"name":"KILL_LOW_DAMAGE","achieved":1},{"name":"KILL_ENEMY_RELOADING","achieved":1},{"name":"KILL_ENEMY_BLINDED","achieved":1},{"name":"KILL_ENEMIES_WHILE_BLIND","achieved":1},{"name":"WIN_KNIFE_FIGHTS_LOW","achieved":1},{"name":"HIP_SHOT","achieved":1},{"name":"KILL_SNIPER_WITH_SNIPER","achieved":1},{"name":"KILL_SNIPER_WITH_KNIFE","achieved":1},{"name":"KILL_SNIPERS","achieved":1},{"name":"KILL_WHEN_AT_LOW_HEALTH","achieved":1},{"name":"FAST_ROUND_WIN","achieved":1},{"name":"WIN_PISTOLROUNDS_LOW","achieved":1},{"name":"WIN_PISTOLROUNDS_MED","achieved":1},{"name":"WIN_BOMB_PLANT_AFTER_RECOVERY","achieved":1},{"name":"LOSSLESS_EXTERMINATION","achieved":1},{"name":"FLAWLESS_VICTORY","achieved":1},{"name":"WIN_DUAL_DUEL","achieved":1},{"name":"UNSTOPPABLE_FORCE","achieved":1},{"name":"IMMOVABLE_OBJECT","achieved":1},{"name":"HEADSHOTS_IN_ROUND","achieved":1},{"name":"WIN_MAP_DE_DUST2","achieved":1},{"name":"WIN_MAP_DE_INFERNO","achieved":1},{"name":"KILL_WHILE_IN_AIR","achieved":1},{"name":"KILL_ENEMY_IN_AIR","achieved":1},{"name":"BLOODLESS_VICTORY","achieved":1},{"name":"DONATE_WEAPONS","achieved":1},{"name":"KILL_BOMB_PICKUP","achieved":1},{"name":"DOMINATIONS_LOW","achieved":1},{"name":"DOMINATIONS_HIGH","achieved":1},{"name":"DOMINATION_OVERKILLS_LOW","achieved":1},{"name":"DOMINATION_OVERKILLS_HIGH","achieved":1},{"name":"REVENGES_LOW","achieved":1},{"name":"REVENGES_HIGH","achieved":1},{"name":"CONCURRENT_DOMINATIONS","achieved":1},{"name":"DOMINATION_OVERKILLS_MATCH","achieved":1},{"name":"EXTENDED_DOMINATION","achieved":1},{"name":"AVENGE_FRIEND","achieved":1},{"name":"GUN_GAME_KILL_KNIFER","achieved":1},{"name":"WIN_MAP_AR_SHOOTS","achieved":1},{"name":"WIN_MAP_DE_LAKE","achieved":1},{"name":"WIN_MAP_DE_STMARC","achieved":1},{"name":"GUN_GAME_ROUNDS_LOW","achieved":1},{"name":"WIN_GUN_GAME_ROUNDS_LOW","achieved":1},{"name":"WIN_GUN_GAME_ROUNDS_MED","achieved":1},{"name":"GUN_GAME_FIRST_KILL","achieved":1},{"name":"ONE_SHOT_ONE_KILL","achieved":1},{"name":"GUN_GAME_CONSERVATIONIST","achieved":1},{"name":"BASE_SCAMPER","achieved":1},{"name":"BORN_READY","achieved":1},{"name":"STILL_ALIVE","achieved":1},{"name":"KILL_ENEMY_HKP2000","achieved":1},{"name":"KILL_ENEMY_SCAR20","achieved":1},{"name":"KILL_ENEMY_SG556","achieved":1},{"name":"KILL_ENEMY_MAG7","achieved":1},{"name":"KILL_ENEMY_SAWEDOFF","achieved":1},{"name":"WIN_MAP_DE_TRAIN","achieved":1}]}}'
  return(data)
  #return(requests.get(URL).text)
  #return(urllib.request.urlopen(urlname).read().decode("utf-8")) #Read url
  
def sortJSON(start, arrayname, printdisplayname=False, printarray=False):
  length = len(start)
  #print(l)
  for items in l[1]['stats']:
    if items['name'][:length] == start:
      globals()[arrayname].append([items['name'],str(items['value'])])
  if printarray == True:
    if printdisplayname == True:
      print(arrayname + " is now being printed")
    print(globals()[arrayname])  
    
def calculateAccuracy(printaccuracy=False):
  for items in totalshots:
    if items[0] == "total_shots_hit" or items[0] == "total_shots_fired":
      pass
    else:
      for items2 in totalhits:
        if items[0][12:] == items2[0][11:]:
          accuracytemp = str(int(((float(items2[1])/float(items[1]))*100)))
          if printaccuracy:
            print("Accuaracy of " + items[0][12:] + " is: " + accuracytemp + "%")
          accuracy.append([items[0][12:], accuracytemp])

def calculateOverallAccuracy(printaccuracy=False):
  hits, shots, overallAccuracy = 0, 0, 0.0
  for items in totalshots:
    if items[0] == "total_shots_hit":
      hits = items
    if items[0] == "total_shots_fired":
      shots = items
  if shots != 0 and hits != 0:
    overallAccuracy = (float(int(hits[1]))/float(int(shots[1])))*100
    if printaccuracy:
      print(overallAccuracy)
    return(overallAccuracy)
  else:
    print("Couldn't find both total_shots_hit and total_shots_fired :?")
    
def tempDefDisplayOutput():
  laststats = ['76561198072165784', '1427495382.7117717', '19.63553029241639', "[['deagle', '25'], ['glock', '21'], ['elite', '22'], ['fiveseven', '18'], ['awp', '37'], ['ak47', '16'], ['aug', '36'], ['famas', '17'], ['g3sg1', '16'], ['p90', '25'], ['mac10', '27'], ['ump45', '18'], ['xm1014', '19'], ['m249', '36'], ['hkp2000', '25'], ['p250', '18'], ['sg556', '16'], ['scar20', '31'], ['ssg08', '32'], ['mp7', '53'], ['mp9', '27'], ['nova', '18'], ['negev', '24'], ['sawedoff', '13'], ['bizon', '24'], ['tec9', '19'], ['mag7', '18'], ['m4a1', '22'], ['galilar', '14']]\n"]
  local1 = str(time.ctime(int(float(time.time()))))
  local2 = str(time.ctime(int(float(laststats[1]))))
  allAccuracy1 = str(int(overallAcc))
  allAccuracy2 = str(int(float(laststats[2])))
  lastAccuracy = ast.literal_eval(laststats[3])
  index = 0
  for items in lastAccuracy:
    accuracy[index].append(items[0])
    accuracy[index].append(str(items[1]))
    accuracy[index].append(int(accuracy[index][3])-int(accuracy[index][1]))
    index = index + 1
  accuracy.append(["overall", allAccuracy1, "overall", allAccuracy2, str(int(allAccuracy2)-int(allAccuracy1))])
  accuracy.insert(0, ["Gun (now)", "Accuracy", "Gun (last)", "Accuracy", "+/-"])
  print("Current Time: " + local1)
  print("Last Time: " + local2)
  return(accuracy)
  #print(tabulate(accuracy, headers="firstrow", tablefmt="fancy"))

def getData():
  global overallAcc
  jsondata = json.loads(urlRequest(URL)) #Actual Data
  [l.extend([k,v]) for k,v in jsondata.items()] #I really have no idea
  
  sortJSON("total_shots", "totalshots", False, False)
  sortJSON("total_hits", "totalhits", False, False)
  sortJSON("total_kills", "totalkills", False, False)
  calculateAccuracy(False)
  overallAcc = calculateOverallAccuracy(False)  

def fileExists():
  #Make sure the file exists
  if os.path.isfile("data.txt") == False:
    with open('data.txt', 'w+') as file:
      pass
  
def runProgram():
  global steamID
  resetData()
  steamID = resolveVanity("pB")
  getData()
  fileExists()
  readFiles()
  
  with open('data.txt', 'r') as file:
    contents = file.readlines()
  for items in contents:
    fileData.append(items.split('`'))
  
  for items in fileData:
    fsteamid = items[0]
    ftimestamp = items[1]
    foveraccuracy = items[2]
    fgunaccuracy = items[3]
    if fsteamid == steamID:
      farray.append([fsteamid, ftimestamp, foveraccuracy, fgunaccuracy])
  
  for items in farray:
    global tempmax
    if float(items[1]) > tempmax:
      tempmax = float(items[1])
      
  for items in farray:
    if float(items[1]) == tempmax:
      laststats = items
  
  with open('data.txt', 'a') as file:
    file.write(steamID + "`" + str(time.time()) + "`" + str(overallAcc) + "`" + str(accuracy) + "\n") 
  
  fulldata = tempDefDisplayOutput()
  return(fulldata)
  
def readFiles():
  with open('data.txt', 'rb') as file:
    fileLines = file.readlines()
    for line in range(len(fileLines)):
      fileLines[line] = str(fileLines[line])
      fileLines[line] = fileLines[line][:-1]
      fileLines[line] = fileLines[line][2:]
      fileLines[line] = fileLines[line].split("`")
      print(fileLines[line][3])
      fileLines[line][3] = eval(fileLines[line[3]])
    print(fileLines[0])