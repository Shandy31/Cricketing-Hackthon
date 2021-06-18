### Imports ###
# add imports - classes and defs
import sys
from predictor import predictRuns


"""
sys.argv[1] is the input test file name given as command line arguments

"""
runs = predictRuns(r'C:\Users\Dell\Desktop\cric hackthon\input_test_data.csv')
print("Predicted Runs: ", runs)