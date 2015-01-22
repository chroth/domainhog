import sys
import logging
import data_handler

def update_data(context):
    print 'Update data'
    data_handler.update()

    return 0, ""

def search(context):
    if not data_handler.has_data():
        context["logger"].debug("Data is missing")
        update_data(context)

    search_word = context['arguments'][1]
    print 'Starting search for ' + search_word

    all_tlds = data_handler.get_tlds()
    hits = 0

    for tld_item in all_tlds:
        domain_suggestion = tld_item.get_suggestion(search_word)
        if domain_suggestion:
            print domain_suggestion
            hits = hits + 1

    if hits == 0:
        print 'No hits'

    return 0, ""

def show_help(context):
    context["logger"].debug("Display API help")
    msg = "BPM Commands:\n"
    keys = sorted(context['api'].keys())
    for k in keys:
        msg += "    {:17s} {:s}\n".format(k, context['api'][k][1])
    return 0, msg.strip()


if __name__ == "__main__":
    #default command
    command = "help"
    try:
        command = sys.argv[1]
    except IndexError as e:
        pass

    # setup logger
    FORMAT = "%(asctime)s %(levelname)s %(funcName)s:%(lineno)s ~ %(message)s"
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    #available commands
    api = {
        'update': (update_data, "Updates tld information"),
        'search': (search, "Searches for an available domain name"),
        'help': (show_help, "Show available commands"),
    }

    #context for all commands
    context = {
        'logger': logger,
        'command': command,
        'arguments': sys.argv[1:],
        'api': api
    }

    #excecute, returns code (!= 0 if failed) and a message
    if not command in api:
        command = 'help'

    code, msg = api[command][0](context)
    print msg
    sys.exit(code)
