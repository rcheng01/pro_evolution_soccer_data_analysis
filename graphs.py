from matplotlib import pyplot as plt

elos = [1795.4089539627068, 1831.6225821557923, 1875.391301715983, 1884.895006213042, 1902.2361016414432, 1958.9946461365098, 1983.1331850181973, 2014.9944870821257, 2056.4541135306056, 2089.618575338345, 2089.618575338345, 2089.618575338345, 2089.618575338345, 2089.618575338345, 2100.1722754602463, 2109.6603405605758, 2111.9775374444698, 2112.9766934825445, 2113.518639786799, 2121.1687988938108, 2121.1687988938108, 2121.1687988938108, 2121.1687988938108, 2121.1687988938108, 2121.1687988938108, 2121.1687988938108, 2121.2786383308417, 2121.2786383308417, 2121.2786383308417, 2121.8759233492524]

XVALUES = list(range(30))
YVALUES = elos
plt.plot(XVALUES, YVALUES)


plt.xlabel("number of player swaps")
plt.ylabel("elo")
plt.title("Algorithmic Improvement of Team via Hill Climbing")
plt.show()