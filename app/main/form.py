from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    about = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    pitch = TextAreaField('Write a pitch')
    submit = SubmitField('Submit')

class PitchComForm(FlaskForm):
    pitchcom = TextAreaField('comment on your pitch ')
    submit = SubmitField('Submit')
