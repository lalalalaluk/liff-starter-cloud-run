from flask import Flask,render_template,send_from_directory

app = Flask(__name__, static_url_path='',
                  static_folder='dist',
                  template_folder='dist')
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(use_reloader=True,host='0.0.0.0',port='8080',debug=True)