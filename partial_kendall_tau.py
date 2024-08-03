from scipy.stats import kendalltau, t
import numpy as np

x = []
y = []
z= []

def partial_kendall(x, y, z, num_bootstraps=1000):
    """
    Calculate the partial correlation coefficient between x and y controlling for z.
    """
    # Calculate the correlation between x and y
    r_xy, _ = kendalltau(x, y)
    
    # Calculate the correlation between x and z
    r_xz, _ = kendalltau(x, z)
    
    # Calculate the correlation between y and z
    r_yz, _ = kendalltau(y, z)
    
    # Calculate the partial correlation coefficient between x and y controlling for z
    num = r_xy - (r_xz * r_yz)
    den = ((1 - r_xz ** 2) * (1 - r_yz ** 2)) ** 0.5
    p_corr = num / den
    
    # Calculate the degrees of freedom for the t-distribution
    n = len(x)
    df = n - 3
    
    # Calculate the t-statistic
    t_stat = p_corr * ((df / (1 - p_corr ** 2)) ** 0.5)
    
    # Calculate the p-value
    p_val = (1 - t.cdf(abs(t_stat), df)) * 2

    '''
    # Permutation test for p-value
    p_corr_perm = np.zeros(num_bootstraps)
    for i in range(num_bootstraps):
        np.random.shuffle(y)
        r_xy_perm, _ = kendalltau(x, y)
        r_xz_perm, _ = kendalltau(x, z)
        r_yz_perm, _ = kendalltau(y, z)
        num_perm = r_xy_perm - (r_xz_perm * r_yz_perm)
        den_perm = ((1 - r_xz_perm ** 2) * (1 - r_yz_perm ** 2)) ** 0.5
        p_corr_perm[i] = num_perm / den_perm
    
    p_val = np.mean(np.abs(p_corr_perm) >= np.abs(p_corr))
    '''
    

    
    # Bootstrap to get the standard error of the partial correlation coefficient
    p_corr_bootstraps = np.zeros(num_bootstraps)
    for i in range(num_bootstraps):
        indices = np.random.choice(n, size=n, replace=True)
        x_boot = x[indices]
        y_boot = y[indices]
        z_boot = z[indices]
        r_xy_boot, _ = kendalltau(x_boot, y_boot)
        r_xz_boot, _ = kendalltau(x_boot, z_boot)
        r_yz_boot, _ = kendalltau(y_boot, z_boot)
        num_boot = r_xy_boot - (r_xz_boot * r_yz_boot)
        den_boot = ((1 - r_xz_boot ** 2) * (1 - r_yz_boot ** 2)) ** 0.5
        p_corr_bootstraps[i] = num_boot / den_boot
    
    se_p_corr = np.std(p_corr_bootstraps, ddof=1)
    
    return p_corr, se_p_corr, p_val

########## USAGE ##########

p_corr, se_p_corr, p_val = partial_kendall(x, y, z)
print("Partial correlation coefficient:", p_corr)
print("Partial correlation standard error:", se_p_corr)
print("p-value:", p_val)
