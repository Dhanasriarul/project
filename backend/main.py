from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'oneyes'

mysql = MySQL(app)

# User login route
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({
            "success": False,
            "message": "Email and password are required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT name, email, password FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()

    if user and user[2] == password:
        return jsonify({
            "success": True,
            "message": "Login successful",
            "user": {
                "name": user[0],
                "email": user[1]
            }
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Incorrect email or password",
        }), 200

# User registration route
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    phone = data.get('phone')
    dob = data.get('dob')
    gender=data.get('gender')

    if not name or not email or not password:
        return jsonify({
            "success": False,
            "message": "Name, Email and password are required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user:
        return jsonify({
            "success": False,
            "message": "Email already exists"
        }), 200

    cursor.execute("INSERT INTO users (name, email, phone, gender, dob, password) VALUES (%s, %s, %s, %s, %s, %s)", (name, email, phone, gender, dob, password))
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "success": True,
        "message": "Registration successful"
    }), 200
    
# Visits
@app.route('/api/visits', methods=['POST'])
def visits():
    data = request.json
    page = data.get('page')

    if not page:
        return jsonify({
            "success": False,
            "message": "Page is required"
        }), 200
    
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO visits (page) VALUES (%s)", (page,))
    mysql.connection.commit()
    cursor.close()

    return jsonify(
        {
            "success": True,
            "message": "Visit logged successfully"
        }
    ), 200

# Send email route
@app.route('/api/send-email', methods=['POST'])
def send_email():
    data = request.json
    to_email = data.get('email')
    message = data.get('message')
    subjectText = data.get('subject')

    if not to_email or not message:
        return jsonify({
            "success": False,
            "message": "Email and message is required"
        }), 200

    # Create an SMTP connection
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Change to your SMTP server's port
    smtp_username = 'oneyesinfotechsolutions@gmail.com'
    smtp_password = 'hvhesvyfilvisjne'

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Compose the email
        from_email = 'Oneyes Infotech Solutions <oneyesinfotechsolutions@gmail.com>'
        subject = subjectText
        message = message

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'html'))

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())

        server.quit()

        return jsonify({
            "success": True,
            "message": "Email sent successfully"
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Failed to send email: {str(e)}"
        }), 200
    
# Admin Stats
@app.route('/api/admin-stats', methods=['GET'])
def admin_stats():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    users_count = cursor.fetchone()

    cursor.execute("SELECT COUNT(*) FROM visits WHERE page = 'home'")
    home_visits_count = cursor.fetchone()

    cursor.execute("SELECT COUNT(*) FROM visits WHERE page = 'hire-connect'")
    hire_connect_visits_count = cursor.fetchone()

    cursor.execute("SELECT COUNT(*) FROM visits WHERE page = 'e-commerce'")
    e_commerce_visits_count = cursor.fetchone()

    cursor.execute("SELECT COUNT(*) FROM visits WHERE page = 'crm'")
    crm_visits_count = cursor.fetchone()

    cursor.execute("SELECT COUNT(*) FROM visits WHERE page = 'edu-tech'")
    edu_tech_visits_count = cursor.fetchone()

    cursor.close()

    return jsonify(
        {
            "success": True,
            "visitCount": {
                "users": users_count[0],
                "home": home_visits_count[0],
                "hireConnect": hire_connect_visits_count[0],
                "eCommerce": e_commerce_visits_count[0],
                "crm": crm_visits_count[0],
                "eduTech": edu_tech_visits_count[0]
            }
        }
    ), 200

# Categories List
@app.route('/api/categories', methods=['GET'])
def categories():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    cursor.close()

    # convert array to object
    categories = [
        {
            "categoryId": category[0],
            "name": category[1],
            "image": category[2]
        }
        for category in categories
    ]

    return jsonify(
        {
            "success": True,
            "categories": categories
        }
    ), 200

# Add Category
@app.route('/api/add-category', methods=['POST'])
def add_category():
    data = request.json
    name = data.get('name')
    image = data.get('image')

    if not name or not image:
        return jsonify({
            "success": False,
            "message": "Name and image are required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO categories (name, image) VALUES (%s, %s)", (name, image))
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "success": True,
        "message": "Category added successfully"
    }), 200

