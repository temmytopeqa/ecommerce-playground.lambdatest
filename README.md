# ecommerce-playground.lambdatest
ecommerce-playground.lambdatest/
│
├── ActionPage/
│   ├── base_page.py               # Common reusable base methods
│   ├── home_page.py               # Handles homepage navigation
│   ├── product_page.py            # Product selection and interaction
│   ├── cart_popup_page_.py        # Interacts with cart popup after adding to cart
│   └── checkout_page.py           # (Optional) Checkout form handler
│
├── Config/
│   ├── __init__.py
│   └── configuration.py           # Global config, including base URL
│
├── LocatorPage/
│   ├── __init__.py
│   └── locator_home.py            # Element locators for UI pages
│
├── test_suite.py                  # Main test file
├── requirements.txt               # Python package dependencies
├── report.html                    # Generated HTML report (after test run)
└── README.md                      # You are here!

⚙️ Configuration
The base URL is managed from Config/configuration.py:

python
Copy
Edit
class Config:
    BASE_URL = "https://ecommerce-playground.lambdatest.io/"
In your test file (test_suite.py), it’s imported like this:

python
Copy
Edit
from Config.configuration import Config
driver.get(Config.BASE_URL)
✅ What the Test Does
Opens the base e-commerce homepage

Navigates to the Headphones category

Adds the first product to cart (if available)

Proceeds to checkout via the cart popup

Confirms redirection to cart or checkout page

If products are sold out, the test gracefully handles it without breaking.

🧪 Running the Test
To run the tests and generate a report:

bash
Copy
Edit
pytest --html=report.html
Then open the report:

bash
Copy
Edit
start report.html  # Windows
# OR
open report.html   # macOS
📦 Requirements
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Example requirements.txt:

text
Copy
Edit
selenium
pytest
pytest-html
🚀 Future Improvements
Add form-filling with valid/invalid data

Use pytest.ini for test configs

Add parallel test execution via pytest-xdist

Implement page object assertions

Use .env for secret values (e.g., credentials, keys)

