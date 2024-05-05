from flask import Flask, jsonify
from g4f.gui import run_gui

app = Flask(__name__)

@app.route('/run-gui', methods=['POST'])
def run_gui_endpoint():
    try:
        run_gui()  # Execute the run_gui function
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
