def solution(numbers, hand):
    # Determine the preferred hand.
    # The problem input gives 'left' or 'right',
    # but we simplify it to 'L' or 'R' for easier comparison later.
    hand = 'R' if hand == 'right' else 'L'
    
    # This string will store the sequence of hands used to press the keypad.
    answer = ''

    # Mapping each keypad number/symbol to its (row, column) coordinate.
    # We treat the keypad like a 2D grid:
    #
    # (0,0) (0,1) (0,2)      1 2 3
    # (1,0) (1,1) (1,2)  ->  4 5 6
    # (2,0) (2,1) (2,2)      7 8 9
    # (3,0) (3,1) (3,2)      * 0 #
    #
    # This allows us to compute distances easily.
    pad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    # Initial position of the left hand is '*'
    lLoc = pad['*']

    # Initial position of the right hand is '#'
    rLoc = pad['#']

    # Iterate through each number that needs to be pressed
    for number in numbers:

        # Numbers in the left column are always pressed by the left hand
        # (1, 4, 7)
        if number in [1,4,7]:
            answer += 'L'
            lLoc = pad[number]   # Update left hand position

        # Numbers in the right column are always pressed by the right hand
        # (3, 6, 9)
        elif number in [3,6,9]:
            answer += 'R'
            rLoc = pad[number]   # Update right hand position

        else:
            # Numbers in the middle column (2,5,8,0)
            # require distance comparison between both hands.

            # Compute Manhattan distance from left hand to the target key
            # Manhattan distance formula:
            # |x1 - x2| + |y1 - y2|
            ld = abs(lLoc[0] - pad[number][0]) + abs(lLoc[1] - pad[number][1])

            # Compute Manhattan distance from right hand to the target key
            rd = abs(rLoc[0] - pad[number][0]) + abs(rLoc[1] - pad[number][1])
            
            # If the left hand is closer, use the left hand
            if ld < rd:
                answer += 'L'
                lLoc = pad[number]

            # If the right hand is closer, use the right hand
            elif rd < ld:
                answer += 'R'
                rLoc = pad[number]

            # If both hands are equally distant,
            # use the user's preferred hand
            else:
                answer += hand

                # Update the position of the hand that was used
                if hand == 'R':
                    rLoc = pad[number]
                else:
                    lLoc = pad[number]
                    
    # Return the final sequence of hand usages
    return answer