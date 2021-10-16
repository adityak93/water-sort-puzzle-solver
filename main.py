def get_hash_key(bottles):
    hash_key = []
    for bottle in bottles:
        for k in bottle:
            hash_key.append(k)
        hash_key.append("-")
    return ''.join(hash_key)


def get_input_bottles():
    # inp = ['BOBO', 'OBOB', '']
    # inp = ['RPPR', 'RGLL', 'SOSR', 'PLBB', 'BOGG', 'LGOP', 'SSOB', '', '']
    # inp = ['BLDG', 'SGPU', 'LUUS', 'UDLP', 'SOBD', 'BSGP', 'GODB', 'ORRO', 'PRLR', '', '']  # Level 98
    inp = ['SBGS', 'PLRO', 'GPSL', 'OGSO', 'OBRL', 'RBLP', 'GPBR', '', '']  # Level 99
    bottles = []
    for i in inp:
        bottle = []
        for j in i:
            bottle.append(j)
        bottles.append(bottle)
    return bottles


def is_single_color(bottle):
    if len(bottle) == 0:
        return True
    for j in bottle[1:]:
        if j != bottle[0]:
            return False
    return True


def is_single_solved(bottle):
    if len(bottle) != 4:
        return False
    return is_single_color(bottle)


def is_solved(bottles):
    for bottle in bottles:
        if len(bottle) == 0:
            continue
        if len(bottle) < 3:
            return False
        single_color_status = is_single_color(bottle)
        if not single_color_status:
            return False
    return True


def can_move_completely(bottle1, bottle2):
    size = 0
    end = len(bottle1) - 1
    while end >= 0 and bottle1[len(bottle1) - 1] == bottle1[end]:
        end -= 1
        size += 1
    return size <= 4 - len(bottle2)


# Check if we can move completely
def can_move_from_1_to_2(bottle1, bottle2):
    if len(bottle2) == 4 or len(bottle1) == 0:
        return False
    if len(bottle2) == 0:
        if is_single_color(bottle1):
            return False
        return True
    return bottle1[-1] == bottle2[-1] and can_move_completely(bottle1, bottle2)


def move(bottles, first, second):
    # Cache bottle on left and Do the actual move
    # print("Moving from %s %s", first, second)
    # print(bottles[first])
    # print(bottles[second])
    moved_color = bottles[first].pop()
    bottles[second].append(moved_color)

    while can_move_from_1_to_2(bottles[first], bottles[second]):
        # print("Moving from %s %s" % (first, second))
        moved_color = bottles[first].pop()
        bottles[second].append(moved_color)


def solve(bottles):
    print("Solving for:")
    print(bottles)
    print("------------")
    print()
    if is_solved(bottles):
        return True
    # if get_hash_key(bottles) in memo:
    #     return False
    for first in range(len(bottles)):
        if is_single_solved(bottles[first]):
            continue
        for second in range(first+1, len(bottles)):
            if is_single_solved(bottles[second]):
                continue
            if can_move_from_1_to_2(bottles[first], bottles[second]):
                move(bottles, first, second)
                # recurse
                solved_value = solve(bottles)
                if solved_value:
                    print("Working Move from %s %s" % (first, second))
                    return True
                move(bottles, second, first)

            if can_move_from_1_to_2(bottles[second], bottles[first]):
                move(bottles, second, first)
                # recurse
                solved_value = solve(bottles)
                if solved_value:
                    print("Working Move from %s %s" % (second, first))
                    return True
                move(bottles, first, second)
    # memo[get_hash_key(bottles)] = True
    return False


# Prints solution in reverse order  
if __name__ == '__main__':
    inp_bottles = get_input_bottles()
    # print(inp_bottles)
    # print(is_solved(inp_bottles))
    print(solve(inp_bottles))
