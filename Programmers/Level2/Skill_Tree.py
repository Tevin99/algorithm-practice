def solution(skill, skill_trees):

    count = 0  # number of valid skill trees

    for tree in skill_trees:
        # keep only the skills that appear in the required skill order
        filtered = ''.join([s for s in tree if s in skill])

        # check if the filtered skill sequence matches the prefix of 'skill'
        # i.e., the order must follow the given skill order from the beginning
        if skill.startswith(filtered):
            count += 1  # this skill tree is valid
            
    return count  # return the number of valid skill trees