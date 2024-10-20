import streamlit as st
import pandas as pd
import numpy as np

from toxicbygnn.models.classicalModels import RandomModel
from toxicbygnn.pipelines.preprocessingPipeline import ChemicalPreprocessor
from toxicbygnn.pipelines.predictionPipeline import PredictionPipeline



classical_models = [
    RandomModel(name="model1"),
    RandomModel(name="model2"),
    RandomModel(name="model3")
    ]
preprocessor = ChemicalPreprocessor()
predictor = PredictionPipeline(preprocessor, classical_models)


st.title('Chemical toxicology prediction')

if "predictions" not in st.session_state:
    st.session_state["predictions"] = pd.DataFrame(columns=['smile', 'model', 'prediction'])

smile = st.text_input('Enter a SMILE')
is_clicked = st.button('Predict')
if is_clicked:
    st.session_state["predictions"] = pd.concat([
        st.session_state["predictions"],
        predictor.predict([smile]),
    ]) 


st.dataframe(st.session_state["predictions"], hide_index=True, use_container_width=True, height=400)
