import sys
import random
import math

MAXQ = 100


def in_conflict(column, row, other_column, other_row):
    """
    Checks if two locations are in conflict with each other.
    :param column: Column of queen 1.
    :param row: Row of queen 1.
    :param other_column: Column of queen 2.
    :param other_row: Row of queen 2.
    :return: True if the queens are in conflict, else False.
    """
    if column == other_column:
        return True  # Same column
    if row == other_row:
        return True  # Same row
    if abs(column - other_column) == abs(row - other_row):
        return True  # Diagonal

    return False


def in_conflict_with_another_queen(row, column, board):
    """
    Checks if the given row and column correspond to a queen that is in conflict with another queen.
    :param row: Row of the queen to be checked.
    :param column: Column of the queen to be checked.
    :param board: Board with all the queens.
    :return: True if the queen is in conflict, else False.
    """
    for other_column, other_row in enumerate(board):
        if in_conflict(column, row, other_column, other_row):
            if row != other_row or column != other_column:
                return True
    return False


def count_conflicts(board):
    """
    Counts the number of queens in conflict with each other.
    :param board: The board with all the queens on it.
    :return: The number of conflicts.
    """
    cnt = 0

    for queen in range(0, len(board)):
        for other_queen in range(queen+1, len(board)):
            if in_conflict(queen, board[queen], other_queen, board[other_queen]):
                cnt += 1

    return cnt


def evaluate_state(board):
    """
    Evaluation function. The maximal number of queens in conflict can be 1 + 2 + 3 + 4 + .. +
    (nqueens-1) = (nqueens-1)*nqueens/2. Since we want to do ascending local searches, the evaluation function returns
    (nqueens-1)*nqueens/2 - countConflicts().

    :param board: list/array representation of columns and the row of the queen on that column
    :return: evaluation score
    """
    return (len(board)-1)*len(board)/2 - count_conflicts(board)


def print_board(board):
    """
    Prints the board in a human readable format in the terminal.
    :param board: The board with all the queens.
    """
    print("\n")

    for row in range(len(board)):
        line = ''
        for column in range(len(board)):
            if board[column] == row:
                line += 'Q' if in_conflict_with_another_queen(row, column, board) else 'q'
            else:
                line += '.'
        print(line)


def init_board(nqueens):
    """
    :param nqueens integer for the number of queens on the board
    :returns list/array representation of columns and the row of the queen on that column
    """

    board = []

    for column in range(nqueens):
        board.append(random.randint(0, nqueens-1))

    return board


"""
------------------ Do not change the code above! ------------------
"""


def random_search(board):
    """
    This function is an example and not an efficient solution to the nqueens problem. What it essentially does is flip
    over the board and put all the queens on a random position.
    :param board: list/array representation of columns and the row of the queen on that column
    """

    i = 0
    optimum = (len(board) - 1) * len(board) / 2

    while evaluate_state(board) != optimum:
        i += 1
        print('iteration ' + str(i) + ': evaluation = ' + str(evaluate_state(board)))
        if i == 1000:  # Give up after 1000 tries.
            break

        for column, row in enumerate(board):  # For each column, place the queen in a random row
            board[column] = random.randint(0, len(board)-1)

    if evaluate_state(board) == optimum:
        print('Solved puzzle!')

    print('Final state is:')
    print_board(board)


def hill_climbing(board):
    
    i = 0
    optimum = (len(board) - 1) * len(board) / 2
    bestColumns = []                                        #this list stores all columns in wich a move leads to the best score

    while evaluate_state(board) != optimum:
        i += 1
        print('iteration ' + str(i) + ': evaluation = ' + str(evaluate_state(board)))
        if i == 1000:  # Give up after 1000 tries.
            break

        columnMax = 0
        boardMax = 0

        for m in range(len(board)):                         #loops through columns
            originalPos = board[m]                          #remember original position of queen in the column   
            for j in range(len(board)):                     #loops through positions within column
                if j == originalPos:                        #we dont need to evaluate the queen's current position
                    continue                                                              
                board[m] = j                                #move the queen
                if evaluate_state(board) > columnMax:
                    columnMax = evaluate_state(board)       #if this move results a in a board that has a better score than any other moves evaluated so far, this becomes the new maximum                          

            board[m] = originalPos                          #put the queen back on original position
            if  columnMax > boardMax:
                bestColumns.clear()                          
                bestColumns.append(m)
                boardMax = columnMax
            elif evaluate_state(board) == boardMax:
                bestColumns.append(m)
            columnMax = 0
            
        if boardMax >= evaluate_state(board):
            column = random.choice(bestColumns)             #select a random column from the ones that contain the best possibility
            originalPos = board[column]
            for k in range(len(board)):                     #loops through positions within column
                if k == originalPos:                        #we dont need to evaluate the queen's current position
                    continue                                                              
                board[column] = k                           #move the queen
                if evaluate_state(board) == boardMax:
                    break
                else:
                    board[column] = originalPos

        bestColumns.clear()      

    if evaluate_state(board) == optimum:
        print('Solved puzzle!')

    print('Final state is:')
    print_board(board)
    

def find_indices(list_1, item):
    indices = []
    for idx, value in enumerate(list_1):
        if value == item:
            indices.append(idx)
    return indices

