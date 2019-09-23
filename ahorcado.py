import random

ASCII_ART = [
    '''           
      ==========
      |       ||
      |       ||
              ||
              ||
              ||
              ||
              ||
              ||
              ||
      ----------
      ----------
    ''',
    '''
      ==========
      |       ||
      |       ||
      O       ||
              ||
              ||
              ||
              ||
              ||
              ||
      ----------
      ----------
    ''',
    '''
      ==========
      |       ||
      |       ||
      O       ||
      |       ||
      |       ||
              ||
              ||
              ||
              ||
      ----------
      ----------
    ''',
    '''
      ==========
      |       ||
      |       ||
      O       ||
     /|       ||
    / |       ||
              ||
              ||
              ||
              ||
      ----------
      ----------
    ''',
    '''
      ==========
      |       ||
      |       ||
      O       ||
     /|\      ||
    / | \     ||
              ||
              ||
              ||
              ||
      ----------
      ----------
    ''',
    '''
      ==========
      |       ||
      |       ||
      O       ||
     /|\      ||
    / | \     ||
     /        ||
    /         ||
              ||
              ||
      ----------
      ----------
    ''',
        '''
      ==========
      |       ||
      |       ||
      O       ||
     /|\      ||
    / | \     ||
     / \      ||
    /   \     ||
              ||
              ||
      ----------
      ----------
    '''
]

WORDS = [
    'CACHETES',
    'ZARZAMORA',
    'JUEGO',
    'RUIN',
    'CIVILIZACION',
    'ACERRIMO',
    'CHIMPANCE',
    'ALOCADO',
    'MUESTRA'
]

MAX_TRY = len(ASCII_ART)

def getRandomWord():
    return WORDS[random.randint(0, len(WORDS) - 1)]

def refreshPlayingBoard(tries, guess):
    print(ASCII_ART[tries])
    print('**---' + str.join(' ', guess) + '---**')

def checkLetterCoincidences(wordToGuess, currentLetterGuess):
    coincidenceIndexes = []
    
    for i in range(0, len(wordToGuess)):
        if currentLetterGuess[0] == wordToGuess[i]:
            coincidenceIndexes.append(i)

    return coincidenceIndexes

def checkWinCondition(currentGuessStatus):
    currentGuessStatus.index("_")

def checkGameOverCondition(currentTry):
    return currentTry == MAX_TRY - 1

def run():
    word = getRandomWord()
    guess = ['_'] * len(word)

    currentTry = 0

    while True:
        refreshPlayingBoard(currentTry, guess)
        
        currentLetterGuess = str(raw_input('Que letra te arriesgaras a adivinar: '))
        currentLetterGuess = str.upper(currentLetterGuess)

        coincidenceIndexes = checkLetterCoincidences(word, currentLetterGuess)

        if 0 < len(coincidenceIndexes):
            for i in coincidenceIndexes:
                guess[i] = currentLetterGuess
        else:
            currentTry += 1

        try:
            checkWinCondition(guess)
        except ValueError:
            refreshPlayingBoard(currentTry, guess)
            print('Te has salvado... Esta vez')
            break

        if(checkGameOverCondition(currentTry)):
            refreshPlayingBoard(currentTry, word)
            print('Tu sabiduria no fue suficiente >:)')
            break

if __name__ == "__main__":
    print('Quieres jugar un juego?')
    run()