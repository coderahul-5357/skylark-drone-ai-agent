import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_client():
    creds = Credentials.from_service_account_file(
        "credentials.json",
        scopes=SCOPES
    )
    return gspread.authorize(creds)

def read_sheet(sheet_name):
    client = get_client()
    sheet = client.open(sheet_name).sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def update_pilot_status(pilot_name, new_status):
    client = get_client()
    sheet = client.open("pilot_roster").sheet1
    records = sheet.get_all_records()

    for i, row in enumerate(records):
        if row["name"].lower() == pilot_name.lower():
            status_column_index = list(row.keys()).index("status") + 1
            sheet.update_cell(i + 2, status_column_index, new_status)
            return True

    return False
