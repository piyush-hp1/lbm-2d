import numpy as np
c = np.array([[0,0],[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]) # c[i] = the discrete velocity model for D2Q3
w = np.array([4/9,1/9,1/9,1/9,1/9,1/36,1/36,1/36,1/36]) # w[i]= the weight of the dicrete velocities for D2Q3
assert np.isclose(w.sum(),1.0),"Check 1 failed:weights do not sum to 1"  #  the sum of the weights should be 1
drift_x = (w*c[:,0]).sum() #the drift velocity in x direction
assert np.isclose(drift_x,0.0),"Check 2 failed: drift velocits in x direction is not equal to 0"
drift_y = (w*c[:,1]).sum()#drift velocity in y direction
assert np.isclose(drift_y,0.0),"Check 2 failed: drift velocits in y direction is not equal to 0"
spread_x = (c[:,0]**2*w).sum()
assert np.isclose(spread_x,1/3),"Check 3 failed: spread in x direction is not equal to 1/3 "
cross_xy = (w*c[:,0]*c[:,1]).sum()
assert np.isclose(cross_xy,0.0),"Check 4 failed: The cross term of x and y step is not equal to 0 "
print("All checks passed")