from flask_wtf import FlaskForm
from sqlalchemy import alias
from wtforms import SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired

class PostForm(FlaskForm):
    title = StringField("Blog Title:", validators=[InputRequired()])
    post = TextAreaField("Type here:",validators=[InputRequired()])
    submit = SubmitField("Post")

class UpdatePostForm(FlaskForm):
    title = StringField("Blog Title:", validators=[InputRequired()]) 
    post = TextAreaField("Type here:", validators=[InputRequired()])
    submit = SubmitField("Update") 

class CommentForm(FlaskForm):
    comment = TextAreaField("Write comment:", validators=[InputRequired()])
    # alias is alternative name for a field providing a more user-friendly description of the
    # content. Unlike true names,aliases do not have to adhere to the limitations of the
    # database and can contain up to 255 characters, including spaces, numbers, 
    # and special characters
    alias =  StringField("Comment alias")
    submit = SubmitField("Comment")

class UpdateProfile(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    bio = TextAreaField("Bio")
    email = StringField("Email/Optional")
    submit = SubmitField("Update")      

