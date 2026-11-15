import numpy as np
c = np.array([[0,0],[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]) # c[i] = the discrete velocity model for D2Q9
w = np.array([4/9,1/9,1/9,1/9,1/9,1/36,1/36,1/36,1/36]) # w[i]= the weight of the discrete velocities for D2Q9
assert np.isclose(w.sum(),1.0),"Check 1 failed:weights do not sum to 1"  #  the sum of the weights should be 1
drift_x = (w*c[:,0]).sum() #the drift velocity in x direction
assert np.isclose(drift_x,0.0),"Check 2 failed: drift velocity in x direction is not equal to 0"
drift_y = (w*c[:,1]).sum()#drift velocity in y direction
assert np.isclose(drift_y,0.0),"Check 2 failed: drift velocity in y direction is not equal to 0"
spread_x = (c[:,0]**2*w).sum()
assert np.isclose(spread_x,1/3),"Check 3 failed: spread in x direction is not equal to 1/3 "
cross_xy = (w*c[:,0]*c[:,1]).sum()
assert np.isclose(cross_xy,0.0),"Check 4 failed: The cross term of x and y step is not equal to 0 "
print("All checks passed")
def equilibrium(rho,u):#rho is the density u is the velocity array
     cu=c[:,0]*u[0]+c[:,1]*u[1]
     uu=u[0]**2+u[1]**2
     feq=w*rho*(1+3*(cu)+4.5*(cu)**2-1.5*uu)
     return feq
test_cases = [
    (1.0, np.array([0.1, 0.0])),
    (1.2, np.array([0.05,-0.02])),
    (0.8,np.array([0.0, 0.0]))
]
for rho, u in test_cases:
    feq=equilibrium(rho,u)
    #print(feq) This line is required for verification 
    assert np.isclose(feq.sum(),rho),"Check 1 failed: The sum of the distribution function is not equal to denisty"
    velocity_x=(feq*c[:,0]).sum()/rho
    assert np.isclose(velocity_x,u[0]),"Check 2 failed: The velocity in x direction is not equal to u[0]"
    velocity_y=(feq*c[:,1]).sum()/rho
    assert np.isclose(velocity_y,u[1]),"Check 3 failed: The velocity in y direction is not equal to u[1]"
print("Equilibrium tests passes")