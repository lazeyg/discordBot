import gspread, datetime, time

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1bAoofoXM3ItQ5gvjHtyn6TzcCLrkRfhZIdyU3HJv-Ew')
NhPlayersSheet = gc.open("NH Players Info")
wks = NhPlayersSheet.worksheet('DiscordTags')
wksGetAll = NhPlayersSheet.worksheet('GetAll')
worksheet = sh.sheet1

def finduser(res):
    res = worksheet.find(res)

#update cell Parameters : Line , Column , "str to update" ex: A2 = update_cell(1,2,'str to update')
def writecell(line, col, res):
    wks.update_cell(line, col, res)

def updateCell(cell,user):
    wks.update(cell,user)

def getAll(line, col, res):
    time.sleep(1)
    wksGetAll.update_cell(line, col, res)

def getHighestMmr(n):
    my_date = datetime.date.today() # if date is 01/01/2018
    yr,weekNumber,weekDay = my_date.isocalendar()
    msg   = wks.acell('A' + str(n)).value
    user  = wks.acell('B' + str(n)).value
    rank  = wks.acell('C' + str(n)).value
    user2 = wks.acell('D' + str(n)).value
    rank2 = wks.acell('E' + str(n)).value
    user3 = wks.acell('F' + str(n)).value
    rank3 = wks.acell('G' + str(n)).value
    mentionuser  = '<@!{}>'.format(user)
    mentionuser2 = '<@!{}>'.format(user2)
    mentionuser3 = '<@!{}>'.format(user3)
    msg2 = msg.replace('#I1D' , str(mentionuser))
    msg3 = msg2.replace('#I2D', str(mentionuser2))
    msg4 = msg3.replace('#I3D', str(mentionuser3))    
    msg5 = msg4.replace('#R1nk', str(rank))
    msg6 = msg5.replace('#R2nk', str(rank2))
    msg7 = msg6.replace('#R3nk', str(rank3))
    finalmsg = msg7.replace('#Week', str(weekNumber))
    return finalmsg