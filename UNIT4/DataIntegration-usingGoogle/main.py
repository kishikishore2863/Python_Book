import gspread
from google.oauth2.service_account import Credentials
from collections import Counter

SERVICE_ACCOUNT_FILE ="Admin.json"
SHEET_URL = "https://docs.google.com/spreadsheets/d/1n0EDQUnQqpUVFHLcZzPWg01jfE-rIYtU9KqZGVqTU6g/edit?usp=sharing"
WORKSHEET_NAME="Sheet4"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open_by_url(SHEET_URL)
worksheet = sheet.worksheet(WORKSHEET_NAME)
data = worksheet.get_all_values()
print(data)

# //get the channel preference
def get_channel_preferences():
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_url(SHEET_URL)
    ws=spreadsheet.worksheet(WORKSHEET_NAME)
    rows = ws.get_all_values()
    if not  rows:
        raise  RuntimeError("No data was found in the sheet")
    header = rows[0]
    idx = header.index("ChannelPreference")
    data_rows=rows[1:]
    if "ChannelPreference" not in header:
        raise RuntimeError("Column 'ChannelPreference' was not found in the header row.")
    prefs=[]
    for r in data_rows:
        if len(r)>idx:
            val = r[idx].strip()
            if val !="":
                prefs.append(val)
    counts = Counter(prefs)
    print("ChannelPreference values")
    for p in prefs:
        print(p)
    print("\nChannelPreference counts")
    for k,v in counts.most_common():
        print(f"{k}:{v}")
    return prefs, counts