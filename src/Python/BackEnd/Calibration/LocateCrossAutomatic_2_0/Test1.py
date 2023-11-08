import matplotlib.pyplot as plt
import numpy as np
from matplotlib import image as mpimg

# Create some example data for the plots
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# Plot the first plot on the top-left subplot
axs[0, 1].plot(x, y1, color='b', label='sin(x)')
axs[0, 1].set_title('Plot on the Left')
axs[0, 1].legend()

# Plot the second plot on the bottom-right subplot
axs[1, 0].plot(x, y2, color='r', label='cos(x)')
axs[1, 0].set_title('Plot on the Bottom')
axs[1, 0].legend()

image = mpimg.imread('two_plots.png')  # Load your image
axs[0, 0].imshow(image)
axs[0, 0].set_title('Image')

# Hide the top-right and bottom-left subplots
axs[0, 0].axis('off')
axs[1, 1].axis('off')

# Adjust the spacing between subplots
plt.tight_layout()

# Save the figure to a file (e.g., PNG format)
plt.savefig('two_plots_2.png')

# Show the figure