# Edit Category
@app.route('/api/edit-category', methods=['POST'])
def edit_category():
    data = request.json
    category_id = data.get('categoryId')
    name = data.get('name')
    image = data.get('image')

    if not category_id or not name or not image:
        return jsonify({
            "success": False,
            "message": "Category ID, Name and image are required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE categories SET name = %s, image = %s WHERE categoryId = %s", (name, image, category_id))
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "success": True,
        "message": "Category updated successfully"
    }), 200

# Delete Category
@app.route('/api/delete-category', methods=['POST'])
def delete_category():
    data = request.json
    category_id = data.get('categoryId')

    if not category_id:
        return jsonify({
            "success": False,
            "message": "Category ID is required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM categories WHERE categoryId = %s", (category_id,))
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "success": True,
        "message": "Category deleted successfully"
    }), 200

# Service Listing route with filters
@app.route('/api/services', methods=['GET'])
def get_services():
    category_id = request.args.get('categoryId')
    keyword = request.args.get('keyword')
    city = request.args.get('city')
    sort_by_impressions = request.args.get('sort')  # 'asc' or 'desc'
    rating = request.args.get('rating')  # 1, 2, 3, 4 or 5

    # Build the base query
    if rating:
        query = "SELECT *, (SELECT COUNT(*) FROM reviews WHERE serviceId = services.serviceId) AS reviewsCount, (SELECT FLOOR(AVG(rating)) FROM reviews WHERE serviceId = services.serviceId) AS avgRating FROM services WHERE categoryId = %s AND (SELECT FLOOR(AVG(rating)) FROM reviews WHERE serviceId = services.serviceId) >= %s"
        params = [category_id, rating]
    else:
        query = "SELECT *, (SELECT COUNT(*) FROM reviews WHERE serviceId = services.serviceId) AS reviewsCount, (SELECT FLOOR(AVG(rating)) FROM reviews WHERE serviceId = services.serviceId) AS avgRating FROM services WHERE categoryId = %s"
        params = [category_id]

    # Add filters to the query and parameters
    if keyword:
        query += " AND title LIKE %s"
        params.append(f"%{keyword}%")
    if city:
        query += " AND city = %s"
        params.append(city)

    # Execute the query and apply sorting if requested
    cursor = mysql.connection.cursor()
    if sort_by_impressions == 'asc':
        query += " ORDER BY impressions ASC"
    elif sort_by_impressions == 'desc':
        query += " ORDER BY impressions DESC"

    cursor.execute(query, tuple(params))
    services = cursor.fetchall()
    cursor.close()

    # Convert results to a list of dictionaries
    services_list = [
        {
            "serviceId": service[0],
            "categoryId": service[1],
            "image": service[2],
            "title": service[3],
            "impressions": service[4],
            "address": service[5],
            "city": service[6],
            "phone": service[7],
            "email": service[8],
            "reviewsCount": service[9],
            "rating": service[10],
        }
        for service in services
    ]

    return jsonify({
        "success": True,
        "services": services_list
    }), 200

# Add impression route
@app.route('/api/add-impression', methods=['POST'])
def add_impression():
    data = request.json
    service_id = data.get('serviceId')

    if not service_id:
        return jsonify({
            "success": False,
            "message": "Service ID is required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE services SET impressions = impressions + 1 WHERE serviceId = %s", (service_id,))
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "success": True,
        "message": "Impression added successfully"
    }), 200

