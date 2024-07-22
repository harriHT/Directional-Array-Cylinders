# Geometric model for cylindrical detectors in 2x1 array
# (C) Harri Toivonen, HT Nuclear Oy, 28 May 2024
# Documentation: Array of two spectrometers for source directional estimation, HT 28 May 2024

def parameterPlotting(r, w, h):
    import matplotlib.pyplot as plt
    from matplotlib.figure import Figure
    import numpy as np

    def cylindricalModel(r, w, h, theta):
        y_theoretical = ((r + w) * np.cos(theta) - h * np.sin(theta)) / ( r * np.cos(theta) + r * np.sin(theta))
        for i in range(len(y_theoretical)):
            if y_theoretical[i] > 1:
                y_theoretical[i] = 1
            if y_theoretical[i] < 0:
                y_theoretical[i] = 0
        return y_theoretical

    figureText = '2x1 Array of Cylindrical Detectors with a Shield between the Detectors\n'
    x = np.arange(0, 91)
    theta = x * np.pi / 180

    plt.clf()  # Clear the current figure

    figDirection = plt.figure(num='Cylindrical geometry', figsize=[11, 9])
    figureText = 'r = radius; w = gap between the detectors; h = collimator'
    figDirection.suptitle(figureText + '\nGeometric model: R = [(r + w) * cos(theta) - h * sin(theta)] / [r * cos(theta) + r * sin(theta)]')
    ax1 = plt.subplot(1, 1, 1)

    y_ideal = cylindricalModel(r, 0, 0, theta)
    ax1.plot(-x, y_ideal, 'r-', linewidth=2, label='Ideal case (w=0; h=0)')
    ax1.plot(x, y_ideal, 'r-', linewidth=2)

    y_theoretical = cylindricalModel(r, w, h, theta)
    ax1.plot(-x, y_theoretical, 'c-', linewidth=2, label='Geometric model (r, w, h)')
    ax1.plot(x, y_theoretical, 'c-', linewidth=2)

    ax1.set_xlabel('Angle \u03b8, deg', fontsize=14)
    ax1.set_ylabel('Ratio of voxel counts (back/front)', fontsize=14)
    ax1.set_xticks([-90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90])
    ax1.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    ax1.grid(alpha=0.6)
    ax1.legend(loc='upper right')

    return figDirection  # Return the figure object

if __name__ == '__main__':
    # Cylindrical model parameters
    r = 3.8
    w = 1.2 
    h = 1.2

    parameterPlotting(r, w, h)
