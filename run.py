import gspread

from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figure input from user
    """
    print("Please enter sales data from the last market.")
    print("Data should be 6 numbers, seperated by commas")
    print("Example: 1,2,3,4,5,6")

    data_str = input("Enter data here: ")
    sales_data = data_str.split(",")

    validate_data(sales_data)

def validate_data(values):
    """
    Inside the try, covnerts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")

get_sales_data()