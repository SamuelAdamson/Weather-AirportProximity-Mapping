# Explicitly authenticate client for bigquery
# Libraries used - google cloud

def authenticate():
    from google.cloud import bigquery

    # Create new client with authentication from service account
    authClient = bigquery.Client.from_service_account_json(
        "../keys/mh-casestudy-location-21123-f9dfcf505b13.json")

    # Return authenticated client
    return authClient
