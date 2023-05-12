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