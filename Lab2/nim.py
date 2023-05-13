import sys


def value(state, turn):
    turn = 0 if turn==1 else 1

    v = -10000000000 if not turn==1 else 100000000000

    if state == 1:      
        return 1, 1 if turn==0 else -1, 0 

    for move in range(1, 4):
        if state-move > 0:
            a = value(state-move, turn)  
            m = a[0] 

    return v, turn


def negamax_decision(state, turn):
    best_move = 0
    v = -10000000000 if not turn==1 else 100000000000

    for move in range(1, 4):
        if state - move > 0:
            a = value(state-move, turn)  
            m = a[0]
            print('M', m)
            if (turn == 0 and m > v) or (turn == 1 and m < v):
                v = m 
                best_move = move

    return best_move, v


def play_nim(state):
    turn = 0

    while state != 1:
        a = negamax_decision(state, turn)
        move = a[0]
        print(negamax_decision(state, turn))
        print(str(state) + ": " + ("MAX" if not turn else "MIN") + " takes " + str(move))

        state -= move
        turn = 1 - turn

    print("1: " + ("MAX" if not turn else "MIN") + " looses")


def main():
    """
    Main function that will parse input and call the appropriate algorithm. You do not need to understand everything
    here!
    """

    try:
        if len(sys.argv) != 2:
            raise ValueError

        state = int(sys.argv[1])
        if state < 1 or state > 100:
            raise ValueError

        play_nim(state)

    except ValueError:
        print('Usage: python nim.py NUMBER')
        return False


if __name__ == '__main__':
    main()
