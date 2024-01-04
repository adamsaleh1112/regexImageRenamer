import gspread # allows spreadsheet writing through python
from oauth2client.service_account import ServiceAccountCredentials # library allows for service account credentials to be given
import time # importing time to allow pauses when updating the sheets

scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"] # setting scope of api contact
saf = "serviceaccount.json" # setting destination of service account json
credentials = ServiceAccountCredentials.from_json_keyfile_name(saf, scopes) # initializing credentials to api
auth = gspread.authorize(credentials) # authorizing credentials


# WRITE DATA TO SPREADSHEET FUNCTION
def tospread(aob,data): # aob defines which column (a or b) and data is the lists of names

    ss = auth.open("PWPSheets") # opening spreadsheet which is shared with the authorized credentials
    ws = ss.get_worksheet(0) # 0 is default worksheet
    row = 1 # starts appending to spreadsheet at row 1 at the specified column

    for filename in data: # iterating through the data lists of filenames

        ws.update_cell(row, aob, filename) # updates the specified cell with the specified data
        row += 1 # adds to the row variable which will then add to the next row on the next iteration

        time.sleep(1) # wait one second because api has a request rate (RATE_LIMIT_EXCEEDED)
