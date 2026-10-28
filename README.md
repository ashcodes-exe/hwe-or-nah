# HWE or nah?
Stress testing the Hardy-Weinberg principle, proving the theory and its collapse irl
Hardy-Weinberg Stress Test

A simulation-based final project for my Python in Research course, built to test 
whether the Hardy-Weinberg Equilibrium (HWE) actually holds in finite, randomly 
sampled populations — not just on paper.

# What it does
- Calculates theoretical genotype frequencies (AA, Aa, aa) under HWE for a given allele frequency
- Simulates a finite population (n=1000) by randomly sampling genotypes based on those expected frequencies
- Runs a chi-square goodness-of-fit test comparing observed vs. expected counts
- Repeats this across many simulation cycles and plots the distribution of resulting p-values

# The point
HWE is often considered as if real populations should match it exactly. This project 
shows that even when a population is *generated* to follow HWE, random sampling 
alone causes a measurable fraction of simulations to deviate significantly 
(p < 0.05), proving the theory holds on average, but not in every finite sample.

# Built with
Python, SciPy, Matplotlib

# Run it
pip install scipy matplotlib
python hwe.ipynb
