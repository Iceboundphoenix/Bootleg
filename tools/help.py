from tools import variables as var
from tools import constants as con
from tools.logger import help

def get_help(helping=""):
    helping = helping.lower()
    help("")
    help("               - Final Fantasy VII Bootleg Mod Configurator -")
    help("                                * Help file *")
    help("")
    if helping and helping not in con.POSSIBLE_HELP and helping not in con.HIDDEN_HELP:
        help("'{0}' is not a valid help topic.".format(helping))
        if con.POSSIBLE_HELP:
            help("Possible help topic{1}: {0}.".format(", ".join(con.POSSIBLE_HELP), "s" if len(con.POSSIBLE_HELP) > 1 else ""))
            if (con.HIDDEN_HELP and var.DEBUG_MODE) or (con.HIDDEN_HELP and var.SHOW_HIDDEN_HELP):
                help("Hidden help command{1}: {0}.".format(", ".join(con.HIDDEN_HELP), "s" if len(con.HIDDEN_HELP) > 1 else ""))
            help("Use 'help <item>' to view a specific help.")
    elif not helping:
        if con.CURRENT_RELEASE:
            help("Bootleg - Final Fantasy VII Configurator - Version {0}".format(con.CURRENT_RELEASE))
        if con.RELEASE_INFO and con.BUILD_INFO:
            help(con.BUILD_INFO + " build " + con.RELEASE_INFO)
        if con.FIRST_DEV:
            help("First developper{1} and base idea: {0}.".format(", ".join(con.FIRST_DEV), "s" if len(con.FIRST_DEV) >1 else ""))
        if con.USER_HELP:
            help("User helper{0} and support team: {1}.".format("s" if len(con.USER_HELP) > 1 else "", ", ".join(con.USER_HELP)))
        if con.CODERS:
            help("Current active programmer{0} and developper{0}: {1}.".format("s" if len(con.CODERS) > 1 else "", ", ".join(con.CODERS)))
        if con.GUI_CODERS:
            help("Programming of the Graphical User Interface (GUI): {0}.".format(", ".join(con.GUI_CODERS)))
        if con.PROCESS_CODERS:
            help("Programming of the Bootleg process: {0}.".format(", ".join(con.PROCESS_CODERS)))
        if con.GAME_CONV:
            help("Game Converter developping and support: {0}.".format(", ".join(con.GAME_CONV)))
        if con.BETA_TESTERS:
            help("Beta tester{0}: {1}.".format("s" if len(con.BETA_TESTERS) > 1 else "", ", ".join(con.BETA_TESTERS)))
        if con.SPECIAL_THANKS:
            help("Special thanks to: {0}.".format(", ".join(con.SPECIAL_THANKS)))
        if con.EMAIL:
            help("Official Bootleg email for support and questions: {0}".format(con.EMAIL))
        if con.POSSIBLE_HELP:
            help("")
            help("Possible help topic{1}: {0}.".format(", ".join(con.POSSIBLE_HELP), "s" if len(con.POSSIBLE_HELP) > 1 else ""))
            if (con.HIDDEN_HELP and var.DEBUG_MODE) or (con.HIDDEN_HELP and var.SHOW_HIDDEN_HELP):
                help("Hidden help command{1}: {0}.".format(", ".join(con.HIDDEN_HELP), "s" if len(con.HIDDEN_HELP) > 1 else ""))
            help("Use 'help <item>' to view a specific help.")
    elif helping == "programming":
        msg = "The current version of Bootleg is coded in Python 3.2"
        if con.PROCESS_CODERS:
            msg = msg + " by {0}".format(", ".join(con.PROCESS_CODERS))
        msg = msg + ".\nThe Graphical User Interface is coded in C#"
        if con.GUI_CODERS:
            msg = msg + " by {0}".format(", ".join(con.GUI_CODERS))
        help(msg + ".")
    elif helping == "code":
        msg = "The {0}{1}Bootleg code is completely open-source".format(con.CURRENT_RELEASE, " " if con.CURRENT_RELEASE else "")
        if con.PROCESS_CODE:
            msg = msg + ", and can be viewed at {0}".format(con.PROCESS_CODE)
        msg = msg + "."
        help(msg)
    elif helping == "support":
        msg = "You can request help by going on the forums"
        if con.EMAIL:
            msg = msg + " or send an email to {0}".format(con.EMAIL)
        if con.USER_HELP:
            msg = msg + "; {0} {1} the official helper{2}".format(", ".join(con.USER_HELP), "are" if len(con.USER_HELP) > 1 else "is", "s" if len(con.USER_HELP) > 1 else "")
        msg = msg + "."
        help(msg)
    elif helping == "commands":
        msg = "There are no available commands."
        if con.COMMANDS:
            msg = "Available command{1}: {0}.".format(", ".join(con.COMMANDS), "s" if len(con.COMMANDS) > 1 else "")
        if (con.HIDDEN_COMMANDS and var.DEBUG_MODE) or (con.HIDDEN_COMMANDS and var.SHOW_HIDDEN_COMMANDS):
            msg = msg + "\nHidden command{1}: {0}.".format(", ".join(con.HIDDEN_COMMANDS), "s" if len(con.HIDDEN_COMMANDS) > 1 else "")
        help(msg)
    else:
        help("Error: '{0}' was not found but is in the database. Critical error.".format(helping), type="error")