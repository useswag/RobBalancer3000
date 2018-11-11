from flask import (
    Flask,
    render_template,
    request
)
from balancer import Balancer
import rob
import numpy as np

# Create the application instance
app = Flask(__name__, template_folder="templates")
b = Balancer()
# Create a URL route in our application for "/"
@app.route('/balance/<num1>/<num2>/<num3>/<num4>/<num5>/<num6>/<num7>/<num8>/<num9>/<num10>')
def balance(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10):
    print(request)
    input_nums = np.array([num1,num2,num3,num4,num5,num6,num7,num8,num9,num10])
    print(b.total(input_nums))
    return str(b.total(input_nums))

@app.route('/rob/<ask>')
def rob_route(ask):
    return str(rob.rob_reply(ask))

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)