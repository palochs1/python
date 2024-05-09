from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        "id": 1,
        "frameworks": "Django",
        "year": 2005
    },
    {
        "id": 2,
        "frameworks": "Flask",
        "year": 2010
    },
    {
        "id": 3,
        "frameworks": "Web2Py",
        "year": 2007
    }
]

@app.route('/')
def home():
    return "Hello World"

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data), 200

@app.route('/api/<int:fw_id>', methods=['POST'])
def get_fw(fw_id):
    """
    This endpoint returns a specific framework by ID.
    """
    fw = [fw for fw in data if fw['id'] == fw_id]
    if len(fw) == 0:
        return jsonify({'error': 'Framework not found'}), 404
    return jsonify(fw[0]), 200

@app.route('/api/post', methods=['POST'])
def post_data():
    """
    This endpoint receives form data via POST request and prints it out.
    """
    # Access form data
    form_data = request.form
    # Print form data
    print("Form Data:")
    print(form_data)
    # Return a response
    return 'Form data received successfully.', 200

@app.route('/api/header', methods=['POST'])
def post_header():
    """
    This endpoint receives form data via POST request and prints the headers.
    """
    # Access request headers
    headers = request.headers
    # Print headers
    print("Request Headers:")
    for header in headers:
        # Check if the header exists in the request
        if header in request.headers:
            print(header, ":", headers[header])
        else:
            print(header, ":", "Not Found")
    # Return a response
    return 'Headers received and printed successfully.', 200


if __name__ == "__main__":
    app.run(debug=True)
