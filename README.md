# Moesif Outgoing Example for Python

This is an example to capture outgoing API calls to send to Moesif for API Analytics and monitoring.

[Moesif](https://www.moesif.com) is an API analytics platform. [moesifpythonrequest](https://github.com/Moesif/moesifpythonrequest)
a library to capture outgoing API calls to send to Moesif.

## Configuration options

##### __`IDENTIFY_USER_OUTGOING`__
(optional, but highly recommended) _(req, res) => string_, a function that takes [Requests](http://docs.python-requests.org/en/master/api/) request and response, and returns a string that is the user id used by your system. While Moesif tries to identify users automatically,
but different frameworks and your implementation might be very different, it would be helpful and much more accurate to provide this function.

##### __`IDENTIFY_COMPANY_OUTGOING`__
(optional) _(req, res) => string_, a function that takes [Requests](http://docs.python-requests.org/en/master/api/) request and response, and returns a string that is the company id for this event.

##### __`GET_METADATA_OUTGOING`__
(optional) _(req, res) => dictionary_, a function that takes [Requests](http://docs.python-requests.org/en/master/api/) request and response, and
returns a dictionary (must be able to be encoded into JSON). This allows
to associate this event with custom metadata. For example, you may want to save a VM instance_id, a trace_id, or a tenant_id with the request.

##### __`GET_SESSION_TOKEN_OUTGOING`__
(optional) _(req, res) => string_, a function that takes [Requests](http://docs.python-requests.org/en/master/api/) request and response, and returns a string that is the session token for this event. Again, Moesif tries to get the session token automatically, but if you setup is very different from standard, this function will be very help for tying events together, and help you replay the events.

##### __`LOG_BODY_OUTGOING`__
(optional) _boolean_, default True, Set to False to remove logging request and response body.

##### __`SKIP_OUTGOING`__
(optional) _(req, res) => boolean_, a function that takes a [Requests](http://docs.python-requests.org/en/master/api/) request and response,
and returns true if you want to skip this particular event.

## How to run this example.

First you'll need to get the source of the project. Do this by cloning the repository:

```bash
# Get the project code
git clone https://github.com/Moesif/moesif-python-outgoing-example.git
```

*NOTE: While working with Python, we would recommend to use virtual environment
to keep all the project's dependencies isolated from other projects.*

##### Create your local environment

```bash
conda create -n outgoingrequest python=3.6 anaconda # Create the environment
source activate outgoingrequest # Activate the environment
```

##### Install dependencies 

```bash
pip install -r requirements.txt
```

##### Be sure to edit the `main.py` to include your own application id.

```
moesif_settings = {
    'APPLICATION_ID': 'Your Moesif Application Id'
}
```

 Your Moesif Application Id can be found in the [_Moesif Portal_](https://www.moesif.com/).
After signing up for a Moesif account, your Moesif Application Id will be displayed during the onboarding steps. 

You can always find your Moesif Application Id at any time by logging 
into the [_Moesif Portal_](https://www.moesif.com/), click on the top right menu,
and then clicking _API Keys_.

##### Start the application
```bash
python main.py
```

The data should be captured in the corresponding Moesif account.

Congratulations! If everything was done correctly, Moesif should now be tracking outgoing network requests. If you have any issues with set up, please reach out to support@moesif.com.

## Other integrations

To view more documentation on integration options, please visit __[the Integration Options Documentation](https://www.moesif.com/docs/getting-started/integration-options/).__
