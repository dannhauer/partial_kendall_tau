## Partial Kendall's Tau Correlation

This Python module contains a function to calculate the partial Kendall's tau correlation coefficient between two variables while controlling for a third variable. Additionally, it estimates the standard error of the coefficient via bootstrapping and provides a p-value using a permutation test.

**Function Overview**

partial_kendall_tau
This function calculates the partial Kendall's tau correlation coefficient between two arrays, x and y, while controlling for the third array, z. The function also estimates the standard error of the partial correlation using bootstrapping and calculates the p-value using a permutation test.

Parameters:
x: array-like, shape (n,)
y: array-like, shape (n,)
z: array-like, shape (n,)
num_bootstraps: int, default=1000. Number of bootstrap samples to use for estimating the standard error.
Returns:
p_corr: float. The partial Kendall's tau correlation coefficient.
se_p_corr: float. The standard error of the partial correlation coefficient from bootstrapping.
p_val: float. The p-value from the permutation test.

**Use Case: Astrophysics Example**

In astrophysics, this function can be used to analyze the trend between luminosities in flux-limited samples while correcting for the effect of redshift. For example, when studying the relationship between two luminosity measurements, one might want to account for the influence of redshift to determine if the observed correlation is intrinsic or driven by the redshift.
