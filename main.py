from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField, SelectField
import csv
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, URL


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    name = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField(label='Opening Time e.g.8AM', validators=[DataRequired()])
    closing_time = StringField(label='Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating',choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"] ,validators=[DataRequired()])
    wifi = SelectField(label='Wifi Strength Rating',choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"] ,validators=[DataRequired()])
    power = SelectField(label='Power Socket Availability', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', 'a', encoding="utf-8") as file:
            file.write(f"\n{form.name.data},{form.location.data},{form.opening_time.data},{form.closing_time.data},{form.coffee_rating.data},{form.wifi.data},{form.power.data}")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    # with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
    #     csv_data = csv.reader(csv_file, delimiter=',')
    #     list_of_rows = []
    #     for row in csv_data:
    #         list_of_rows.append(row)
    file = open('cafe-data.csv', encoding="utf-8")
    reader = csv.reader(file)
    data = [line for line in reader]
    print(data)
    return render_template('cafes.html', cafes=data, length=len(data))


if __name__ == '__main__':
    app.run(debug=True)
