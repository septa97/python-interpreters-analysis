import matplotlib.pyplot as plt
import numpy as np

from subprocess import call

def cpu_bound_test():
    # CPython
    print "CPython interpreter running..."
    cpython_log = open("CPython.txt", "w")
    call(["python", "cpu-bound-test.py"], stdout=cpython_log)

    # Jython
    print "Jython interpreter running..."
    jython_log = open("Jython.txt", "w")
    call(["jython", "cpu-bound-test.py"], stdout=jython_log)

    # PyPy
    print "PyPy interpreter running..."
    pypy_log = open("PyPy.txt", "w")
    call(["pypy", "cpu-bound-test.py"], stdout=pypy_log)

if __name__ == "__main__":
    # CPU bound test
    cpu_bound_test()
    cpython_result = np.loadtxt("CPython.txt")
    jython_result = np.loadtxt("Jython.txt")
    pypy_result = np.loadtxt("PyPy.txt")

    plt.plot(cpython_result[:, 0], cpython_result[:, 1])
    plt.plot(jython_result[:, 0], jython_result[:, 1])
    plt.plot(pypy_result[:, 0], pypy_result[:, 1])

    plt.title('CPU bound test')
    plt.legend(["CPython", "Jython", "PyPY"], loc="upper left")
    plt.show()

