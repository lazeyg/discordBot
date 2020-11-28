import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1bAoofoXM3ItQ5gvjHtyn6TzcCLrkRfhZIdyU3HJv-Ew')
wks = gc.open("NH Players Info").worksheet('DiscordTags')
worksheet = sh.sheet1

def finduser(res):
    res = worksheet.find(res)

def writecellA(line , res):
    #update cell Parameters : Line , Column , "str to update" ex: A2 = update_cell(1,2,'str to update')
    wks.update_cell(line, 1, res)

def writecellB(line , res):
    wks.update_cell(line, 2, res)

def checkrank1s(user):
    wks.update('A10', user)

def checkrank2s(user):
    wks.update('A14', user)

def checkrank3s(user):
    wks.update('A18', user)

def checkrank(user):
    wks.update('A22',user)

def checkcountry(user):
    wks.update('A26',user)

def matchmake(user):
    wks.update('A30',user)

def addfriend(user):
    wks.update('B34',user)