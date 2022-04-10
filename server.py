from flask import Flask, render_template
app = Flask(__name__)

# return an 8 by 8 board with default coloring
@app.route('/')
def index():
    return render_template("index.html", x_coord=8, y_coord=8)

# display a 8 by 'num' board with default coloring
@app.route('/<int:num>')
def indexY(num):
    return render_template("index.html", x_coord=8, y_coord=int(num))

# dispay a 'numX' by 'numY' baord with default coloring
@app.route('/<int:numX>/<int:numY>')
def indexXY(numX, numY):
    return render_template("index.html", x_coord=int(numX), y_coord=int(numY))

# SENSI BONUS: display a checkerboard with 4 paraments, x, y, abd square colors
# dispay a 'numX' by 'numY' baord with default coloring
@app.route('/<int:numX>/<int:numY>/<string:square1>/<string:square2>')
def indexXYColors(numX, numY, square1, square2):
    return render_template("index.html", x_coord=int(numX), y_coord=int(numY), square1=square1, square2=square2)

if __name__=="__main__":
    app.run(debug=True)

