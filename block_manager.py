from singleblock import Block


class BlockManager:

    def __init__(self):
        self.wall = []

        # another set of obstacles
        # self.x_coordinates = [30, 70, 110, 150, 190, 230, 270, 310, 350, 390]
        # self.y_coordinates = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270]

        # set the coordinates of obstacle blocks, currently isn't very good
        self.x_coordinates = [30, 110, 190, 270, 350]
        self.y_coordinates = [0, 60, 120, 180, 240, 270]

        self.color = "white"
        # create blocks
        for loc_y in self.y_coordinates:
            for loc_x in self.x_coordinates:
                block = Block((loc_x, loc_y))
                if self.color == "white":
                    self.color = "gray"
                else:
                    self.color = "white"
                block.color(self.color)
                self.wall.append(block)

                negative_side = ((loc_x * -1), loc_y)
                block2 = Block(negative_side)
                block2.color(self.color)
                self.wall.append(block2)

    def check_hit(self, position):
        for block in self.wall:
            if not block.hit:
                x = block.xcor()
                y = block.ycor()
                #print(type(block.xcor()))
                if (x - 20 < position[0] < x +20) and (y-20<position[1]<y+20):
                    block.remove()
                    return True
