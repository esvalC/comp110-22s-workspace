"""Dictionary related utility functions."""

__author__ = "730482131"

# from calendar import c
from csv import DictReader
# from sqlite3 import Row


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of csv into a table."""
    result: list[dict[str, str]] = []
    
    # Open a handlt to the data file
    file_handle = open(filename, "r", encoding="utf8")\

    # Read the file as csv instead of just strings
    csv_reader = DictReader(file_handle)

    # Read each row of CSV row by row
    for row in csv_reader:
        result.append(row)

    # Close file when ur done to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Take N number of the first values in the tables column."""
    result: dict[str, list[str]] = {}
    
    for column in table:
        row_list: list[str] = []
        single_column = table[column]
        if rows > len(single_column):
            rows = len(single_column)
        for i in range(rows):
            row_list.append(single_column[i])
        result[column] = row_list

    return result


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce tables with desired columns."""
    result: dict[str, list[str]] = {}

    for items in names:
        result[items] = column_table[items]

    return result


def concat(first_table: dict[str, list[str]], second_table: dict[str, list[str]]) -> dict[str, list[str]]:
    """Makes two tables one."""
    result: dict[str, list[str]] = {}

    for column in first_table:
        result[column] = first_table[column]
    for column in second_table:
        if column in result:
            for name in column:
                if name not in result[column]:
                    result[column].append(name)
        result[column] = second_table[column]

    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the amount of each value."""
    result: dict[str, int] = {}

    for word in values:
        if word in result:
            result[word] += 1
        elif word not in result:
            result[word] = 1

    return result