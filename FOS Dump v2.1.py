'''
First attempt to pull JSON data out of a decrypted Fallout Shelter save file

'''
import json, os

def invDump(vData):
    # define desired fields
    fields = ('id', 'type', 'extraData')
    
    # define field labels
    labels = ('id', 'type', 'uniqueName', 'bonus', 'bonusValue')
    
    # print field headers
    inv = ','.join(labels) + '\n'
    #print(inv)
    
    # print the (fields) of <item>
    for item in vData['vault']['inventory']['items']:
        #print(item)
        inv += item[fields[0]]
        #print(fields[0])
        #print(fields[1])
        for field in range(1, len(fields)):
            #print(field)
            try:
                if fields[field] == 'extraData':
                    #print(list(item[fields[field]].keys()))
                    inv += ',' + ','.join([str(item[fields[field]][key]) for key in list(item[fields[field]].keys())])
                else:
                    inv += ',' + str(item[fields[field]])
            except KeyError:
                #inv += ',Error: KeyError: Field: ' + fields[field]
                pass
        inv += '\n'
            
    with open('inv.csv', 'w', encoding='utf-8') as csv:
        csv.write(inv)
    
    print("Wrote inv.csv")


def getRoom(vData, roomId):
    rooms = vData['vault']['rooms']
    room = ''
    if roomId == -1:
        room = ""
    else:
        i = 0
        while room == '':
            if rooms[i]['deserializeID'] == roomId:
                room = rooms[i]['type']
            i += 1
    return room

    
def getInQueue(vData, dID):
    teams = vData['vault']['wasteland']['teams']
    q = ''
    i = 0
    while q == '':
        if teams[i]['dwellers'].count(dID):
            q = teams[i]['status']
        if i >= len(teams[i]['dwellers']):
            q = 'No'
        i += 1
    return q


def getExploring(vData, dID):
    if getInQueue(vData, dID) == 'No':
        return 'No'
    else:
        return 'Yes'
    
    
def dwellerDump(vData):
    headers = ['ID', 'Name', 'Last Name', 'Happiness', 'Health', 'maxHealth', 'Rads', 'Level', 'XP', 'Gender', 'Rarity', 'S', 'P', 'E', 'C', 'I', 'A', 'L', 'Weapon ID', 'Outfit ID', 'Pet ID', 'Pet Type', 'Pet Name', 'Pet Bonus', 'Pet Bonus Value', 'Room Assignment', 'Exploring?', 'In Queue?', 'Pregnant?', 'Baby Ready?']
    
    # print field headers
    pop = ','.join(headers) + '\n'
    #print(pop)
    
    # print the (fields) of <dweller>
    for dweller in vData['dwellers']['dwellers']:
        pop += str(dweller['serializeId'])
        pop += ',' + dweller['name']
        pop += ',' + dweller['lastName']
        pop += ',' + str(dweller['happiness']['happinessValue'])
        pop += ',' + str(dweller['health']['healthValue'])
        pop += ',' + str(dweller['health']['maxHealth'])
        pop += ',' + str(dweller['health']['radiationValue'])
        pop += ',' + str(dweller['experience']['currentLevel'])
        pop += ',' + str(dweller['experience']['experienceValue'])
        pop += ',' + 'M' if dweller['gender']==2 else ',F'
        pop += ',' + dweller['rarity']
        for i in range(1, len(dweller['stats']['stats'])):
            pop += ',' + str(dweller['stats']['stats'][i]['value'])
        pop += ',' + dweller['equipedWeapon']['id']
        pop += ',' + dweller['equipedOutfit']['id']
        try: #because not every dweller will have a pet
            pop += ',' + dweller['equippedPet']['id']
            pop += ',' + dweller['equippedPet']['type']
            pop += ',' + dweller['equippedPet']['extraData']['uniqueName']
            pop += ',' + dweller['equippedPet']['extraData']['bonus']
            pop += ',' + str(dweller['equippedPet']['extraData']['bonusValue'])
        except KeyError:
            pop += ',,,,,'
        pop += ',' + getRoom(vData, dweller['savedRoom'])
        pop += ',' + getExploring(vData, dweller['serializeId'])
        pop += ',' + getInQueue(vData, dweller['serializeId'])
        pop += ',' + str(dweller['pregnant'])
        pop += ',' + str(dweller['babyReady'])
        
        pop += '\n'
        
    with open('dweller.csv', 'w', encoding='utf-8') as csv:
        csv.write(pop)
    print("Wrote dweller.csv")


#def decryptSAV(savFile):
    

    
def resDump(vData):
    res = vData['vault']['storage']['resources']
    
    stuff = str(res['Nuka']) + '\n'
    stuff += str(res['Food']) + '\n'
    stuff += str(res['Water']) + '\n'
    stuff += str(res['Energy']) + '\n'
    stuff += str(res['StimPack']) + '\n'
    stuff += str(res['RadAway']) + '\n'
    stuff += str(vault['vault']['LunchBoxesByType'].count('0')) + '\n'
    stuff += str(vault['vault']['LunchBoxesByType'].count('1')) + '\n'
    stuff += str(vault['vault']['LunchBoxesByType'].count('2')) + '\n'
    stuff += str(res['NukaColaQuantum']) + '\n'
    
    with open('resources.csv', 'w', encoding='utf-8') as csv:
        csv.write(stuff)
    
    print("Wrote resources.csv")


if __name__ == '__main__':
    #with open('Vault1.sav', mode="rb") as save:
    #    savData = save.readall()
    
    #decrypted = decryptSAV(savData)
    #with open
    
    # load data from the vault   /// sys.arv[0]
    with open('Vault1.json', encoding="utf-8") as vault:
        vaultData = json.load(vault)
        
    
    invDump(vaultData)
    dwellerDump(vaultData)
    resDump(vaultData)