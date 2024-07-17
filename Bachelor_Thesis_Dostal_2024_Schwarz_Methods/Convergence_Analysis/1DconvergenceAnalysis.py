import numpy as np
import matplotlib.pyplot as plt

# Functions to calculate the errors
def e1(x, e2_d):
    return e2_d * (x - a) / (d - a)

def e2(x, e1_c):
    return e1_c * (b - x) / (b - c)

# Domain boundaries
a = 0
b = 8
d = 5
c = 4.7

# Generate x values for subdomains
x1 = np.linspace(a, d, 100)
x2 = np.linspace(c, b, 100)

# Assume initial errors
e2_d_initial = 1

# Calculate error values for the first iteration
e1_values = e1(x1, e2_d_initial)
e1_c = e1(c, e2_d_initial)
e2_values = e2(x2, e1_c)

# Calculate error values for the second iteration
e1_values_2 = e1(x1, e2(d, e1_c))
e1_c_2 = e1(c, e2(d, e1_c))
e2_values_2 = e2(x2, e1_c_2)

# Calculate error values for the third iteration
e1_values_3 = e1(x1, e2(d, e1_c_2))
e1_c_3 = e1(c, e2(d, e1_c_2))
e2_values_3 = e2(x2, e1_c_3)

# Calculate error values for the fourth iteration
e1_values_4 = e1(x1, e2(d, e1_c_3))
e1_c_4 = e1(c, e2(d, e1_c_3))
e2_values_4 = e2(x2, e1_c_4)

# Plot the errors
plt.figure(figsize=(10, 6))
plt.plot(x1, e1_values, 'k')
plt.plot(x2, e2_values, 'r')
plt.plot(x1, e1_values_2, 'k--')
plt.plot(x2, e2_values_2, 'r--')
plt.plot(x1, e1_values_3, 'k-.')
plt.plot(x2, e2_values_3, 'r-.')
plt.plot(x1, e1_values_4, 'k:')
plt.plot(x2, e2_values_4, 'r:')

plt.axvline(x=d, color='purple', linestyle='--', label='$d$')
plt.axvline(x=c, color='green', linestyle='--', label='$c$')

# Add delta annotation on the x-axis
plt.annotate(r'$\delta$', xy=(c, -0.1), xytext=(d, -0.1),
             arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5), fontsize=12, color='blue', ha='center')

# Fill delta region
plt.axvspan(c, d, color='gray', alpha=0.3, label='$\delta$')

plt.xlabel('x')
plt.ylabel('Error')

# Annotate the lines
plt.text((d-a)/2, e1((d-a)/2, e2_d_initial) + 0.05, '$e_1^{1}$', color='k', fontsize=12, ha='center')
plt.text((b+c)/2, e2((b+c)/2, e1_c) + 0.03, '$e_2^{1}$', color='r', fontsize=12, ha='center')
plt.text((d-a)/2, e1((d-a)/2, e2(d, e1_c)) + 0.03, '$e_1^{2}$', color='k', fontsize=12, ha='center')
plt.text((b+c)/2, e2((b+c)/2, e1_c_2) + 0.03, '$e_2^{2}$', color='r', fontsize=12, ha='center')
plt.text((d-a)/2, e1((d-a)/2, e2(d, e1_c_2)) + 0.03, '$e_1^{3}$', color='k', fontsize=12, ha='center')
plt.text((b+c)/2, e2((b+c)/2, e1_c_3) + 0.02, '$e_2^{3}$', color='r', fontsize=12, ha='center')
plt.text((d-a)/2, e1((d-a)/2, e2(d, e1_c_3)) - 0.05, '$e_1^{4}$', color='k', fontsize=12, ha='center')
plt.text((b+c)/2, e2((b+c)/2, e1_c_4) - 0.06, '$e_2^{4}$', color='r', fontsize=12, ha='center')

plt.legend(loc='upper right', prop={'size': 15})

plt.grid(True)

# Save the figure
plt.savefig("1D_Convergence_Schwarz_Overlap.pdf")
plt.show()