# Add enquiry route(save to database and send email)
@app.route('/api/add-enquiry', methods=['POST'])
def add_enquiry():
    data = request.json
    service_id = data.get('serviceId')
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    message = data.get('message')
    messageTemplate = data.get('messageTemplate')
    to_email = data.get('toEmail')

    if not service_id or not name or not email or not phone or not message:
        return jsonify({
            "success": False,
            "message": "Service ID, Name, Email, Phone and Message are required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO enquiries (serviceId, name, email, phone, message) VALUES (%s, %s, %s, %s, %s)", (service_id, name, email, phone, message))
    mysql.connection.commit()
    cursor.close()

    # Create an SMTP connection
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Change to your SMTP server's port
    smtp_username = 'oneyesinfotechsolutions@gmail.com'
    smtp_password = 'hvhesvyfilvisjne'

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Compose the email
        from_email = 'Oneyes Infotech Solutions <oneyesinfotechsolutions@gmail.com>'
        subject = 'New Enquiry'
        message = messageTemplate

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'html'))

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())

        server.quit()

        return jsonify({
            "success": True,
            "message": "Enquiry sent successfully"
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Failed to send email: {str(e)}"
        }), 200

# Enquiries List based on serviceId
@app.route('/api/enquiries', methods=['GET'])
def enquiries():
    service_id = request.args.get('serviceId')

    if not service_id:
        return jsonify({
            "success": False,
            "message": "Service ID is required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM enquiries WHERE serviceId = %s", (service_id,))
    enquiries = cursor.fetchall()
    cursor.close()

    # Convert results to a list of dictionaries
    enquiries_list = [
        {
            "enquiryId": enquiry[0],
            "serviceId": enquiry[1],
            "name": enquiry[2],
            "email": enquiry[3],
            "phone": enquiry[4],
            "message": enquiry[5],
        }
        for enquiry in enquiries
    ]

    return jsonify({
        "success": True,
        "enquiries": enquiries_list
    }), 200
    
# Service Details route
@app.route('/api/service', methods=['GET'])
def service_details():
    service_id = request.args.get('serviceId')

    if not service_id:
        return jsonify({
            "success": False,
            "message": "Service ID is required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT *, (SELECT COUNT(*) FROM reviews WHERE serviceId = services.serviceId) AS reviewsCount, (SELECT FLOOR(AVG(rating)) FROM reviews WHERE serviceId = services.serviceId) AS avgRating FROM services WHERE serviceId = %s", (service_id,))
    service = cursor.fetchone()

    if not service:
        return jsonify({
            "success": False,
            "message": "Service not found"
        }), 200

    cursor.execute("SELECT * FROM reviews WHERE serviceId = %s", (service_id,))
    reviews = cursor.fetchall()
    cursor.close()

    # Convert results to a list of dictionaries
    reviews_list = [
        {
            "reviewId": review[0],
            "serviceId": review[1],
            "name": review[2],
            "rating": review[3],
            "message": review[4],
        }
        for review in reviews
    ]

    # No of 5 stars
    five_stars = 0
    for review in reviews_list:
        if review['rating'] == 5:
            five_stars += 1

    # No of 4 stars
    four_stars = 0
    for review in reviews_list:
        if review['rating'] == 4:
            four_stars += 1
    
    # No of 3 stars
    three_stars = 0
    for review in reviews_list:
        if review['rating'] == 3:
            three_stars += 1

    # No of 2 stars
    two_stars = 0
    for review in reviews_list:
        if review['rating'] == 2:
            two_stars += 1

    # No of 1 stars
    one_stars = 0
    for review in reviews_list:
        if review['rating'] == 1:
            one_stars += 1

    if int(service[9]) != 0:
        five_star_percentage = round((int(five_stars) / int(service[9])) * 100)
        four_star_percentage = round((int(four_stars) / int(service[9])) * 100)
        three_star_percentage = round((int(three_stars) / int(service[9])) * 100)
        two_star_percentage = round((int(two_stars) / int(service[9])) * 100)
        one_star_percentage = round((int(one_stars) / int(service[9])) * 100)
    else:
        five_star_percentage = 0
        four_star_percentage = 0
        three_star_percentage = 0
        two_star_percentage = 0
        one_star_percentage = 0

    return jsonify({
        "success": True,
        "service": {
            "serviceId": service[0],
            "categoryId": service[1],
            "image": service[2],
            "title": service[3],
            "impressions": service[4],
            "address": service[5],
            "city": service[6],
            "phone": service[7],
            "email": service[8],
            "reviewsCount": service[9],
            "rating": service[10],
            "reviews": reviews_list,
            "stars": {                
                "fiveStars": five_star_percentage,
                "fourStars": four_star_percentage,
                "threeStars": three_star_percentage,
                "twoStars": two_star_percentage,
                "oneStars": one_star_percentage
            }
        }
    }), 200

# Add service route
@app.route('/api/add-service', methods=['POST'])
def add_service():
    data = request.json
    category_id = data.get('categoryId')
    image = data.get('image')
    title = data.get('title')
    address = data.get('address')
    city = data.get('city')
    phone = data.get('phone')
    email = data.get('email')

    if not category_id or not image or not title or not address or not city or not phone or not email:
        return jsonify({
            "success": False,
            "message": "Category ID, Image, Title, Address, City, Phone and Email are required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO services (categoryId, image, title, address, city, phone, email) VALUES (%s, %s, %s, %s, %s, %s, %s)", (category_id, image, title, address, city, phone, email))
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "success": True,
        "message": "Service added successfully"
    }), 200

# Edit service route
@app.route('/api/edit-service', methods=['POST'])
def edit_service():
    data = request.json
    service_id = data.get('serviceId')
    category_id = data.get('categoryId')
    image = data.get('image')
    title = data.get('title')
    address = data.get('address')
    city = data.get('city')
    phone = data.get('phone')
    email = data.get('email')

    if not service_id or not category_id or not image or not title or not address or not city or not phone or not email:
        return jsonify({
            "success": False,
            "message": "Service ID, Category ID, Image, Title, Address, City, Phone and Email are required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE services SET categoryId = %s, image = %s, title = %s, address = %s, city = %s, phone = %s, email = %s WHERE serviceId = %s", (category_id, image, title, address, city, phone, email, service_id))
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "success": True,
        "message": "Service updated successfully"
    }), 200

