import json

agenda_file = open('agenda_messages.json')

agenda_messages = json.load(agenda_file)

agenda_file.close()


def get_messages_agenda_dict():
    return agenda_messages
