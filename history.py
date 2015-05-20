from classes.HistoryHandler import HistoryHandler, HistoryHandlerException
from classes.OptionParser import OptionParser

import argparse
import os
import sys

# TODO Find more appropriate place for this function
def is_valid_file(arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return is_valid_file

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--add', nargs=1, type=is_valid_file, help='Adds a file to the program database',
                    required=False)
parser.add_argument('-d', '--diff', nargs=3, type=str, help='Differentiate two sets of revisions', required=False)  # TODO Add custom check to differentiate 1 string and 2 ints

# TODO Have to work on that, not sure how to create an arg without a variable
# parser.add_argument('-v', '--verbose', nargs=1, help='???',  required=False, default=argparse.SUPPRESS)

args = parser.parse_args()

opt = OptionParser(vars(args))

if opt.is_add:
    try:
        HistoryHandler.add_to_history(opt.file_path)
    except HistoryHandlerException as e:
        sys.exit()

if opt.is_diff:
    history_handler = HistoryHandler()

    try:
        history_handler.generate_diff(opt.file_path, opt.revision_id_1, opt.revision_id_2)
    except HistoryHandlerException as e:
        sys.exit()

    history_handler.print_diff(opt.is_verbose)
