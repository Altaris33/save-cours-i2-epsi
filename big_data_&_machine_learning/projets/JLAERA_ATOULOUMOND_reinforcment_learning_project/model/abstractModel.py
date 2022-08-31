from abc import ABC, abstractmethod


class AbstractModel(ABC):
    def __init__(self, maze, **kwargs):
        self.environment = maze
        self.name = kwargs.get("name", "model")

    def load(self, filename):
        """ 
            Loads model from file. 
        """
        pass

    def save(self, filename):
        """
            Save model to file. 
        """
        pass

    def train(self, stop_at_convergence=False, **kwargs):
        """ 
            Trains model if training is performed. 
        """
        pass

    @abstractmethod
    def q(self, state):
        """ 
            Returns q values for state. 
            """
        pass

    @abstractmethod
    def predict(self, state):
        """ 
            Predict value based on state. 
        """
        pass