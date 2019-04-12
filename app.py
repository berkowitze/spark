from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """ homepage """
    return render_template('index.html')


@app.route('/formfilled', methods=['POST'])
def form():
    """ form filled out """
    return render_template('formfilled.html', form=request.form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(405)
def get_req_form(e):
    return render_template('405.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
