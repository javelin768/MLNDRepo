{"filter":false,"title":"SciPyTest.py","tooltip":"/mlndhelloword/SciPyTest.py","undoManager":{"mark":13,"position":13,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["\"\"\"","====================================","Plotting Cross-Validated Predictions","====================================","","This example shows how to use `cross_val_predict` to visualize prediction","errors.","","\"\"\"","from sklearn import datasets","from sklearn.model_selection import cross_val_predict","from sklearn import linear_model","import matplotlib.pyplot as plt","","lr = linear_model.LinearRegression()","boston = datasets.load_boston()","y = boston.target","","# cross_val_predict returns an array of the same size as `y` where each entry","# is a prediction obtained by cross validation:","predicted = cross_val_predict(lr, boston.data, y, cv=10)","","fig, ax = plt.subplots()","ax.scatter(y, predicted, edgecolors=(0, 0, 0))","ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)","ax.set_xlabel('Measured')","ax.set_ylabel('Predicted')","plt.show()",""],"id":1}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":1},"action":"insert","lines":["p"],"id":2}],[{"start":{"row":28,"column":1},"end":{"row":28,"column":2},"action":"insert","lines":["r"],"id":3}],[{"start":{"row":28,"column":2},"end":{"row":28,"column":3},"action":"insert","lines":["i"],"id":4}],[{"start":{"row":28,"column":3},"end":{"row":28,"column":4},"action":"insert","lines":["n"],"id":5}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":5},"action":"insert","lines":["t"],"id":6}],[{"start":{"row":28,"column":5},"end":{"row":28,"column":7},"action":"insert","lines":["()"],"id":7}],[{"start":{"row":28,"column":6},"end":{"row":28,"column":8},"action":"insert","lines":["\"\""],"id":8}],[{"start":{"row":28,"column":7},"end":{"row":28,"column":8},"action":"insert","lines":["T"],"id":9}],[{"start":{"row":28,"column":8},"end":{"row":28,"column":9},"action":"insert","lines":["e"],"id":10}],[{"start":{"row":28,"column":9},"end":{"row":28,"column":10},"action":"insert","lines":["s"],"id":11}],[{"start":{"row":28,"column":10},"end":{"row":28,"column":11},"action":"insert","lines":["t"],"id":12}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":13},"action":"insert","lines":["print(\"Test\")"],"id":13}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"insert","lines":["2"],"id":14}]]},"ace":{"folds":[],"scrolltop":126.5,"scrollleft":0,"selection":{"start":{"row":21,"column":12},"end":{"row":21,"column":12},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":6,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1515820820237,"hash":"f8478a377d92ff11a62e9772a69117428f334e90"}