from toxicbygnn.model.classicalModels import RandomModel
import numpy as np
import pytest

models = [RandomModel()]

def test_predict():
    x1 = np.ones([1,1])
    x2 = np.ones([3,1])
    x3 = [1,2,3]

    for model in models:
        assert isinstance(model.predict(x1), float)
        with pytest.raises(ValueError):
            model.predict(x2)
        with pytest.raises(TypeError):
            model.predict(x3)

def test_batchPredict():
    x1 = np.ones([3,1])
    x2 = np.ones([3,1,1])
    x3 = [1,2,3]

    for model in models:
        assert isinstance(model.predictBatch(x1), list)
        with pytest.raises(ValueError):
            model.predict(x2)
        with pytest.raises(TypeError):
            model.predict(x3)
        