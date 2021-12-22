# SUSY_DecisionTree
A 3-level decision tree achieves a 76.48% success rate in the SUSY file test (https://archive.ics.uci.edu/ml/datasets/SUSY)

Requirements:

Spyder 4

In the disk C:\ you should find the file SUSY.csv downloaded from  https://archive.ics.uci.edu/ml/datasets/SUSY

Functioning:

From Spyder 4 runs:

SUSY_DecisionTree.py

The last 500,000 SUSY.csv records are considered as tests, the first 4,500,000 records as training

You can use a different test file but that has the same structure as SUSY by changing the assignment of the file that appears in line 54 of the program and changing the values of the ContaMaxy Start parameters that appear at the beginning of the program.

The nodes and decision values have been obtained using the SUSYDecisionTree_C4-5_parameters.py program, which is attached to obtain the entropy of field 8 in the case of having already calculated the nodes and decision values up to 2.

References:

https://archive.ics.uci.edu/ml/datasets/SUSY

Diverse material of practices of the subject Artificial Intelligence of the Superior Polytechnic School of the Autonomous University of Madrid.

https://github.com/ablanco1950/SUSY_WEIGHTED_V1

Regarding accuracy:

The results offered on the website: http://physics.bu.edu/~pankajm/ML-Notebooks/HTML/NB5_CVII-logreg_SUSY.html

"Using Pyspark Environment for Solving a Big Data Problem: Searching for Supersymmetric Particles" Mourad Azhari, Abdallah Abarda, Badia Ettaki, Jamal Zerouaoui, Mohamed Dakkon International Journal of Innovative Technology and Exploring Engineering (IJITEE) ISSN: 2278-3075, Volume-9 Issue-7, May 2020 https://www.researchgate.net/publication/341301008_Using_Pyspark_Environment_for_Solving_a_Big_Data_Problem_Searching_for_Supersymmetric_Particles 
