import riiideducation
env = riiideducation.make_env()

with timer('cuDF'):
    df = cudf.read_csv('../train.csv')