'''
parcheesi game for final project
'''
import random
import csv
from datetime import date

from mpmcgeeparcheesiobjects import *

a = Human("", "1", 0, "safe", 0)
b = Human("", "2", 0, "safe", 0)
c = Computer("", "C", 0, "safe", 0)

today = date.today()


def rules():
    print("Welcome to parcheesi, would you like to read the rules?")
    answer = ""
    while answer != "Y" and answer != "N":

        answer = input("'Y' for yes or 'N' for no. ")
        answer = answer.upper()
        if answer == "Y":
            print("* All players start off in jail and have three opportunities per turn to roll doubles to get out of jail. If doubles are rolled, player moves out of jail and may roll again.")
            print("* If a player rolls doubles after they are out of jail, they will get another turn.")
            print("* If a player lands on a space where another player is, the player who was already on that space will be captured return to jail.")
            print("* Every 5  spaces on the board will be safe spaces, where a player cannot be captured")
            print("* Once a player reaches space 63, they are safe for the remainder of the game, but can only roll one die")
            print("* To win the game, a player must reach space 69 by an exact roll")





def main():

  rules()
  a.getName()
  b.getName()
  c.autoGetName()
  print("You will be playing against {}({})" .format(c.name, c.indicator))

  keepGoing = "true"
  turn=0


  while keepGoing == "true":

    a.position = 0
    b.position = 0
    c.position = 0


    while a.position < 69 and b.position < 69:
        turn=turn+1


        # Player 1's turn:

        print("\n{}'s({}) turn" .format(a.name, a.indicator))
        a.roll()
        a.checkDanger()

        if a.position == b.position and b.danger == "danger":
            b.position = 0
            print("{}({}) has been captured and returned to jail" .format(b.name, b.indicator))
        if a.position == c.position and c.danger == "danger":
            print("{}({}) has been captured and returned to jail" .format(c.name, c.indicator))
            c.position = 0
        a.printBoard()
        b.printBoard()
        c.printBoard()

        if a.position > 68:
            a.wins = a.wins+1
            print("{}({}) wins in {} turns!" .format(a.name, a.indicator, turn))
            print("Wins: {}({}) = {}, {}({}) = {}, {}({}) = {}" .format(a.name, a.indicator, a.wins, b.name, b.indicator, b.wins, c.name, c.indicator, c.wins))
            break

        # Player 2's turn:
        print("\n{}'s({}) turn" .format(b.name, b.indicator))
        b.roll()
        b.checkDanger()

        if b.position == a.position and a.danger == "danger":
            a.position = 0
            print("{}({}) has been captured and returned to jail" .format(a.name, a.indicator))
        if b.position == c.position and c.danger == "danger":
            c.position = 0
            print("{}({}) has been captured and returned to jail" .format(c.name, c.indicator))
        a.printBoard()
        b.printBoard()
        c.printBoard()
        if b.position > 68:
            b.wins = b.wins+1
            print("{}({}) wins in {} turns!" .format(b.name, b.indicator, turn))
            print("Wins: {}({}) = {}, {}({}) = {}, {}({}) = {}" .format(a.name, a.indicator, a.wins, b.name, b.indicator, b.wins, c.name, c.indicator, c.wins))
            break

         # Computer's turn:
        print("\n{}'s({}) turn" .format(c.name, c.indicator))
        c.autoRoll()
        c.checkDanger()

        if c.position == a.position and a.danger == "danger":
            a.position = 0
            print("{}({}) has been captured and returned to jail" .format(a.name, a.indicator))
        if c.position == b.position and b.danger == "danger":
            b.position = 0
            print("{}({}) has been captured and returned to jail" .format(b.name, b.indicator))
        a.printBoard()
        b.printBoard()
        c.printBoard()
        if c.position > 68:
            c.wins = c.wins+1
            print("{}({}) wins in {} turns!" .format(c.name, c.indicator, turn))
            print("Wins: {}({}) = {}, {}({}) = {}, {}({}) = {}" .format(a.name, a.indicator, a.wins, b.name, b.indicator, b.wins, c.name, c.indicator, c.wins))
            break


    #Play again option
    print ("Would you like to play again?")
    choice = ""
    while choice != "Y" and choice != "N":
        choice = input("'Y' for yes or 'N' for no. ")
        choice = choice.upper()
        if choice == "Y":
            keepGoing = "true"
        if choice == "N":
            keepGoing = "false"
            games=(a.wins+b.wins+c.wins)
            percent= (a.wins/games)*100
            with open('mpmcgee-parcheesistats.csv', mode='a') as mpmcgee_parcheesistats:
                parcheesi_writer = csv.writer(mpmcgee_parcheesistats, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                parcheesi_writer.writerow([today, a.name, a.wins, games, round(percent, 2)])
                print("{}({})'s stats written to mpmcgee-parcheesistats.csv" .format(a.name, a.indicator))
                print("Thank you for playing Parcheesi!")

main()



