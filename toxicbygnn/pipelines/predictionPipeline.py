from toxicbygnn.models import BaseModel
from toxicbygnn.pipelines.preprocessingPipeline import ChemicalPreprocessor
import pandas as pd

class PredictionPipeline:
    def __init__(self, 
                preprocessor: ChemicalPreprocessor,
                classical_models: list[BaseModel] = [],
                deep_models: list[BaseModel] = [],
                ):
        self.preprocessor = preprocessor
        self.classical_models = classical_models
        self.deep_models = deep_models

    def predict(self, smiles: list[str]) -> pd.DataFrame:
        X = self.preprocessor.getStandardizeSmiles(smiles)
        X = self.preprocessor.getMoleculesFromSmiles(X)
        X = self.preprocessor.getDescriptorsFromMol(X)

        result = {
            "smile" : [],
            "model" : [],
            "prediction": []
            }
        print(f"Start processing {len(self.classical_models)} classical models")
        for i, model in enumerate(self.classical_models):
            print(f"\t{i+1}. {model.name}")
            pred = model.predictBatch(X)
            result["prediction"] += pred
            result["model"] += [model.name] * len(smiles)
            result["smile"] += smiles
    
        return pd.DataFrame(result).head()