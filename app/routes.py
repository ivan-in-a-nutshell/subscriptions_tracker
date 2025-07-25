from flask import Blueprint, render_template, redirect, url_for, flash
from flask import request
from app import db
from app.models import Subscription
from app.forms import SubscriptionForm, EmailForm
from sqlalchemy import func
import app.remind as remind
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
    
    email_form = EmailForm()
    subscriber = None
    if email_form.validate_on_submit():
        subscriber = email_form.email.data
        flash('Email updated.')
        return redirect(url_for('main.subscriptions'))

    subs = Subscription.query.order_by(Subscription.renewal_date).all()
    total_cost = db.session.query(func.sum(Subscription.cost)).scalar() or 0
    remind.send_daily_reminders(subscriber)
    return render_template('subscriptions.html', form=form, subscriptions=subs, total_cost=total_cost, email_form=email_form)

@bp.route('/delete/<int:sub_id>')
def delete(sub_id):
    sub = Subscription.query.get_or_404(sub_id)
    db.session.delete(sub)
    db.session.commit()
    flash('Subscription deleted.')
    return redirect(url_for('main.subscriptions'))