'''
First attempt to pull JSON data out of a decrypted Fallout Shelter save file

'''
import json, os#, sys

def InvDump(vData):
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
                inv += 'Error: KeyError\n'
    
        inv += '\n'
        
            
    with open('inv.csv', 'w', encoding='utf-8') as csv:
        csv.write(inv)
    
    #print("Wrote inv.csv")

def parseJSONList(obj, fields, str):
    for thing in obj:
        for field in fields:
            if type(thing[fields[field]]) == list:
                
        #if type(fields[1]) == list:
        
def getRoom(vData):
    

def DwellerDump(vData):
    '''# define desired fields
    fields = ('serializeId',
            'name',
            'lastName',
            ('happiness','happinessValue'),
            ('health', 'healthValue', 'maxHealth', 'radiationValue'),
            ('experience','currentLevel', 'experienceValue'),
            'gender',
            'rarity',
            'stats', #special case, values don't have labels
            ('equipedWeapon', 'id'),
            ('equipedOutfit', 'id'),
            ('equippedPet', 'id', 'type', #careful, they don't always have this dict
                ('extraData', 'uniqueName', 'bonus', 'bonusValue')),
            'savedRoom', #need unique function for this one
            'Explo
            )
    '''
    chart = ['ID', 'Name', 'Last Name', 'Happiness', 'Health', 'maxHealth', 'Rads', 'Level', 'XP', 'Gender', 'Rarity', 'S', 'P', 'E', 'C', 'I', 'A', 'L', 'Weapon ID', 'Outfit ID', 'Pet ID', 'Pet Type', 'Pet Name', 'Pet Bonus', 'Pet Bonus Value', 'Room Assignment', 'Exploring?', 'In Queue?']
    
    # print field headers
    pop = ','.join(fields) + '\n'
    #print(pop)
    
    # print the (fields) of <dweller>
    for dweller in vData['dwellers']['dwellers']:
        #print(dweller)
        pop += dweller[fields[0]]

        for field in range(1, len(fields)):
            #print(field)
            try:
                if fields[field] == 'extraData':
                    #print(list(dweller[fields[field]].keys()))
                    pop += ',' + ','.join([str(dweller[fields[field]][key]) for key in list(dweller[fields[field]].keys())])
                else:
                    pop += ',' + str(dweller[fields[field]])
            except KeyError:
                pop += 'Error: KeyError: {0}\n'.format(str(dweller[fields[field]]))
    
        pop += '\n'
        
            
    with open('dweller.csv', 'w', encoding='utf-8') as csv:
        csv.write(pop)
    
    #print("Wrote dweller.csv")

if __name__ == __main__:
    # load data from the vault   /// sys.arv[0]
    with open('Vault1.json', encoding="utf-8") as vault:
        vaultData = json.load(vault)
    
    InvDump(vaultData)
    #DwellerDump(vaultData)
    
    