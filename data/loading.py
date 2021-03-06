from csv import DictReader
from functools import partial

from six import iteritems


def load_from_csv(path_to_csv, exclude_cols=None):
    """
    Load a CSV and return a list of dicts, one dict for each row of
    the form {column_header1: <value>, column_header2: <value>, ...}
    :param path_to_csv: path to CSV file
    :param exclude_cols: iterable of columns to exclude (often the target variable)
    """
    with open(path_to_csv, 'r') as csvfile:
        data = list(DictReader(csvfile))
    if exclude_cols is not None:
        if isinstance(exclude_cols, str):
            exclude_cols = {exclude_cols}
        filt = partial(filter_keys, fields=set(exclude_cols))
        return [filt(rec) for rec in data]
    return data


def filter_keys(record, fields):
    """
    Filter keys from a dict
    :param record: dict
    :param fields: set of strings indicating fields to drop
    :return:
    """
    return {k: v for k, v in iteritems(record) if k not in fields}
