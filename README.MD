# Teste Backend Web Scraping

Deploying Python web scraping to get information about laptops in [https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops](https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops).

## Heroku APP

For use the API hosted in heroku, you need to make a GET request in this link:

```
https://teste-backend-gabrielhvm.herokuapp.com/
```

When the request response with sucess you will receive a JSON object with this structure:

```
{
    "data":
        "laptops": <LIST OF LAPTOPS>
}
```
Where ```<LIST OF LAPTOPS>``` is the list containing all laptops of the manufacturer Lenovo orderer by price.

### Special use
If you need a list of another manufacturer just pass in the link, like (example with manufacturer Asus):

```
https://teste-backend-gabrielhvm.herokuapp.com/?manufacturer=asus
```

The response is like the normal usage

## Run localy
To run this app in localhost, you will need this requirements:

 - Python >= 3.7
 - Packages of the file ```requirements.txt``` installeds

After the installation of the requirements, you will need to run the file wsgi.py:

```
python wsgi.py
```
When you run the app, it will show this lines in you terminal:

```
 * Serving Flask app 'app.main' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

Informing that app is ready to use. Therefore, for use the app you will need to make a GET request [like in Heroku app](##heroku-app), but now you will make this request in the localhost link with port 5000:

```
http://127.0.0.1:5000
```

If you need to change the port of the application: go to the line 5 of the file ```wsgi.py``` and change the attribute ```port``` to the port you want.