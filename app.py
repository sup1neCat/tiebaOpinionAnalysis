from flask import Flask, render_template, session, g, request, redirect, url_for
from flask_migrate import Migrate
import config
from blueprints.forms import ResetForm
from exts import db
from decorators import login_required
from models import UserModel
from werkzeug.security import generate_password_hash
from blueprints.auth import bp as auth_bp
from blueprints.words import bp as words_bp
from blueprints.wordcloud import bp as wordcloud_bp
from blueprints.data import bp as data_bp
from blueprints.opinion import bp as opinion_bp
from blueprints.index import bp as index_bp

app = Flask(__name__)

# 绑定配置文件
app.config.from_object(config)

db.init_app(app)

# ORM映射数据库
migrate = Migrate(app, db)

# blueprint注册
app.register_blueprint(index_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(words_bp)
app.register_blueprint(wordcloud_bp)
app.register_blueprint(data_bp)
app.register_blueprint(opinion_bp)


# hook
@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)


@app.context_processor
def my_context_processor():
    return {"user": g.user}


@app.route("/settings", methods=['GET', 'POST'])
@login_required
def settings():
    form = ResetForm(request.form)
    if request.method == 'GET':
        return render_template('./settings.html', form=form)
    else:
        if form.validate():
            password = form.password.data
            user = UserModel.query.get(session.get("user_id"))
            user.password = generate_password_hash(password)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            return render_template('./settings.html', form=form)


if __name__ == '__main__':
    app.run()
