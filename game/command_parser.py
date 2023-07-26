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
        return prepositions

    @staticmethod
    def parse_command(command):
        verbs = ["move", "take", "use", "quit", "hit", "pull", "glance", "glance at", "go", "eat", "look", "inventory",
                 "examine", "show", "turn on", "turn off", "insert", "upgrade", "study", "cut", "activate", "deactivate",
                 "decipher", "display", "help", "drop", "look at"]

        prepositions = CommandParser.identify_prepositions(command)

        words = command.split()
        verb = None
        obj = []

        i = 0
        while i < len(words):
            word = words[i]
            multi_word_verb = None
            # check for multi-word verb first
            if i < len(words) - 1:  # ensure there's a next word
                candidate_verb = f"{word} {words[i + 1]}"
                if candidate_verb in verbs:
                    multi_word_verb = candidate_verb
                    i += 2  # increment i by 2 as we're using two words

            if multi_word_verb:
                verb = multi_word_verb
            elif word in verbs:  # if the word is a verb and not part of a multi-word verb
                verb = word
                i += 1
            elif verb:  # append to obj only if the verb has been found
                if word not in prepositions and word not in verbs:
                    obj.append(word)
                i += 1

        return verb, " ".join(obj)
