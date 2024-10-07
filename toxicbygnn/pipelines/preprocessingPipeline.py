from molvs import standardize_smiles
from rdkit.Chem import AllChem
from rdkit.Chem import MolFromSmiles
from rdkit.Chem import Mol
from rdkit.Chem import Descriptors
from pandas import DataFrame
import numpy as np



class ChemicalPreprocessor:
    def __init__(
            self,
            morgan_radius = 3,
            morgan_size = 2024):
        """
        morgan_radius -> the radius used to compute morgan fingerprints
        morgan_size -> the size of the morgan fingerprint vectors
        """
        self.morgan_radius = morgan_radius
        self.morgan_size = morgan_size
        self.fpgen = AllChem.GetMorganGenerator(radius=morgan_radius,fpSize=morgan_size)


    def getStandardizeSmiles(self, codes: list[str]) -> list[str]:
        return [
            standardize_smiles(el)
            for el in codes
        ]

    def getMoleculesFromSmiles(self, codes: list[str]) -> list[Mol]:
        chemicals = [
            MolFromSmiles(el)
            for el in codes
        ]
        return chemicals

    def getFingerprintFromMol(self, mols: list[Mol]) -> np.ndarray:
        fingerprints = [
            self.fpgen.GetFingerprintAsNumPy(mol)
            for mol in mols
        ]

        return np.stack(fingerprints, axis=0)
    
    def getDescriptorsFromMol(self, mols: list[Mol]) -> np.ndarray:
        descriptors = DataFrame([
            Descriptors.CalcMolDescriptors(mol)
            for mol in mols
        ])
        return descriptors.values

