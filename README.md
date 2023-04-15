# dp-proxy
DIfferential Privacy Proxy

This is a bare bones project demonstrating how to build Privacy Proxy for adding niose to the query results in order to preserve privacy.
Installation

    Clone the repository: git clone https://github.com/akihug/dp-proxy.git
    Navigate to the project directory: cd dp-proxy
    Install the required dependencies: pip install -r requirements.txt

Usage

    Start the server: uvicorn main:app --reload
    Navigate to http://localhost:8000/docs to view the API documentation.
    Use the API endpoints to interact with the application.

API Endpoints

The following API endpoints are available:

Returns the noise added query results. Only COUNT,SUM aggregate queries are allowed.

POST /get_dp_result
body: {'query': str}

Contributing:
If you would like to contribute to this project, please submit a pull request.
