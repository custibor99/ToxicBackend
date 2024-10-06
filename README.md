
# ToxicByGNN <br>  A platform for chemical toxicity prediction 

Toxicology prediction of chemical compounds is a critical step in pharmaceutical research, environmental safety, and chemical engineering. Predicting whether a molecule will exhibit toxic properties helps reduce the time, cost, and risk associated with developing new drugs or assessing environmental hazards. Traditionally, classical machine learning (ML) methods such as random forests, support vector machines (SVMs), and decision trees have been widely used for molecular toxicity prediction. However, the recent rise of graph neural networks (GNNs) presents a new approach that can potentially outperform classical methods due to their ability to capture complex graph structures of molecules. This project aims to investigate whether GNNs can outperform classical ML methods in predicting molecular toxicity by leveraging the inherent graph structure of molecules.

## Data Description
I will use the Tox21[3], ClinTox[4], and Comprehensive chemical compounds [5] datasets.  The Tox21 dataset consists of molecular compounds labeled with their toxicological effects based on 12 different toxicity types. ClinTox contains molecular compounds and whether or not a compound failed clinical phase trials. The final dataset only contains molecular structures and no toxicology endpoints as its primary use will be for unsupervised model training.

The molecules are represented using SMILES (Simplified Molecular Input Line Entry System), which can be converted into graph structures. An example of a smile representation:

<p align="center">
<b>Clc(c(Cl)c(Cl)c1C(=O)O)c(Cl)c1Cl</b>
</p>
The same molecule can be represented in different smile formats, which is why we will standardize them using MolVS [7]

Based on a molecule's SMILE we can calculate statistical descriptors, for that, we will use Rdkit[6]. Rdkit can also be used to calculate Morgan fingerprints which is a form of vector representation of chemical compounds. Both Morgan fingerprints and Statistical descriptors will be used as features for Traditional ML methods.

The datasets contain the following features
### Tox21
- **Size:** 8000 molecules.
- **Input Features:** SMILES representation of molecules (to be converted into graphs).
- **Target Variables:** 12 Toxicity labels (binary).

### ClinTox
- **Size:** 1491 molecules.
- **Input Features:** SMILES representation of molecules (to be converted into graphs).
- **Target Variables:** Passed clinical trial (binary).

### Comprehensive chemical compounds Datase
- **Size:** 21804 molecules.
- **Input Features:** SMILES representation of molecules & molecule weight.
- **Target Variables:** None

The dataset splits will follow the splits in Sharma[1] so that our results can also be compared to state-of-the-art methods, even tho that is not the goal of this project. 

## Technologies used
### Python and Libraries
Python is the core programming language for the project, utilizing several key libraries:

- **PyTorch** and **PyTorch Geometric (PyG)**: Used to design, build, and train graph neural networks (GNNs) efficiently, especially for handling graph data.
- **Scikit-learn (sklearn)**: Employed to implement classical machine learning models (Random Forest, SVM) to benchmark against GNN performance.
- **RDKit and MolVS**: Essential for processing chemical data, converting SMILES to graph representations, and ensuring consistency in molecular structures.
### Database and Storage
**PostgreSQL** with **Pgvector Extension**: Used to store molecular data, model outputs, and graph embeddings. Pgvector allows efficient storage and querying of vector data.
### Application Framework
**Streamlit:** This Python-based framework will be used to create the final web-based application where users can input SMILES strings to predict the toxicity of molecules in real time. Streamlit is easy to integrate with Python models and offers a fast way to build interactive applications without needing extensive web development experience.

## Work Breakdown
<div align="center">

| **Task** &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|**Hours** &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|
|--------------------------------------|-------|
| Research and Project Planning        | 5     |
| Dataset Collection and Preprocessing | 5     |
| Preparing classical Models           | 5     |
| Model Design and Implementation      | 15    |
| Model Training and Fine-Tuning       | 15    |
| Model Evaluation and Comparison      | 10    |
| Application Development              | 10    |
| Report Writing and Presentation      | 10    |
|                                      |       |
| **Total**                            | **75**|

</div>


## References
[1] Sharma, B., Chenthamarakshan, V., Dhurandhar, A. et al. Accurate clinical toxicity prediction using multi-task deep neural nets and contrastive molecular explanations. Sci Rep 13, 4908 (2023). https://doi.org/10.1038/s41598-023-31169-8

[2] A Review on the Recent Applications of Deep Learning in Predictive Drug Toxicological Studies Krishnendu Sinha, Nabanita Ghosh, and Parames C. Sil
Chemical Research in Toxicology 2023 36 (8), 1174-1205
DOI: 10.1021/acs.chemrestox.2c00375

[3] Tox21 Dataset, https://github.com/deepchem/deepchem/tree/master/datasets

[4] ClinTox Dataset, https://github.com/deepchem/deepchem/tree/master/examples/clintox/datasets

[5] Comprehensive chemical compounds Dataset, https://www.kaggle.com/datasets/mahinshikder/comprehensive-chemical-compounds-catalog 

[6] Rdkit for python, https://www.rdkit.org/docs/GettingStartedInPython.html

[7] MolVS for python, https://molvs.readthedocs.io/en/latest/



