from crypt import methods
from flask import render_template, request, redirect, abort, url_for
from . import main
from ..models import User, Comment, Post, Subscribers
from flask_login import login_required, current_user
from .forms import UpdateProfile, PostForm, CommentForm, UpdatePostForm
from datetime import datetime
from .. import db
from ..requests import get_quote
from ..email import welcome_message, notification_message

#bleach a html sanitazing library that escapes/stripes text(markup/attribute) frm untrusted sources
import bleach

@main.route("/", methods = ["GET","POST"])
def index():
    posts = Post.get_all_posts()
    quote = get_quote()

    if request.method == "POST":
        new_sub = Subscribers(email=request.form.get("subscriber"))
        db.session.add(new_sub)
        db.session.commit()
        welcome_message("Thanks for subscribing to Nazz blog","email/welcome",new_sub.email)
    return render_template("idex.html",posts=posts, quote=quote)

@main.route("/post/<int:id>", methods = ["GET","POST"]) 
def post(id):
    post = Post.query.filter_by(id=id).first()
    comments = Comment.query.filter_by(post_id=id).all()
    comment_form = CommentForm
    comment_count = len(comments)

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment_form.comment.data = ""
        comment_alias = comment_form.alias.data
        comment_form.alias.data = ""
        if current_user.is_authenticated:
            comment_alias = current_user.username
        new_comment = Comment(comment = comment,  
                            comment_at = datetime.now(),
                            comment_by = comment_alias,
                            post_id = id) 
        new_comment.save_comment()
        return redirect(url_for("main.post",id=post.id))
        
    return render_template("post.html",
                            post = post,
                            comments = comments,
                            comment_form = comment_form,
                            comment_count = comment_count)                          



