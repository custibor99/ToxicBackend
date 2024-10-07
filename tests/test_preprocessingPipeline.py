import pytest
from toxicbygnn.pipelines.preprocessingPipeline import ChemicalPreprocessor
from rdkit.Chem import Mol
import numpy as np

SMILES = [
    'C1CCC1OCC',
    'CC(C)OCC',
    'CCOCC',
]

preprocessor = ChemicalPreprocessor()

def testStandardization():
    standardized = preprocessor.getStandardizeSmiles(SMILES)
    assert len(standardized) == len(SMILES)
    for el in standardized:
        assert isinstance(el, str)

def testGetMoleculesFromSMILES():
    molecules = preprocessor.getMoleculesFromSmiles(SMILES)
    assert len(molecules) == len(SMILES)
    for el in molecules:
        assert isinstance(el, Mol)    

def testGetFingerprintFromMol():
    molecules = preprocessor.getMoleculesFromSmiles(SMILES)
    prints = preprocessor.getFingerprintFromMol(molecules)
    isinstance(prints, np.ndarray)
    assert prints.shape == (3, 2024)

def testGetDescriptorsFromMol():
    molecules = preprocessor.getMoleculesFromSmiles(SMILES)
    descriptors = preprocessor.getDescriptorsFromMol(molecules)
    isinstance(descriptors, np.ndarray)
    assert descriptors.shape == (3, 210) 
    print(descriptors.shape)
