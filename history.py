import sys
from classes.HistoryHandler import HistoryHandler, HistoryHandlerException
from classes.OptionParser import OptionParser


args = [arg for arg in sys.argv]
opt = OptionParser(args)

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
