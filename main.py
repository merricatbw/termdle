from typing import NewType
import curses
import random

class Box:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.value = " "
        
    def draw_self(self, screen: curses._CursesWindow):
        screen.addstr(self.x, self.y, "---")
        screen.addstr(self.x + 1, self.y, "|" + self.value + "|")
        screen.addstr(self.x + 2, self.y, "---")

#constants
TITLE = "TERMDLE"


# ComparisonCheck is a comparison of two Word types
# each integer corrisponds to the letter index of the words that are being copared
# if the letters don't compare then the integer should be 0
# if they do compare then the integer will be 2
# if they don't compare but the guessed letter is somewhere in the word it should be a 1
ComparisonCheck = NewType('ComparisonCheck', tuple[int, int, int, int, int])
Word = NewType('Word', tuple[str, str, str, str, str])




def main() -> None:
    screen = curses.initscr()
    screen.refresh()
    width = curses.COLS
    screen.addstr(
        0,
        find_horizontal_centre(TITLE, width),
        TITLE
        )
    screen.refresh()
    curses.napms(2000)

    word = get_word()
    
    curses.endwin()
    
def find_horizontal_centre(string: str, width: int) -> int:
    word_length = len(string)
    return int(width / 2) - int(word_length / 2)
    
def get_word() -> Word:
    random_number = random.randrange(0, 14954)
    word = ""
    with open("./wordlist", "r") as wl:
        word = list(wl)[random_number].strip()
    return str_to_word(word)

def str_to_word(x: str) -> Word:
    return Word((x[0], x[1], x[2], x[3], x[4]))

def compare_words(word: Word, user_guess: Word) -> ComparisonCheck:
    checker = [0, 0, 0, 0, 0]    
    for i in range(0, 5):
        if user_guess[i] == word[i]:
            checker[i] = 2
        elif user_guess[i] in word:
            checker[i] = 1
        else:
            checker[i] = 0
    return ComparisonCheck((checker[0],
                            checker[1],
                            checker[2],
                            checker[3],
                            checker[4]))


if __name__ == "__main__":
    main()