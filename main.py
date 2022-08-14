import random, sys

print('KAMIEŃ, PAPIER, NOŻYCE')
# Te zmienne przechowują informację o liczbie zwycięstw, porażek i remisów
wins = 0
loses = 0
ties = 0

#Pętla główna gry
while True:
    print('%s zwycięstw, %s porażek, %s remisów' % (wins, loses, ties))
    #Pętla danych wejściowych gracza
    while True:
        print('Podaj swój wybór: (k)amień, (p)apier, (n)ożyce lub (w)yjście')
        playerMove = input()
        if playerMove == 'w':
            sys.exit() # Zakończenie działania programu.
        if playerMove == 'p' or playerMove == 'k' or playerMove == 'n':
            break #Opuszczenie pętli danych wejściowych gracza.
        print('Wpisz literę p, k, n lub w.')
