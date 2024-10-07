import numpy as np
from pathlib import Path
import random as rnd

class BaseModel:
    def checkInput(self, X: np.ndarray):
        if not isinstance(X, np.ndarray):
            raise TypeError(f"Incorrect type of X. Is of type {type(X)} not ndarray")
        ndim = len(X.shape)
        if ndim != 2:
            raise ValueError(f"Incorrect number of dimensions. Expected 2 got {ndim}")
        n, m = X.shape
        if n != 1:
            raise ValueError(f"incorrect shape: {X.shape}")
        
    def checkBatchInput(self, X: np.ndarray):
        if not isinstance(X, np.ndarray):
            raise TypeError(f"Incorrect type of X. Is of type {type(X)} not ndarray")
        ndim = len(X.shape)
        if ndim != 2:
            raise ValueError(f"Incorrect number of dimensions. Expected 2 got {ndim}")

    def predict(self, X: np.ndarray) -> float:
        raise NotImplementedError()
    
    def predictBatch(self, X: np.ndarray) -> list[float]:
        raise NotImplementedError()

    def save(self, filepath: Path):
        raise NotImplementedError()
    
    def load(self, filepath: Path):
        raise NotImplementedError()
    
    def __str__(self, ):
        raise NotImplementedError()
    


class RandomModel(BaseModel):
    def __init__(self, seed = None):
        self.name = "UniformRandomBaselineModel"
        self.seed = seed
        self.generator = rnd.Random()
        self.generator.seed(seed)

    def predict(self, X: np.ndarray) -> float:
        self.checkInput(X)
        return self.generator.random()
    
    def predictBatch(self, X: np.ndarray) -> list[float]:
        self.checkBatchInput(X)
        n, _ = X.shape
        return [self.generator.random() for i in range(n)]

    def save(self, filepath: Path):
        pass
    
    def load(self, filepath: Path):
        pass
    
    def __str__(self, ):
        return f"{self.name=},{self.seed=}"
    

