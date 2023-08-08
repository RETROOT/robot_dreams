from flask import Flask, render_template, jsonify
import logging

app = Flask(__name__)


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@app.route('/hello', methods=['GET'])
def hello_world():
    logger.info('Handling /hello endpoint')
    return 'Hello, world!'


@app.route('/html', methods=['GET'])
def return_html():
    logger.info('Handling /html endpoint')
    return render_template('index.html')


@app.route('/json', methods=['GET'])
def return_json():
    logger.info('Handling /json endpoint')
    data = {'message': 'Hello, world!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

