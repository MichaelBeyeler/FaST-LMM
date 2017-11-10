import os
os.chdir('../FaST-LMM-master')

import logging
import numpy as np
from fastlmm.association import single_snp
from pysnptools.snpreader import Bed
logging.basicConfig(level=logging.INFO)
pheno_fn = "fastlmm/feature_selection/examples/toydata.phe"
results_dataframe = single_snp(test_snps="fastlmm/feature_selection/examples/toydata.5chrom", pheno=pheno_fn)
print results_dataframe.iloc[0].SNP,round(results_dataframe.iloc[0].PValue,7),len(results_dataframe)