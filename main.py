from moesifpythonrequest.start_capture.start_capture import StartCapture
import requests


def identify_user(req, res):
    return 'my_user_id'


def identify_company(req, res):
    return 'my_company_id'


def get_token(req, res):
    # If you don't want to use the standard WSGI session token,
    # add your custom code that returns a string for session/API token
    return "XXXXXXXXXXXXXX"


def get_metadata(req, res):
    return {
        'datacenter': 'westus',
        'deployment_version': 'v1.2.3',
    }


def should_skip(req, res):
    # Your custom code that returns true to skip logging
    return "health/probe" in req.url


moesif_settings = {
    'APPLICATION_ID': 'Your Moesif Application Id',
    'LOG_BODY_OUTGOING': True,
    'GET_SESSION_TOKEN_OUTGOING': get_token,
    'GET_METADATA_OUTGOING': get_metadata,
    'IDENTIFY_USER_OUTGOING': identify_user,
    'IDENTIFY_COMPANY_OUTGOING': identify_company,
    'SKIP_OUTGOING': should_skip
}


def main():
    # Outgoing API call to third party like Github / Stripe or to your own dependencies
    response = requests.get("http://httpbin.org/uuid")
    print(response.json())


if __name__ == "__main__":
    StartCapture().start_capture_outgoing(moesif_settings)
    main()
