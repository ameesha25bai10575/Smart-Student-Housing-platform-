from flask import Flask, render_template, request, redirect, jsonify
from werkzeug.utils import secure_filename
import os, razorpay
from modules.lease_analyzer import analyze_pdf
from config import Config
from database_handler import get_listings, get_listing_by_id, add_review, report_listing, add_listing

app = Flask(__name__)

# Upload
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Razorpay
client = razorpay.Client(auth=(Config.RAZORPAY_KEY_ID, Config.RAZORPAY_KEY_SECRET))

# HOME
@app.route('/')
def index():
    listings = get_listings()
    return render_template('index.html', listings=listings)

# ADD LISTING
@app.route('/add-listing', methods=['GET','POST'])
def add_listing_route():
    if request.method == 'POST':
        data = request.form.copy()
        file = request.files.get('image')

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data['image'] = filename

        add_listing(data)
        return redirect('/')

    return render_template('add_listing.html')

# DETAIL
@app.route('/listing/<int:id>')
def listing_detail(id):
    listing = get_listing_by_id(id)
    recommendations = get_listings()[:3]  # Get first 3 as recommendations

    return render_template('listing_detail.html',
                           listing=listing,
                           recommendations=recommendations)

# LEASE ANALYZER
@app.route('/analyze', methods=['GET','POST'])
def analyze():
    result = None
    if request.method == 'POST':
        file = request.files['file']
        result = analyze_pdf(file)
    return render_template('analyze.html', result=result)

# ROOMMATE
@app.route('/roommate', methods=['GET','POST'])
def roommate():
    score = None
    if request.method == 'POST':
        score = (int(request.form['budget']) +
                 int(request.form['clean']) +
                 int(request.form['sleep'])) / 3
    return render_template('roommate.html', score=score)

# REVIEWS
reviews = []

@app.route('/reviews/<int:id>', methods=['GET','POST'])
def reviews_page(id):
    if request.method == 'POST':
        add_review(request.form)
    # For now, return empty reviews since database_handler doesn't store them persistently
    return render_template('reviews.html', reviews=[])

# REPORT
@app.route('/report/<int:id>', methods=['POST'])
def report(id):
    report_listing(request.form)
    return f"Listing {id} reported!"

# PAYMENT
@app.route('/payment/<int:id>')
def payment(id):
    return render_template('payment.html', id=id)

@app.route('/create-order/<int:id>')
def create_order(id):
    order = client.order.create({
        "amount": 1000 * 100,
        "currency": "INR",
        "payment_capture": 1
    })
    return jsonify({
        "order_id": order['id'],
        "key": RAZORPAY_KEY_ID,
        "amount": 1000 * 100
    })

if __name__ == "__main__":
    app.run(debug=True)
