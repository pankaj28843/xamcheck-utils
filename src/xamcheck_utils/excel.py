# Third Party Stuff
import xlrd
from xamcheck_utils.exceptions import ValidationError


def get_workbook(workbook_file):
    """Opens the excel file whose name"""
    error_messages = []

    try:
        workbook = xlrd.open_workbook(file_contents=workbook_file)
    except xlrd.XLRDError as e:
        error_messages.append(e.message)
        raise ValidationError(error_messages)

    return workbook


def get_worksheet_by_index(workbook, index=0):
    """Returns worksheet having the specified index"""
    error_messages = []

    try:
        worksheet = workbook.sheet_by_index(index)
    except IndexError as e:
        error_messages.append(e.message)
        raise ValidationError(error_messages)

    return worksheet


def get_worksheet_by_name(workbook, sheet_name):
    """Returns worksheet with the given name
        in the given workbook"""
    error_messages = []

    try:
        worksheet = workbook.sheet_by_name(sheet_name)
    except IndexError as e:
        error_messages.append(e.message)
        raise ValidationError(error_messages)

    return worksheet


def validate_worksheet_size(worksheet, min_cols, min_rows):
    """ Validates the size of the worksheet to verify
        the minimum number of rows and columns
    """
    error_messages = []

    ncols = worksheet.ncols
    nrows = worksheet.nrows

    if ncols < min_cols:
        error_messages.append('Invalid worksheet - atleast {0} columns must '
                              'be present.'.format(min_cols))
        raise ValidationError(error_messages)

    if nrows < min_rows:
        error_messages.append('Invalid worksheet - atleast {0} rows must be '
                              'present.'.format(min_rows))
        raise ValidationError(error_messages)


def get_first_worksheet(workbook_file, min_cols=0, min_rows=0):
    """ Returns the first worksheet of the specified workbook"""
    workbook = get_workbook(workbook_file)
    worksheet = get_worksheet_by_index(workbook, index=0)

    if min_cols > 0 and min_rows > 0:
        validate_worksheet_size(worksheet, min_cols, min_rows)

    return worksheet


def get_worksheet_by_name_from_file(workbook_file, sheet_name, min_cols=0, min_rows=0):
    """ Returns the worksheet with the given name and
        workbook file
    """
    workbook = get_workbook(workbook_file)
    worksheet = get_worksheet_by_name(workbook, sheet_name)

    if min_cols > 0 and min_rows > 0:
        validate_worksheet_size(worksheet, min_cols, min_rows)

    return worksheet
