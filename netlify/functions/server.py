import sys
import os
from pathlib import Path

# Add the project root to the path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

# Load environment variables
from dotenv import load_dotenv
load_dotenv(project_root / ".env")

from app import create_app

app = create_app()

# Netlify Functions handler
def handler(event, context):
    """
    AWS Lambda handler for Netlify Functions
    Converts HTTP events to Flask requests
    """
    from werkzeug.wrappers import Request, Response
    
    # Build the WSGI environ from the event
    http_method = event.get("httpMethod", "GET")
    path = event.get("path", "/")
    query_string = event.get("queryStringParameters") or {}
    headers = event.get("headers", {})
    body = event.get("body", "")
    
    environ = {
        "REQUEST_METHOD": http_method,
        "SCRIPT_NAME": "",
        "PATH_INFO": path,
        "QUERY_STRING": "&".join([f"{k}={v}" for k, v in query_string.items()]) if query_string else "",
        "CONTENT_TYPE": headers.get("content-type", ""),
        "CONTENT_LENGTH": len(body) if body else 0,
        "SERVER_NAME": headers.get("host", "localhost").split(":")[0],
        "SERVER_PORT": "443",
        "SERVER_PROTOCOL": "HTTP/1.1",
        "wsgi.version": (1, 0),
        "wsgi.url_scheme": "https",
        "wsgi.input": None,
        "wsgi.errors": sys.stderr,
        "wsgi.multithread": False,
        "wsgi.multiprocess": True,
        "wsgi.run_once": False,
    }
    
    # Add headers to environ
    for header_name, header_value in headers.items():
        header_name = header_name.upper().replace("-", "_")
        if header_name not in ["CONTENT_TYPE", "CONTENT_LENGTH"]:
            environ[f"HTTP_{header_name}"] = header_value
    
    # Simulate WSGI call
    response_data = []
    response_status = None
    response_headers = None
    
    def start_response(status, headers, exc_info=None):
        nonlocal response_status, response_headers
        response_status = status
        response_headers = headers
        return response_data.append
    
    try:
        # Call Flask app
        app_iter = app(environ, start_response)
        response_data.extend(app_iter)
        
        # Parse status code
        status_code = int(response_status.split(" ")[0])
        
        # Convert headers to dict
        headers_dict = {}
        for header_name, header_value in response_headers:
            headers_dict[header_name] = header_value
        
        # Return Lambda response
        return {
            "statusCode": status_code,
            "headers": headers_dict,
            "body": "".join(response_data),
            "isBase64Encoded": False,
        }
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": '{"error": "Internal server error"}',
            "isBase64Encoded": False,
        }
