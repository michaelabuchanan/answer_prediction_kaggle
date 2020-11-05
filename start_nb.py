import riiideduction
env = riiideduction.make_env()

with timer('cuDF'):
    df = cudf.read_csv('../train.csv')