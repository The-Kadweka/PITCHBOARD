from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class AddPitchForm(FlaskForm):
    title = StringField("Pitch Title", validators = [Required()])
    pitch = TextAreaField("Go", validators = [Required()])
    category = SelectField(
        "category",
        choices=[("highlights", "highlights"),("gossip","gossip"),("funny","funny"),("promotion","promotion"),("product","product"),("cheesy","cheesy"),("random","random")],validators = [Required()]
    )
    submit = SubmitField("Add pitch")

class AddComment(FlaskForm):
    content = TextAreaField("Add comment")
    submit = SubmitField("Add")