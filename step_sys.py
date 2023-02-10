import matplotlib.pyplot as plt
import control


def example():
    num = 1
    den = [1, 2]
    sys = control.tf(num, den)

    t, y = control.step_response(sys)

    plt.figure()
    plt.plot(t, y)
    plt.grid()
    plt.show()