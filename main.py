import util


class MineNode:

    def __init__(self):
        self.value = 0
        self.x = 0
        self.y = 0

    def create_node(self, x, y, value=0):
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return "Node: ({}, {}) <{}>".format(self.x, self.y, self.value)


class BattleGround:

    def __init__(self, n=8):
        self.grid = list()
        self.side = n
        self.move = 0
        self.status = 0

    def initialize_grid(self):
        # print("side = {}".format(self.side))
        for i in range(self.side):
            row = list()
            for j in range(self.side):
                # print("\ni={}\tj={}".format(i, j))
                new_node = MineNode()
                new_node.create_node(i, j)
                row.append(new_node)
            self.grid.append(row)

    def deploy_mines(self):
        mines = util.define_mines(self.side)
        print(mines)
        for mine in mines:
            x, y = mine
            self.grid[x][y].value = "m"

    def display(self):
        if self.move == 0:
            util.print_grid_skeleton(self.side)


if __name__ == "__main__":
    new_ground = BattleGround()
    new_ground.display()
    new_ground.initialize_grid()
    new_ground.deploy_mines()
    print(new_ground.grid)
