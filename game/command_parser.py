# class CommandParser:
#     @staticmethod
#     def parse_command(command, prepositions):
#         """
#         Parse the user command and identify the verb, preposition, and object (if applicable).
#         """

#         verbs = ["move", "take", "use", "quit", "hit", "pull", "go", "eat", "look", "look at", "inventory",
#                  "examine", "show", "turn on", "turn off", "insert", "upgrade", "study", "cut", "activate", "deactivate"
#                  "decipher", "display", "help", "drop"]

#         words = command.split()
#         verb = None
#         preposition = None
#         obj = []

#         i = 0
#         while i < len(words):
#             word = words[i]
#             if word in verbs:
#                 verb = word
#                 i += 1
#             elif word in prepositions:
#                 preposition = word
#                 i += 1
#             else:
#                 # If the word is not a verb or preposition, it's part of the object
#                 # Look ahead to check if the next word is also part of the object
#                 j = i + 1
#                 while j < len(words):
#                     next_word = words[j]
#                     if next_word in verbs or next_word in prepositions:
#                         break
#                     obj.append(next_word)
#                     j += 1
#                 i = j

#         return verb, preposition, " ".join(obj)


# command_parser.py
class CommandParser:
    @staticmethod
    def parse_command(command, prepositions):
        """
        Parse the user command and identify the verb, preposition, and object (if applicable).
        """
        
        # Will have to fix this and minimize and create something separate for aliases
        verbs = ["move", "take", "use", "quit", "hit", "pull", "go", "eat", "look", "look at", "inventory",
                 "examine", "show", "turn on", "turn off", "insert", "upgrade", "study", "cut", "activate", "deactivate"
                 "decipher", "display", "help", "drop"]

        words = command.split()
        verb = None
        preposition = []
        obj = []

        for word in words:
            if word in verbs:
                verb = word
            elif word in prepositions:
                # Removes all prepositions from the command so that it doesn't get added to the object
                preposition.append(word)
            else:
                obj.append(word)

        return verb, " ".join(obj)