# Delete service route

@app.route('/api/delete-service', methods=['POST'])
def delete_service():
    data = request.json
    service_id = data.get('serviceId')

    if not service_id:
        return jsonify({
            "success": False,
            "message": "Service ID is required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM services WHERE serviceId = %s", (service_id,))
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "success": True,
        "message": "Service deleted successfully"
    }), 200

# GET images of service route
@app.route('/api/get-images', methods=['GET'])
def get_images():
    service_id = request.args.get('serviceId')

    if not service_id:
        return jsonify({
            "success": False,
            "message": "Service ID is required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM gallery WHERE serviceId = %s", (service_id,))
    images = cursor.fetchall()
    cursor.close()

    # Convert results to a list of dictionaries
    images_list = [
        {
            "galleryId": image[0],
            "serviceId": image[1],
            "image": image[2],
        }
        for image in images
    ]

    return jsonify({
        "success": True,
        "images": images_list
    }), 200

# Delete image route
@app.route('/api/delete-image', methods=['POST'])
def delete_image():
    data = request.json
    gallery_id = data.get('galleryId')

    if not gallery_id:
        return jsonify({
            "success": False,
            "message": "Gallery ID is required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM gallery WHERE galleryId = %s", (gallery_id,))
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "success": True,
        "message": "Image deleted successfully"
    }), 200

# Add image route
@app.route('/api/add-image', methods=['POST'])
def add_image():
    data = request.json
    service_id = data.get('serviceId')
    image = data.get('image')

    if not service_id or not image:
        return jsonify({
            "success": False,
            "message": "Service ID and Image are required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO gallery (serviceId, image) VALUES (%s, %s)", (service_id, image))
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "success": True,
        "message": "Image added successfully"
    }), 200

# Add review route
@app.route('/api/add-review', methods=['POST'])
def add_review():
    data = request.json
    service_id = data.get('serviceId')
    name = data.get('name')
    rating = data.get('rating')
    message = data.get('message')

    if not service_id or not name or not rating or not message:
        return jsonify({
            "success": False,
            "message": "Service ID, Name, Rating and Message are required"
        }), 200

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO reviews (serviceId, name, rating, message) VALUES (%s, %s, %s, %s)", (service_id, name, rating, message))
    mysql.connection.commit()
    cursor.close()

    return jsonify({
        "success": True,
        "message": "Review added successfully"
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
