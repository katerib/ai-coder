import spacy

class CommandParser:
    @staticmethod
    def identify_prepositions(command):
        """
        Identify prepositions in the user command using spaCy.
        """
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(command)
        prepositions = [token.text for token in doc if token.pos_ == "ADP"]
        # if prepositions:
        #     print(f"found preposition! {prepositions}")
        return prepositions

    @staticmethod
    def parse_command(command):
        """
        Parse the user command and identify the verb and object. Calls identify_preposition using spaCy.
        """
        verbs = ["move", "take", "use", "quit", "hit", "pull", "go", "eat", "look", "look at", "inventory",
                 "examine", "show", "turn on", "turn off", "insert", "upgrade", "study", "cut", "activate", "deactivate",
                 "decipher", "display", "help", "drop"]

        prepositions = CommandParser.identify_prepositions(command)

        words = command.split()
        verb = None
        obj = []

        for word in words:
            if word in verbs:
                verb = word
            elif word not in prepositions:
                obj.append(word)

        return verb, " ".join(obj)
