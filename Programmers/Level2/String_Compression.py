def solution(s):
    # Initialize answer with the original string length
    answer = len(s)

    # Try slicing the string with unit sizes from 1 to half of the string length
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]  # First substring unit
        count = 1

        # Iterate through the string with the given step size
        for j in range(step, len(s), step):

            # If the current substring is the same as the previous one
            if s[j:j+step] == prev:
                count += 1
            else:
                # If different, append the compressed form
                # Add count only when it is greater than 1
                compressed += str(count) + prev if count > 1 else prev

                # Reset previous substring and count
                prev = s[j:j+step]
                count = 1

        # Handle the last accumulated substring
        compressed += str(count) + prev if count > 1 else prev

        # Update the minimum compressed length
        answer = min(answer, len(compressed))

    return answer