import matplotlib.pyplot as plt
from random import choice

class Random_walk():
    def init_ (self , MAXN = 5000):
        self.max = MAXN
        self.x_value = [0]
        self.y_value = [0]
    def fill_walk(self):
        while len(self.x_value) < self.max:
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            if(x_step == 0 and y_step == 0):
                continue
            new_x = self.x_value[-1] + x_step
            new_y = self.y_value[-1] + y_step
            self.x_value.append(new_x)
            self.y_value.append(new_y)

rw = Random_walk()
rw.init_()
rw.fill_walk()
plt.scatter(rw.x_value , rw.y_value , s = 8 )
plt.show()