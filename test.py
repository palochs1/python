from flask import Flask, request

app = Flask(__name__)

@app.route('/api/post', methods=['POST'])
def receive_form_data():
    # รับ form data จาก request
    form_data = request.form

    # พิมพ์ค่า key และ value ที่ได้รับจาก form data
    for key, value in form_data.items():
        print(f'{key}: {value}')

    return 'Received form data', 200

if __name__ == '__main__':
    app.run(debug=True, port=523)