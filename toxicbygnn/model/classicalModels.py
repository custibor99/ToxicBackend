from toxicbygnn.model.BaseModel import BaseModel
import numpy as np
from pathlib import Path
import random as rnd

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
    

