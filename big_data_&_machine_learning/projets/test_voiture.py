### Code origiennellement par @Thibault Neveu - https://github.com/thibo73800 
### Modifié par Claire Perrot - janvier 2021

import numpy as np
from random import randint
import random

class EnvGrid(object):

    def __init__(self):
        super(EnvGrid, self).__init__()

        self.grid = [
            [0, 0, 1],
            [0, -1, 0],
            [0, 0, 0]
        ]

        # starting position
        self.st_pos = [0,2]
        self.reset()

        self.actions = [
            [-1, 0], # Up
            [1, 0], #Down
            [0, -1], # Left
            [0, 1] # Right
        ]

    def get_state(self):
        return self.y*3 + self.x + 1

    def reset(self):
        """
            Reset du jeu
        """
        self.x = self.st_pos[0]
        self.y = self.st_pos[1]

    def step(self, action):
        """
            Action: 0, 1, 2, 3;
            mise a jour de la position + retourne l'état d'arrivée et la récompense
        """
        self.y = max(0, min(self.y + self.actions[action][0],2))
        self.x = max(0, min(self.x + self.actions[action][1],2))

        return self.get_state(), self.grid[self.y][self.x]

    def show(self):
        """
            Show the grid
        """
        print("---------------------")
        y = 0
        for line in self.grid:
            x = 0
            for pt in line:
                print("%s\t" % (pt if y != self.y or x != self.x else "X"), end="")
                x += 1
            y += 1
            print("")

    def is_finished(self):
        return self.grid[self.y][self.x] == 1 ## on est arrives au but

def take_action(st, Q, eps):
    # Choisir une action (retourne l'action choisie)
    if random.uniform(0, 1) < eps: # exploration
        action = randint(0, 3)
    else: # exploitation, on vient chercher la valeur la plus haute dans la Q table  
        action = np.argmax(Q[st])
    return action

if __name__ == '__main__':
    env = EnvGrid()
    env.reset()
    st = env.get_state()

    Q = [
        [0, 0, 0, 0], ## pour l'état 0 (n'existe pas)
        [0, 0, 0, 0], ## pour l'état 1
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    
    for _ in range(20):
        # Reset
        env.reset()
        st = env.get_state()
        
        while not env.is_finished(): ## on est pas encore sur la case finale
            #env.show()
            #at = int(input("$>"))
            action = take_action(st, Q, 0.4)

            stp1, r = env.step(action)
            #print("s", stp1)
            #print("r", r)

            # Mise à jour de la Q-table
            atp1 = take_action(stp1, Q, 0.0)
            Q[st][action] = Q[st][action] + 0.1*(r + 0.9*Q[stp1][atp1] - Q[st][action])

            st = stp1

    ## affichage de la Q-table finale
    print('     up     down    left   right')
    for s in range(1, 10):
        formatted_Q = [ '%.2f' % elem for elem in Q[s] ]
        print(s, formatted_Q)
    
    ## affichage de la policy finale apprise et du nombre d'étapes
    env.reset()
    s = env.get_state()
    print("starting state", s)
    nb_steps = 0
    while not env.is_finished():
        a = take_action(s,Q,0.0)
        next_state, reward = env.step(a)
        print("state", next_state)
        s = next_state
        nb_steps += 1
    print("fin du parcours en", nb_steps, "etapes")