def genetic(board):
    itr = 0
    optimum = (len(board) - 1) * len(board) / 2

    while evaluate_state(board) != optimum:
        itr += 1
        print('iteration ' + str(itr) + ': evaluation = ' + str(evaluate_state(board)))
        if itr == 1000:  # Give up after 1000 tries.
            break

        # 1) Init population
        chromosome = []
        for i in range(4): # set population as 4
            gene = []
            for j in range(len(board)):
                gene.append(random.randint(0, len(board) - 1))
            chromosome.append(gene)

        # 2) Fitness function
        heurisitcs = []
        for i in range(4):
            heurisitcs.append(count_conflicts(chromosome[i]))
    
        # 3) Selection
        # choose 2 members from the chromosome (population), they're the ones w/ the least conflicts
        for i in range(2):
            if i == 0:
                pa = chromosome[heurisitcs.index(min(heurisitcs) )].copy()
                del chromosome[heurisitcs.index(min(heurisitcs) )]
                del heurisitcs[heurisitcs.index(min(heurisitcs) )]
            else:
                ma = chromosome[heurisitcs.index(min(heurisitcs) )].copy()
                del chromosome[heurisitcs.index(min(heurisitcs) )]
                del heurisitcs[heurisitcs.index(min(heurisitcs) )]
    
        # the god's scissors decides to cut at the point where the proportion 
        # of the 2 segments would be roughly 1:1.618 ~= 4:6
        cut = round((len(board) * 0.4))
        rmn = len(board) - cut
        if cut + rmn > len(board):
            rmn -= 1
    
        # 4) Crossover: 
        egg = []
        for i in range(2): # 2 possibilities (fertilised eggs)
            if i == 0:
                tmp = []
                for j in range(cut):
                    tmp.append(pa[j])
                for j in range(rmn):
                    tmp.append(ma[cut+j])
                egg.append(tmp)

            else:
                tmp = []
                for j in range(cut):
                    tmp.append(ma[j])
                for j in range(rmn):
                    tmp.append(pa[cut+j])
                egg.append(tmp)
     
        # 5) Mutation: if there're duplicated numbers, change one (some) of them
        # the rule is: randomly choose one of them, turn it into a number which is not yet 
        # in the sequence, also it should not be its adjacent neighbours' 
        # increment / decrement
        for i in range(2): # 2 eggs for mutation
            options = [] # options for duplicated index to choose a new number
            # Initialising
            for j in range(len(board)): # initialise w/ True
                options.append(True)
            for j in range(len(board)):
                for k in range(len(board)): # search for existed members
                    if board[k] == j:
                        options[j] = False

            for j in range(len(board)):
                idx = find_indices(egg[i], j)
            for j in range(len(board)):
                for k in range(len(idx) - 1):
                    try:
                        pos = options.index(True)
                        passing = True
                    except ValueError():
                        passing = False
                        break
                    oldPos = egg[i][idx[k]]
                    egg[i][idx[k]] = pos
                    options[pos] = False

                if passing != False and (egg[i][idx[k]] == egg[i][idx[k-1]] + 1 or egg[i][idx[k]] == egg[i][idx[k-1]] - 1 or egg[i][idx[k]] == egg[i][idx[k+1]] + 1 or egg[i][idx[k]] == egg[i][idx[k+1]] - 1):
                    egg[i][idx[k]] = oldPos
    
    if evaluate_state(board) == optimum:
        print('Solved puzzle!')

    print('Final state is:')
    print_board(board)

def time_to_temperature(time):
    T = 100000 - time 
    if T < 1:
        T = 1

    return T

def simulated_annealing(board):
    optimum = (len(board) - 1) * len(board) / 2
    time = 1
    
    while evaluate_state(board) != optimum:
        
        print('iteration ' + str(time) + ': evaluation = ' + str(evaluate_state(board)))
        randomColumn = random.randint(0, len(board)-1)                                  
        originalPos = board[randomColumn]
        originalEval = evaluate_state(board)

        while board[randomColumn] == originalPos:
            board[randomColumn] = random.randint(0, len(board)-1)
        
        deltaE = evaluate_state(board) - originalEval
        T = time_to_temperature(time)
        
        if deltaE <= 0: 
            options = [True, False]
            choice = random.choices(options, cum_weights=(pow(math.e, deltaE/T), 1), k = 1)
            if choice == False:
                board[randomColumn] = originalPos
                time -= 1
        
        if time == 100000:
            break

        time += 1

    if evaluate_state(board) == optimum:
        print('Solved puzzle!')

    print('optimum:', optimum)
    print('Final state is:')
    print_board(board)
    pass


def main():
    """
    Main function that will parse input and call the appropriate algorithm. You do not need to understand everything
    here!
    """

    try:
        if len(sys.argv) != 2:
            raise ValueError

        n_queens = int(sys.argv[1])
        if n_queens < 1 or n_queens > MAXQ:
            raise ValueError

    except ValueError:
        print('Usage: python n_queens.py NUMBER')
        return False

    print('Which algorithm to use?')
    algorithm = input('1: random, 2: hill-climbing, 3: simulated annealing 4: genetic\n')

    try:
        algorithm = int(algorithm)

        if algorithm not in range(1, 5):
            raise ValueError

    except ValueError:
        print('Please input a number in the given range!')
        return False

    board = init_board(n_queens)
    print('Initial board: \n')
    print_board(board)

    if algorithm == 1:
        random_search(board)
    if algorithm == 2:
        hill_climbing(board)
    if algorithm == 3:
        simulated_annealing(board)
    if algorithm == 4:
        genetic(board)


# This line is the starting point of the program.
if __name__ == "__main__":
    main()
