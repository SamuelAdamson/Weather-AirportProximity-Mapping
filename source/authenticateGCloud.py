# Explicitly authenticate client for bigquery
# Libraries used - google cloud

def authenticate():
    from google.cloud import bigquery

    # Create new client with authentication from service account
    authClient = bigquery.Client.from_service_account_json(
        "missingKeyFile")

    # Return authenticated client
    return authClient
