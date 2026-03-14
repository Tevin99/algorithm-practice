def solution(board, moves):
    s = []      # stack to store picked dolls
    count = 0   # number of removed dolls

    for move in moves:
        move -= 1  # adjust index (moves start from 1 in the problem)

        # scan the column from top to bottom
        for i in range(len(board)):
            if board[i][move] != 0:   # if there is a doll
                doll = board[i][move]

                # remove the doll from the board
                board[i][move] = 0

                # if the top of the stack has the same doll
                if s and s[-1] == doll:
                    s.pop()      # remove the previous doll
                    count += 2   # two dolls disappear
                else:
                    s.append(doll)  # push the doll into the stack

                break  # once a doll is picked, move to the next move

    return count