"""Convenience functions for interacting with data in the
Google Drive
Author: Gergely Turi
"""

import gspread
import pandas as pd
from google.auth import default
from google.colab import auth

BASE_DATA_PATH = "/gdrive/Shareddrives/Turi_lab/Data/pilocybin_project/PCB_pupil"


def useful_datasets():
    """Return a list of useful datasets."""
    auth.authenticate_user()
    creds, _ = default()
    gc = gspread.authorize(creds)

    worksheet = gc.open("pupil_data_to_analyze").sheet1

    # get_all_values gives a list of rows.
    rows = worksheet.get_all_values()

    # Convert to a DataFrame and render.
    return pd.DataFrame.from_records(rows[1:], columns=rows[0])


def return_exp_path():
    """Return the path to the experiment data.    

    Returns:
        str: The path to the experiment data on google drive.
    """
    try:
        return BASE_DATA_PATH
    except Exception as e:
        return e
