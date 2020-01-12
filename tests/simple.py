import sys; sys.path.append("G:\\Repos")


import numpy as np
import pandas as pd
import scipy
from scipy import stats
import trikit

from trikit.chainladder import BaseChainLadder
from trikit.chainladder.mack import MackChainLadder
from trikit.chainladder.bootstrap import BootstrapChainLadder




raa  = trikit.load(dataset="raa")
ta83 = trikit.load(dataset="ta83")
auto = trikit.load(dataset="lrdb", lob="COM_AUTO", grcode=32743)



tri = trikit.totri(data=raa)
cl_ = BaseChainLadder(tri)
cl = cl_.__call__()


mcl_ = MackChainLadder(tri)
mcl = mcl_.__call__()

tri = cl.trisqrd
tri = tri.reset_index(drop=False).rename({"index":"origin"}, axis=1)
df = pd.melt(tri, id_vars=["origin"], var_name="dev", value_name="value").drop("value", axis=1)
df = df[df.dev!="ultimate"].reset_index(drop=True)


raa  = trikit.load(dataset="raa")
itri = trikit.totri(data=raa, type_="incr")
tt = itri.as_tbl()

df = df.merge(tt, how="outer", on=["origin", "dev"])

tt.to_csv("G:\\Repos\\GT\\ISYE6420\\Project\\RAA0.csv", index=False, sep=",")




bcl = BootstrapChainLadder(tri)

df = pd.melt(cl.trisqrd, id_vars=[cl.trisqrd.index], value_vars=cl.trisqrd.columns, var_name="dev", value_name="value")

df = pd.melt(cl.trisqrd, id_vars=[cl.trisqrd.columns], var_name="dev", value_name="value")
df_ = df_[~np.isnan(df_[self.value])]
        df_ = df_.astype({self.origin:np.int_, self.dev:np.int_, self.value:np.float_})
        return(df_.sort_values(by=[self.origin, self.dev]).reset_index(drop=True))
