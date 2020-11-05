import sys

sys.path.append("/home/michaela/kaggle/answer_prediction_kaggle/riiideducation")

import riiideducation
env = riiideducation.make_env()

with timer('cuDF'):
    df = cudf.read_csv('../train.csv')

