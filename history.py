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
        return arg


parser = argparse.ArgumentParser()

addHelpStr = 'Adds a file to the program database'
diffHelpStr = 'Differentiate two sets of revisions'
verbHelpStr = 'Prints diff with set of additional information, helpful in e.g. displaying in GUI '

parser.add_argument('-a', '--add', nargs=1, type=is_valid_file, help=addHelpStr, required=False)
# TODO Add custom check to differentiate 1 string and 2 ints
parser.add_argument('-d', '--diff', nargs=3, type=str, help=diffHelpStr, required=False)
parser.add_argument('-v', '--verbose', nargs='*', help=verbHelpStr, required=False)

opt = OptionParser(vars(parser.parse_args()))

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

    history_handler.print_diff(opt)
