from flask import Blueprint, render_template, redirect, url_for, flash
from flask import request
from app import db
from app.models import Subscription
from app.forms import SubscriptionForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return redirect(url_for('main.subscriptions'))

@bp.route('/subscriptions', methods=['GET', 'POST'])
def subscriptions():
    form = SubscriptionForm()
    if form.validate_on_submit():
        sub = Subscription(
            name=form.name.data,
            cost=form.cost.data,
            renewal_date=form.renewal_date.data
        )
        db.session.add(sub)
        db.session.commit()
        flash('Subscription added.')
        return redirect(url_for('main.subscriptions'))
    subs = Subscription.query.order_by(Subscription.renewal_date).all()
    return render_template('subscriptions.html', form=form, subscriptions=subs)

@bp.route('/delete/<int:sub_id>')
def delete(sub_id):
    sub = Subscription.query.get_or_404(sub_id)
    db.session.delete(sub)
    db.session.commit()
    flash('Subscription deleted.')
    return redirect(url_for('main.subscriptions'))