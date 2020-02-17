from random import randint


def print_grid_skeleton(n=8):
    col_id, row_id = dict(), dict()
    default_node_value = "* " * n
    for i in range(n):
        col_id[i] = chr(65 + i)
        row_id[i] = 1 + i
    print("\t{}".format(" ".join(col_id.values())))
    for i in range(n):
        print("{}\t{}".format(row_id[i], default_node_value))


def define_mines(n=8):
    mines = list()
    while len(mines) != n:
        pos_x = randint(0, n - 1)
        pos_y = randint(0, n - 1)
        mine_pos = (pos_x, pos_y)
        if mine_pos not in mines:
            mines.append(mine_pos)
    return mines
