from mycroft import MycroftSkill, intent_file_handler


class Ll(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ll.intent')
    def handle_ll(self, message):
        self.speak_dialog('ll')


def create_skill():
    return Ll()

