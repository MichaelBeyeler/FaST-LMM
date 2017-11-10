import os
os.chdir('../FaST-LMM-master')

from fastlmm.association import single_snp

test_snps = "../Data/dgrp2"
test_snps_published = '../Outputs/Plinkfiles/Dgrp2-Tergite-Online'
#test_snps_maf5 = '../Outputs/Plinkfiles/
variants_maf5_lines_filtered = '../Outputs/Plinkfiles/dgrp2_maf5_linesfiltered'
test_snps_maf5_head = '../Outputs/Plinkfiles/dgrp2_maf5_head'
phenotypes = "../Outputs/Fast-Lmm-Inputs/T5-Pheno-for-Fast-Lmm.txt"
phenotypes_online = '../Outputs/Fast-Lmm-Inputs/T5-Pheno-Online-for-Fast-Lmm.txt'
pheno_all_lines = '../Outputs/Fast-Lmm-Inputs/Test-Phenotype-All-Lines.txt'

#cov_fn = "../../tests/datasets/synth/cov.txt"


# Running GWAS
###############################################################################
results_df = single_snp(variants_maf5_lines_filtered,  phenotypes_online,
                             leave_out_one_chrom=False, output_file_name='Test-Fast-Lmm')

import pylab
import fastlmm.util.util as flutil
flutil.manhattan_plot(results_df.as_matrix(["Chr", "ChrPos", "PValue"]),pvalue_line=1e-5,xaxis_unit_bp=False)
pylab.show()

from fastlmm.util.stats import plotp
plotp.qqplot(results_df["PValue"].values, xlim=[0,5], ylim=[0,5])

# print head of results data frame
import pandas as pd
pd.set_option('display.width', 1000)
results_df.head(n=10)

results_df.to_csv('../Outputs/Fast-Lmm-Outputs/Quality-Control-Tergite-Online-Adjusted-Phenotype-Leave-False.txt', sep='\t')


from pysnptools.standardizer import Unit
from fastlmm.inference.fastlmm_predictor import _snps_fixup, _pheno_fixup, _kernel_fixup, _SnpTrainTest
test_snps = _snps_fixup(test_snps)
K_causal = test_snps.read_kernel(Unit()).standardize()
pylab.imshow(K_causal.val, cmap=pylab.gray(), vmin=0, vmax=1)
