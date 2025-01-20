from datetime import datetime, timezone

import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests.adapters import HTTPAdapter, Retry
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

from blizzapi.core.utils import BearerAuth


class OAuth2Client:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        token_uri: str,
        token_expiration_grace_period: int = 60,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_uri = token_uri
        self.token = None
        self.token_expiration_grace_period = token_expiration_grace_period  # Amount of minutes left on a token expirations to trigger requesting a new token

        self.s = requests.Session()
        retries = Retry(
            total=3, backoff_factor=0.2, status_forcelist=[500, 502, 503, 504, 404, 403]
        )

        self.s.mount("https://", HTTPAdapter(max_retries=retries))

    def get(self, uri):
        self.refresh_token()
        response = self.s.get(uri, auth=BearerAuth(self.token["access_token"]))
        return response.json()

    def refresh_token(self):
        if self.token is None:
            self.get_new_token()
        elif self.token_expiring_soon():
            self.get_new_token()

    def get_new_token(self):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)

        self.token = oauth.fetch_token(
            token_url=self.token_uri,
            auth=HTTPBasicAuth(self.client_id, self.client_secret),
        )

    def token_expiring_soon(self):
        expire_time = datetime.fromtimestamp(self.token["expires_at"], timezone.utc)
        now_time = datetime.now(timezone.utc)

        difference = expire_time - now_time
        minutes_left = difference.total_seconds() / 60
        return minutes_left <= self.token_expiration_grace_period
