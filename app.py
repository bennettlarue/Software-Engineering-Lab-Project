from flask import Flask, render_template, jsonify, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = StringField('Password', [validators.DataRequired()])
    login = SubmitField('Login') 


class AddDataEntryForm(FlaskForm):
    add_column_index = IntegerField('Column Index', [validators.DataRequired(), validators.NumberRange(min=0)])
    add_value = StringField('Data Value', [validators.DataRequired()])


class RemoveDataEntryForm(FlaskForm):
    remove_column_index = IntegerField('Column Index', [validators.DataRequired(), validators.NumberRange(min=0)])
    remove_row_index = IntegerField('Row Index', [validators.DataRequired(), validators.NumberRange(min=0)])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm() 
    if form.validate_on_submit():
        pass
    return render_template('index.html', form=form)


@app.route('/api/login', methods=['POST'])
def api_login():
    form = LoginForm(data=request.json)
    if form.validate():
        username = form.username.data
        password = form.password.data
        return jsonify(message=f"Stub response: Logged in with username: '{username}' and password: '{password}'"), 200
    # Return errors if validation fails
    return jsonify(errors=form.errors), 400


@app.route('/api/add_data_entry', methods=['POST'])
def api_add_data_entry():
    form = AddDataEntryForm(data=request.json)
    if form.validate():
        add_column_index = form.add_column_index.data
        add_value = form.add_value.data
        return jsonify(message=f"Stub response: Added value '{add_value}' to column '{add_column_index}'"), 200
    # Return errors if validation fails
    return jsonify(errors=form.errors), 400


@app.route('/api/remove_data_entry', methods=['POST'])
def api_remove_data_entry():
    form = RemoveDataEntryForm(data=request.json)
    if form.validate():
        remove_column_index = form.remove_column_index.data
        remove_row_index = form.remove_row_index.data
        return jsonify(message=f"Stub response: Removed value at row '{remove_row_index}' and column '{remove_column_index}'"), 200
    # Return errors if validation fails
    return jsonify(errors=form.errors), 400


@app.route('/api/generate_bar_graph', methods=['POST'])
def api_generate_bar_graph():
    return jsonify(message=f"Stub response: received a bar graph."), 200


@app.route('/api/generate_line_graph', methods=['POST'])
def api_generate_line_graph():
    return jsonify(message=f"Stub response: received a line graph."), 200


@app.route('/api/generate_scatter_plot', methods=['POST'])
def api_generate_scatter_plot():
    return jsonify(message=f"Stub response: received a scatter plot."), 200


@app.route('/api/generate_data_analysis', methods=['POST'])
def api_generate_data_analysis():
    return jsonify(message=f"Stub response: received a data analysis."), 200


if __name__ == "__main__":
    app.run(debug=True)
