import sys

class Unscrambler:

    WORD_LIST_FILENAME = "wordlist.txt" #Const
    
    world_list_original = []
    word_list_dict= {}
    
    def __init__(self):
        self.world_list_original = self.read_and_clear_txt(self.WORD_LIST_FILENAME)
        self.create_wordlist_dictionary()

    # Read in .txt file, clear contents of linebreaks -> "\n" and save into a list variable
    def read_and_clear_txt(self, file_name):
        f = open(file_name, "r")
        values = f.read().rstrip().split("\n")
        return values

    # Create wordlist dict
    def create_wordlist_dictionary(self):
        for i in range(len(self.world_list_original)):
            self.word_list_dict[''.join(sorted(self.world_list_original[i]))] = self.world_list_original[i]
            

    # Read in input txt
    def find_matches(self, input):
        answer = []
        for i in range (len(input)):
            # sorteeri input sõnad üks haaval ja võrdle sorteeritud vastet wordlist dict key-ga
            sortedInputWord = ''.join(sorted(input[i]))
            if self.word_list_dict.get(sortedInputWord):
                # kui leiab key vaste, siis lisa sõna answer listi
                answer.append(self.word_list_dict.get(sortedInputWord))
        return answer
                
    def run(self, file_name):
        input = self.read_and_clear_txt(file_name)
        answer = self.find_matches(input)
        print(','.join((answer)))

unscrambler = Unscrambler()

unscrambler.run(sys.argv[1])