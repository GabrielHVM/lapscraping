"""Module with main code"""
from app.classes.web_scraper import WebScraper
from flask import Flask, jsonify, request

app = Flask(__name__)   

@app.route("/", methods=["GET"])
def process_request():
    manufacturer = request.args.get('manufacturer')
    web_scraper = WebScraper()
    if manufacturer is not None:
        laptops = web_scraper.get_laptops_informations_from_url(manufacturer)
    else:
        laptops = web_scraper.get_laptops_informations_from_url()
    response = {
            "data":{
            "laptops": list(map(lambda laptop:laptop.to_dict(), laptops))}
        }
    code = 200
    return jsonify(response), 200
