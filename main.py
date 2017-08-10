from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
          <label name="rot">Rotate by:</strong></label>
          <input name="rot" type='text' value="0">
          <br>
          <textarea name="original_text" placeholder="enter message here">{0}</textarea>
          <br>
          <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rotate = request.form['rot']
    text = request.form['original_text']

    rot_new = int(rotate)

    encrypted_message = rotate_string(text,rot_new)
    return form.format(encrypted_message)

@app.route("/")
def index():
    return form.format('')

app.run()
