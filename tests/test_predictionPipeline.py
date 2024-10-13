import pytest
from toxicbygnn.models.classicalModels import RandomModel
from toxicbygnn.pipelines.preprocessingPipeline import ChemicalPreprocessor
from toxicbygnn.pipelines.predictionPipeline import PredictionPipeline
import pandas as pd


def test_prediction_pipeline():
    classical_models = [
        RandomModel(name="model1"),
        RandomModel(name="model2"),
        RandomModel(name="model3")
        ]
    preprocessor = ChemicalPreprocessor()
    predictor = PredictionPipeline(preprocessor, classical_models)

    SMILES = [
        'C1CCC1OCC',
        'CC(C)OCC',
        'CCOCC',
    ]

    res = predictor.predict(SMILES)
    
    assert isinstance(res, pd.DataFrame)
    assert len(res.columns) == len(classical_models) + 1
    assert len(res) == len(SMILES)
    for model in classical_models:
        assert model.name in res.columns

def test_prediction_pipeline_empty():
    classical_models = [
        RandomModel(name="model1"),
        RandomModel(name="model2"),
        RandomModel(name="model3")
    ]
    preprocessor = ChemicalPreprocessor()
    predictor = PredictionPipeline(preprocessor, classical_models)

    SMILES = []

    res = predictor.predict(SMILES)
    
    assert isinstance(res, pd.DataFrame)
    assert len(res.columns) == len(classical_models) + 1
    assert len(res) == len(SMILES)
    for model in classical_models:
        assert model.name in res.columns