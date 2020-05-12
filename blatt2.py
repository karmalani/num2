# Daniel Banov, Sarah Müller
# Blatt 2
# nimm Rechtschreibfehler bitte nicht übel, es ist 05:20
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Variablen für den Plot
fig = plt.figure()
ax = plt.axes()


# Die Funktion, die den Plot erstellt
def animate(s):
    # bestimmung des richtigen s
    s = np.linspace(0, 1, 21)[s]
    # definition von A
    A = np.array([[1, -2 * s, 3 * s], [0, 6, s], [3 * s, 0, 9 + 10 * 1j]])
    # plot erstellen
    ax.clear()
    plot_eig_and_gerschgorin(A)
    plt.xlim([-5, 13])
    plt.ylim([-6, 14])
    ax.legend(loc='upper left')


def plot_complex(numbers, form, label=None):
    # Funktion, die komplexe zahlen erhällt und diese plottet
    x = [x.real for x in numbers]
    y = [y.imag for y in numbers]
    if label is None:
        ax.plot(x, y, form)
    ax.plot(x, y, form, label=label)


def plot_circle(mid, radius):
    # funtion, die einen Kreis mit gegebenem Radius und Mittelpunkt plottet
    x = [mid + radius]
    for i in np.linspace(0, 2 * np.pi):
        x.append(mid + radius * (np.cos(i) + np.sin(i) * 1j))
    return plot_complex(x, "-")


def plot_eig_and_gerschgorin(matrix):
    # funktion, die alle Mittelpunkte, Eigenwerte und Gerschgorinkreise plottet

    # bestimme die Eigenwerte und plotte sie
    values, _ = np.linalg.eig(matrix)
    plot_complex(values, "x", "Eigenvalues")

    # plotte die Eigenwerte
    plot_complex(np.diag(matrix), "x", "Center")

    # berechne die Radien und plotte die Kreise
    for i in range(matrix.shape[0]):
        radius = 0
        for j in range(matrix.shape[0]):
            if i != j:
                radius += np.abs(matrix[i][j])
        plot_circle(matrix[i][i], radius)


# die Animation wird erstellt und gezeigt
anim = animation.FuncAnimation(fig, animate, frames=21, blit=False)
plt.show()
