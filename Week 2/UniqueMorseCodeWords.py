class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseLetters = {
          'a':".-",
          'b':"-...",
          'c':"-.-.",
          'd':"-..",
          'e':".",
          'f':"..-.",
          'g':"--.",
          'h':"....",
          'i':"..",
          'j':".---",
          'k':"-.-",
          'l':".-..",
          'm':"--",
          'n':"-.",
          'o':"---",
          'p':".--.",
          'q':"--.-",
          'r':".-.",
          's':"...",
          't':"-",
          'u':"..-",
          'v':"...-",
          'w':".--",
          'x':"-..-",
          'y':"-.--",
          'z':"--.." 
        }    

        s = set() 

        for i in words:
            aux = list(i)
            wordMorse = ""
            for j in aux:
                wordMorse+=morseLetters[j]
            s.add(wordMorse)

        return(len(s))