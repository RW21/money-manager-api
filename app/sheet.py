import gspread
import datetime
from collections import defaultdict
from dataclasses import dataclass
import os

# config
current_sheet = str(datetime.date.today().year)
# sheet_key = "1A-UI02Q3fRV-yQCywTT3taW--5b3ILFtAbgrMlkC0ts"
sheet_key = os.environ.get('SHEET_KEY')
gc = gspread.service_account(filename="auth.json")
file = gc.open_by_key(sheet_key)
categories = defaultdict(list)
for category in filter(lambda x: x != '', file.worksheet('Categories').col_values(1)[1:]):
    parent, child = category.split(', ')
    categories[parent].append(child)

# open sheet
current_working_sheet = file.worksheet(current_sheet)


def get_base_row(month):
    if month == 1:
        return 1
    return (month - 1) * 6


def get_latest_col(month):
    return len(current_working_sheet.col_values(get_base_row(month))) + 1


@dataclass
class Entry:
    description: str
    date: datetime.date
    amount: int
    category_parent: str
    category_child: str
    is_income: bool


test_entry = Entry(description="test", date=datetime.date(2021, 2, 17),
                   amount=12, category_child='Fun', category_parent='Food', is_income=False)


def add_entry(entry: Entry):
    latest = get_latest_col(entry.date.month)
    base_x = get_base_row(entry.date.month)
    # date
    current_working_sheet.update_cell(latest, base_x, entry.date.day)
    # name
    current_working_sheet.update_cell(latest, base_x + 1, entry.description)
    # category
    current_working_sheet.update_cell(latest, base_x + 2, f"{entry.category_parent}, {entry.category_child}")
    # amount
    if entry.is_income:
        current_working_sheet.update_cell(latest, base_x + 4, entry.amount)
    else:
        current_working_sheet.update_cell(latest, base_x + 3, entry.amount)


