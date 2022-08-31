# test Reinforcment learning Python
import numpy as np 
import logging
from random import randint
from enum import Enum, IntEnum

class EnvironmentLabyrinthGrid():
    
    labyrinth_version: tuple = ("1", "2", "3")
    
    def __init__(self, labyrinth_coordinates):
        self.labyrinth_coordinates = labyrinth
    
    ACTIONS: list = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1]
        ]    
    start_position = [0,0]
    # reset()

    def __str__(self):
        return f'Labyrinth grid: {self.labyrinth_coordinates}'

    def __repr__(self):
        return f'<Labyrinth: {self.labyrinth_coordinates}>'

    @classmethod
    def get_labyrinth_version(cls, labyrinth_coordinates):
        return cls(labyrinth_coordinates, cls.labyrinth_version[0])    


    def print_labyrinth_coordinates_beautified(self):
        """

        Returns the labyrinth as a visual 2D grid
        -------
        None.

        """
        for item in labyrinth:
            if not item == -1:
                separator = '    '
            else:
                separator = ' '    
            print(*item, sep=separator)
        
    def reset(self):
        """
        Resets the agent's position

        Returns
        -------
        None.

        """
        self.x = self.start_position[0]
        self.y = self.start_position[1]

    def take_action():
        pass 

if __name__ == '__main__':
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
    labyrinthGrid = EnvironmentLabyrinthGrid(labyrinth)
    print(labyrinthGrid)
    labyrinthGrid.print_labyrinth_coordinates_beautified()
   
    # faire un np array 2D pour faire du 36(états) x 4 (4 actions)
    # si trésor trouvé, état altéré -> faire 36 états lorsqu'il aura le trésor. 
    # Q(s,a) : étant actuellement état s, à quel point l'action a est un bon chemin? 
    # partir du code existant, en modifiant le grille du code
    # ajouter les trésor et la modification du nombre d'états 
    q_table = [[0 for i in range(4)] for j in range(36)]
    q_table_state_with_treasure = [[o for i in range(4)] for j in range(36)]
    print("Generated Q Table: \n")
    for item in q_table:
            if not item == -1:
                separator = '    '
            else:
                separator = ' '    
            print(*item, sep=separator)
    print(f'Generated Q Table: {q_table}')