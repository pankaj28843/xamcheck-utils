from __future__ import unicode_literals

# Standard Library
from os.path import abspath, dirname, join, normpath
from unittest import TestCase

# Third Party Stuff
from xamcheck_utils.exceptions import ValidationError

# Xamcheck-Utils Stuff
from xamcheck_utils import excel

CURRENT_DIR = dirname(abspath(__file__))
EXCEL_FILES_ROOT = normpath(join(CURRENT_DIR, 'data/excel-files'))

excel_file_path = normpath(join(EXCEL_FILES_ROOT, "excel1.xlsx"))

with open(excel_file_path, 'rb') as excel_file:
    excel_file_contents = excel_file.read()
    workbook = excel.get_workbook(excel_file_contents)


class TestUtilsExcelUtils(TestCase):

    def test_get_workbook(self):
        workbook = excel.get_workbook(excel_file_contents)
        self.assertEqual(workbook.sheet_names(), [u'Sheet1'])

    def test_get_worksheet_by_index(self):
        worksheet = excel.get_worksheet_by_index(workbook, 0)
        self.assertEqual(worksheet.columns_from_right_to_left, 0)

    def test_get_worksheet_by_name(self):
        worksheet = excel.get_worksheet_by_name(workbook, 'Sheet1')
        self.assertEqual(worksheet.columns_from_right_to_left, 0)

    def test_validate_worksheet_size(self):
        worksheet = workbook.sheet_by_index(0)
        items = (
            (worksheet, 0, 3),
            (worksheet, 3, 0),
        )
        for (worksheet, min_cols, min_rows) in items:
            with self.assertRaises(ValidationError):
                excel.validate_worksheet_size(
                    worksheet, min_cols, min_rows)

    def test_get_worksheet_by_name_from_file(self):
        worksheet = excel.get_worksheet_by_name_from_file(
            excel_file_contents, 'Sheet1')
        self.assertEqual(worksheet.columns_from_right_to_left, 0)
        items = (
            (excel_file_contents, 'Sheet1', 1, 1),
        )
        for (workbook_file, sheet_name, min_cols, min_rows) in items:
            with self.assertRaises(ValidationError):
                excel.get_worksheet_by_name_from_file(
                    workbook_file, sheet_name, min_cols, min_rows)

    def test_get_first_worksheet(self):
        worksheet = excel.get_first_worksheet(
            excel_file_contents, 0, 0)
        self.assertEqual(worksheet.columns_from_right_to_left, 0)
        items = (
            (excel_file_contents, 1, 1),
        )
        for (workbook_file, min_cols, min_rows) in items:
            with self.assertRaises(ValidationError):
                excel.get_first_worksheet(
                    workbook_file, min_cols, min_rows)
