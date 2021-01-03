from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    def __init__(self, num_of_points=5000):
        self.num_of_points = num_of_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_of_points:
            x_step = self.get_step()
            y_step = self.get_step()
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            if x == 0 and y == 0:
                continue
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([-1, 1])
        step = choice([1, 2, 3, 4, 5, 6, 7, 8]) * direction
        return step


while True:
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9))
    random_walk = RandomWalk(5000)
    random_walk.fill_walk()
    ax.plot(random_walk.x_values, random_walk.y_values)
    ax.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c='red', edgecolors='none', s=100)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    q = input('Do you want to continue (Y, N)')
    if q == 'N' or q == 'n':
        break