import matplotlib.pyplot as plt
import control

## Matlab

# num = 1;
# den = [1 10 0];
# g = tf(num, den)

# rlocus(g);
# hold on

# num = [1 0.9];
# den = [1 4.5];
# gc = tf(num, den);
# rlocus(g*gc);


## Python
def example():
    num = 1
    den = [1, 10, 0]
    g = control.tf(num, den)

    plt.figure()
    control.root_locus(g)

    num = [1, 0.9]
    den = [1, 4.5]
    gc = control.tf(num, den)

    plt.figure()
    control.root_locus(g * gc)

    plt.show()