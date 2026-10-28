import random
from scipy.stats import chisquare
import matplotlib.pyplot as plt 


# Function to calculate expected genotype frequencies under Hardy-Weinberg Equilibrium
def hardy_weinberg_expected(p, total):
    q = 1 - p
    return {
        'AA': p**2 * total,
        'Aa': 2*p*q * total,
        'aa': q**2 * total
    }

significant_count = 0 # Initialize counter to count how many simulations significantly deviate from HWE
p_vals = [] # Store p-values from each simulation

no_sim = int(input("Enter the number of cycles you want: "))

# Run simulations
for i in range(no_sim):
    p = random.uniform(0.01, 1.0)
    total_population = 1000
    
    expected = hardy_weinberg_expected(p, total_population) # Calculate expected genotype frequencies based on current p
    
    # Simulate observed genotype distribution
    genotypes = random.choices(
        population=['AA', 'Aa', 'aa'],
        weights=[expected['AA'], expected['Aa'], expected['aa']],
        k = total_population
    )
    
    # Count the actual occurrences of each genotype in the simulated population
    observed_counts = {'AA': 0, 'Aa': 0, 'aa': 0}
    for g in genotypes:
        observed_counts[g] += 1

    # Convert dictionaries to lists so we can use them in the chi-square test
    observed_list = [observed_counts['AA'], observed_counts['Aa'], observed_counts['aa']]
    expected_list = [expected['AA'], expected['Aa'], expected['aa']]

    # Run Chi-square test
    chi_stat, p_value = chisquare(f_obs=observed_list, f_exp=expected_list)

    # Save the p-value
    p_vals.append(p_value)
    
    # Count how many simulations deviate significantly (p < 0.05)
    if p_value < 0.05:
        significant_count += 1

    # Print results for this simulation cycle
    print(f"Cycle {i+1:02d} | p = {p:.3f}")
    print(f"  Observed counts ➜ AA: {observed_counts['AA']}, Aa: {observed_counts['Aa']}, aa: {observed_counts['aa']}")
    print(f"  Expected counts ➜ AA: {expected['AA']:.1f}, Aa: {expected['Aa']:.1f}, aa: {expected['aa']:.1f}")
    print(f"  Chi-Square = {chi_stat:.3f}, p-value = {p_value:.3f}")
    print(f"{' DEVIATES from HWE' if p_value < 0.05 else ' FITS HWE'}\n")

# Summary stats: print how many showed significant deviation from HWE
print(f"Out of {no_sim} simulations, {significant_count} deviated significantly from Hardy-Weinberg (p < 0.05).")
print(f"The failure rate observed due to sampling error is: {(significant_count/no_sim)*100:.2f}%")

# Plotting p-value distribution
plt.hist(p_vals, bins=20, orientation = "horizontal", edgecolor='black')
plt.axhline(y=0.05, color='red', linestyle='--', label='Significance threshold (p = 0.05)') 
    # Add a red dashed line at the 0.05 significance threshold
plt.title("Distribution of p-values from Hardy-Weinberg Simulations")
plt.xlabel("Frequency")
plt.ylabel("p-value")
plt.legend()
plt.show()
