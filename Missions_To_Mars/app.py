from flask import Flask, render_template, redirect
from flask_pymongo import pymongo,PyMongo
import scrape_mars

app = Flask(__name__)

# setup mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", vacation=destination_data)

@app.route("/scrape")
def scrape():
    
    # Run the scrape function
    mars_dict = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_dict, upsert=True)

    # Redirect back to home page
    return redirect("/")

#if __name__ == "__main__":
   # app.run(debug=True)

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape())