from flask import (
    Blueprint,
    render_template,
    flash,
    session,
    redirect,
    url_for
)

from flask.ext.login import (
    login_user,
    logout_user,
    login_required,
    current_app
)

from application.services import is_allowed_to_see_title

from .models import User
from .forms import LoginForm

auth = Blueprint('auth', __name__, template_folder='templates' , url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data)
        if user and is_allowed_to_see_title(user, form.password.data):
            login_user(user)
            return redirect(form.next.data or url_for('index'))
        else:
            current_app.logger.info("Login failed for user email %s" % form.email.data)
            flash("Sorry, those details haven&rsquo;t been recognised. Please try again.")
    return render_template("auth/login_user.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    session.pop("lrid", None)
    session.pop("roles", None)
    logout_user()
    return redirect(url_for('auth.login'))
