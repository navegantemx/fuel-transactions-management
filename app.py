import os
from flask import Flask, render_template, redirect, request, url_for
import flask_pymongo
from bson.objectid import ObjectId
from os import path
from utils.db_utils import handle_mongo_errors, find_object
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'fuel_management'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config["FLASK_DEBUG"] = True
app.config["SECRET_KEY"] = b'_5#y2L"F4Q8z\n\xec]/'

mongo = flask_pymongo.PyMongo(app)


@app.route('/')
@app.route('/get_receipts')
def get_receipts():
    """
    Display all the receipts for the user
    """
    return render_template('receipts.html', receipts=mongo.db.receipts.find())


@app.route('/add_receipt')
def add_receipt():
    return render_template('addreceipt.html',
                           sites=mongo.db.sites.find())


@app.route('/insert_receipt', methods=['POST'])
def insert_receipt():
    receipts = mongo.db.receipts.find()
    receipt = request.form.to_dict()
    vehicle = mongo.db.vehicles.find_one({"vehicle_id": receipt['vehicle_id']})
    if vehicle:
        mongo.db.receipts.insert_one(receipt)
        return redirect(url_for('get_receipts'))

    else:
        return('vehicle does not exist')


@app.route('/edit_receipt/<receipt_id>')
def edit_receipt(receipt_id):
    the_receipt, error = handle_mongo_errors(
        find_object, mongo.db['receipts'], receipt_id)
    if error:
        return redirect(url_for('get_receipts'))
    all_sites = mongo.db.sites.find()
    return render_template('editreceipt.html', receipt=the_receipt,
                           sites=all_sites)


@app.route('/update_receipt/<receipt_id>', methods=["POST"])
def update_receipt(receipt_id):
    receipts = mongo.db.receipts
    receipts.update({'_id': ObjectId(receipt_id)},
                    {
        'pump_number': request.form.get('pump_number'),
        'vehicle_id': request.form.get('vehicle_id'),
        'employee_id': request.form.get('employee_id'),
        'site_name': request.form.get('site_name'),
        'quantity': request.form.get('quantity'),
        'issue_date': request.form.get('issue_date'),
    })
    return redirect(url_for('get_receipts'))


@app.route('/delete_receipt/<receipt_id>')
def delete_receipt(receipt_id):
    mongo.db.receipts.remove({'_id': ObjectId(receipt_id)})
    return redirect(url_for('get_receipts'))


@app.route('/get_sites')
def get_sites():
    return render_template('sites.html',
                           sites=mongo.db.sites.find())


@app.route('/delete_site/<site_id>')
def delete_site(site_id):
    mongo.db.sites.remove({'_id': ObjectId(site_id)})
    return redirect(url_for('get_sites'))


@app.route('/edit_site/<site_id>')
def edit_site(site_id):
    return render_template('editsite.html',
                           site=mongo.db.sites.find_one({'_id': ObjectId(site_id)}))


@app.route('/update_site/<site_id>', methods=['POST'])
def update_site(site_id):
    mongo.db.sites.update(
        {'_id': ObjectId(site_id)},
        {'site_name': request.form.get('site_name')})
    return redirect(url_for('get_sites'))


@app.route('/insert_site', methods=['POST'])
def insert_site():
    site_doc = {'site_name': request.form.get('site_name')}
    mongo.db.sites.insert_one(site_doc)
    return redirect(url_for('get_sites'))


@app.route('/add_site')
def add_site():
    return render_template('addsite.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
