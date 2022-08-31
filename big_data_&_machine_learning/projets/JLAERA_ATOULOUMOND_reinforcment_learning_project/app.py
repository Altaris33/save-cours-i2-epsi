# main Python class 
# to be run  

import logging
from enum import Enum, auto

import matplotlib.pyplot as plt
import numpy as np

import model
import qtable
from environment.labyrinth import Labyrinth, Render

logging.basicConfig(format="%(levelname)-8s: %(asctime)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=logging.INFO)  


class Test(Enum):
    SHOW_MAZE_ONLY = auto()
    Q_LEARNING = auto()


test = Test.SARSA_ELIGIBILITY  

labyrinth: list = [
      [-1, -1, -1, -1, -1, -1, -1, -1],
      [-1, 0, -1, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1,  2, -1, -1],
      [-1, -1, -1, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1, -1, -1, -1],
      [-1, -1, -1, -1, -1, -1, -1, -1] 
    ]

game = Labyrinth(labyrinth) 

if test == Test.SHOW_MAZE_ONLY:
    game.render(Render.MOVES)
    game.reset()

# train using tabular Q-learning
if test == Test.Q_LEARNING:
    game.render(Render.TRAINING)
    model = qtable.QTable(game, name="QTable")
    h, w, _, _ = model.train(discount=0.90, exploration_rate=0.10, learning_rate=0.10, episodes=200,
                             stop_at_convergence=True)

try:
    h  
    fig, (ax1, ax2) = plt.subplots(2, 1, tight_layout=True)
    fig.canvas.set_window_title(model.name)
    ax1.plot(*zip(*w))
    ax1.set_xlabel("episode")
    ax1.set_ylabel("win rate") 
    ax2.plot(h)
    ax2.set_xlabel("episode")
    ax2.set_ylabel("cumulative reward")
    plt.show()
except NameError:
    pass

game.render(Render.MOVES)
game.play(model, start_cell=(0, 0))

plt.show()  