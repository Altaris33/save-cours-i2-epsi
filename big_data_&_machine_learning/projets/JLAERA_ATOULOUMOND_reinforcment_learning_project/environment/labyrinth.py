#!/usr/bin/env python

from enum import Enum, IntEnum

import logging
import matplotlib.pyplot as plt
import numpy as np  

class Cell(IntEnum):
    FREE = 0
    OCCUPIED = 1
    CURRENT =2

class Render(IntEnum):
    NOTHING = 0
    TRAINING = 1
    MOVES = 2 

class Action(IntEnum):
    MOVE_TO_LEFT = 0
    MOVE_TO_RIGHT = 1
    MOVE_TO_TOP = 2 
    MOVE_TO_BOTTOM = 3 

class Labyrinth():
    """
    Class for the labyrinth: a 6x6 grid. The agent will start at position (0;0)  
    """
    
    actions = {Action.MOVE_TO_LEFT, Action.MOVE_TO_RIGHT, Action.MOVE_TO_TOP, Action.MOVE_TO_BOTTOM}
    
    final_reward = 10.0
    penalty_move = -.10
    penalty_cell_alreay_visited = -.20
    penalty_out_of_bound_move = -.50

    def __init__(self, labyrinth, start_cell = (0,0), exit_cell = None):
        self.labyrinth = labyrinth
        self.__minimum_reward = -.5 * self.labyrinth.size 
        
        nrows, ncols = self.labyrinth.shape 
        
        self.cells = [(col, row) for col in range(ncols) for row in range (nrows)]
        self.empty = [(col, row) for col in range(ncols) for row in range(nrows) if self.labyrinth[row, col] == Cell.FREE]
        self.__exit_cell = (ncols - 1, nrows - 1) if exit_cell is None else exit_cell
        self.empty.remove(self.__exit_cell)  
        
        if self.__exit_cell not in self.cells:
            raise Exception("Error: exit cell at {} is not inside the labyrinth".format(self.__exit_cell))
        if self.labyrinth[self.__exit_cell[::-1]] == Cell.OCCUPIED:
            raise Exception("Error: exit cell at {} is not free".format(self.__exit_cell))  
            
        
        self.__render = Render.NOTHING  
        self.__ax1 = None  
        self.__ax2 = None  
        
        self.reset(start_cell) 
        
    def reset(self, start_cell=(0, 0)):
        """ 
            Parameters: tuple representing the starting cell
            Returns: the new state of agent after resetting the labyrinth
        """
        if start_cell not in self.cells:
            raise Exception('Error: start cell at {start_cell} is not inside labyrinth')
        if self.labyrinth[start_cell[::-1]] == Cell.OCCUPIED:
            raise Exception('Error: start cell at {start_cell} is not free')
        if start_cell == self.__exit_cell:
            raise Exception('Error: start/exit cell cannot be the same {start_cell}')

        self.__previous_cell = self.__current_cell = start_cell
        self.__total_accumulated_reward = 0.0  
        self.__visited = set()  

        if self.__render in (Render.TRAINING, Render.MOVES):
            nrows, ncols = self.labyrinth.shape
            self.__ax1.clear()
            self.__ax1.set_xticks(np.arange(0.5, nrows, step=1))
            self.__ax1.set_xticklabels([])
            self.__ax1.set_yticks(np.arange(0.5, ncols, step=1))
            self.__ax1.set_yticklabels([])
            self.__ax1.grid(True)
            self.__ax1.plot(*self.__current_cell, "rs", markersize=30)  
            self.__ax1.text(*self.__current_cell, "Start", ha="center", va="center", color="white")
            self.__ax1.plot(*self.__exit_cell, "gs", markersize=30) 
            self.__ax1.text(*self.__exit_cell, "Exit", ha="center", va="center", color="white")
            self.__ax1.imshow(self.labyrinth, cmap="binary")
            self.__ax1.get_figure().canvas.draw()
            self.__ax1.get_figure().canvas.flush_events()

        return self.__observe()    
    
    def __draw(self):
        """ 
            Drawing a line from previous cell to current cell   
        """
        self.__ax1.plot(*zip(*[self.__previous_cell, self.__current_cell]), "bo-")  
        self.__ax1.plot(*self.__current_cell, "ro")  
        self.__ax1.get_figure().canvas.draw()
        self.__ax1.get_figure().canvas.flush_events()
        
        
    def render(self, content=Render.NOTHING):
        """ 
            Parameters: Renders content: NOTHING, TRAINING, MOVES  
        """
        self.__render = content

        if self.__render == Render.NOTHING:
            if self.__ax1:
                self.__ax1.get_figure().close()
                self.__ax1 = None
            if self.__ax2:
                self.__ax2.get_figure().close()
                self.__ax2 = None
        if self.__render == Render.TRAINING:
            if self.__ax2 is None:
                fig, self.__ax2 = plt.subplots(1, 1, tight_layout=True)
                fig.canvas.set_window_title("Best move")
                self.__ax2.set_axis_off()
                self.render_q(None)
        if self.__render in (Render.MOVES, Render.TRAINING):
            if self.__ax1 is None:
                fig, self.__ax1 = plt.subplots(1, 1, tight_layout=True)
                fig.canvas.set_window_title("Maze")

        plt.show(block=False)    
        
        
    def step(self, action):
        """ 
            Parameters: Action action: the agent will move in this direction (LEFT, RIGHT, TOP, BOTTOM)
            Returns: state, reward, status
        """
        reward = self.__execute(action)
        self.__total_accumulated_reward += reward
        status = self.__status()
        state = self.__observe()
        logging.debug("action: {:10s} | reward: {: .2f} | status: {}".format(Action(action).name, reward, status))
        return state, reward, status  
    
    def __execute(self, action):
        """ 
            Parameters: Action action: direction in which the agent will move
            Returns: float: reward or penalty which results from the action
        """
        possible_actions = self.__possible_actions(self.__current_cell)

        if not possible_actions:
            reward = self.__minimum_reward - 1  
        elif action in possible_actions:
            col, row = self.__current_cell
            if action == Action.MOVE_LEFT:
                col -= 1
            elif action == Action.MOVE_UP:
                row -= 1
            if action == Action.MOVE_RIGHT:
                col += 1
            elif action == Action.MOVE_BOTTOM:
                row += 1

            self.__previous_cell = self.__current_cell
            self.__current_cell = (col, row)

            if self.__render != Render.NOTHING:
                self.__draw()

            if self.__current_cell == self.__exit_cell:
                reward = Labyrinth.reward_exit  
            elif self.__current_cell in self.__visited:
                reward = Labyrinth.penalty_visited  
            else:
                reward = Labyrinth.penalty_move  

            self.__visited.add(self.__current_cell)
        else:
            reward = Labyrinth.penalty_impossible_move  

        return reward
    
    def __possible_actions(self, cell=None):
        """ 
            Parameters tuple cell: location of the agent (optional, else use current cell)
            Return list: all possible actions
        """
        if cell is None:
            col, row = self.__current_cell
        else:
            col, row = cell

        possible_actions = Labyrinth.actions.copy()  

        # now restrict the initial list by removing impossible actions
        nrows, ncols = self.labyrinth.shape
        if row == 0 or (row > 0 and self.labyrinth[row - 1, col] == Cell.OCCUPIED):
            possible_actions.remove(Action.MOVE_UP)
        if row == nrows - 1 or (row < nrows - 1 and self.maze[row + 1, col] == Cell.OCCUPIED):
            possible_actions.remove(Action.MOVE_BOTTOM)

        if col == 0 or (col > 0 and self.labyrinth[row, col - 1] == Cell.OCCUPIED):
            possible_actions.remove(Action.MOVE_LEFT)
        if col == ncols - 1 or (col < ncols - 1 and self.labyrinth[row, col + 1] == Cell.OCCUPIED):
            possible_actions.remove(Action.MOVE_RIGHT)

        return possible_actions

    def __status(self):
        """ 
            Returns Status: current game status (WIN, LOSE, PLAYING)
        """
        if self.__current_cell == self.__exit_cell:
            return Status.WIN

        if self.__total_accumulated_reward < self.__minimum_reward:  # force end of game after to much loss
            return Status.LOSE

        return Status.PLAYING

    def __observe(self):
        """ 
            Returns numpy.array [1][2]: agents current location
        """
        return np.array([[*self.__current_cell]])

    def play(self, model, start_cell=(0, 0)):
        """ 
            Parameters class AbstractModel model: the prediction model to use
                       tuple start_cell: agents initial cell (optional, else upper left)
            :return Status: WIN, LOSE
        """
        self.reset(start_cell)

        state = self.__observe()

        while True:
            action = model.predict(state=state)
            state, reward, status = self.step(action)
            if status in (Status.WIN, Status.LOSE):
                return status

    def check_win_all(self, model):
        """ 
            Check if the model wins from all possible starting cells. 
        """
        previous = self.__render
        self.__render = Render.NOTHING  

        win = lose = 0

        for cell in self.empty:
            if self.play(model, cell) == Status.WIN:
                win += 1
            else:
                lose += 1

        self.__render = previous  

        logging.info("won: {} | lost: {} | win rate: {:.5f}".format(win, lose, win / (win + lose)))

        result = True if lose == 0 else False

        return result, win / (win + lose)

    def render_q(self, model):
        """ 
            Param class AbstractModel model: the prediction model to use
        """
        def clip(n):
            return max(min(1, n), 0)

        if self.__render == Render.TRAINING:
            nrows, ncols = self.labyrinth.shape

            self.__ax2.clear()
            self.__ax2.set_xticks(np.arange(0.5, nrows, step=1))
            self.__ax2.set_xticklabels([])
            self.__ax2.set_yticks(np.arange(0.5, ncols, step=1))
            self.__ax2.set_yticklabels([])
            self.__ax2.grid(True)
            self.__ax2.plot(*self.__exit_cell, "gs", markersize=30)  
            self.__ax2.text(*self.__exit_cell, "Exit", ha="center", va="center", color="white")

            for cell in self.empty:
                q = model.q(cell) if model is not None else [0, 0, 0, 0]
                a = np.nonzero(q == np.max(q))[0]

                for action in a:
                    dx = 0
                    dy = 0
                    if action == Action.MOVE_LEFT:
                        dx = -0.2
                    if action == Action.MOVE_RIGHT:
                        dx = +0.2
                    if action == Action.MOVE_UP:
                        dy = -0.2
                    if action == Action.MOVE_BOTTOM:
                        dy = 0.2

                    
                    color = clip((q[action] - -1)/(1 - -1))

                    self.__ax2.arrow(*cell, dx, dy, color=(1 - color, color, 0), head_width=0.2, head_length=0.1)

            self.__ax2.imshow(self.labyrinth, cmap="binary")
            self.__ax2.get_figure().canvas.draw()