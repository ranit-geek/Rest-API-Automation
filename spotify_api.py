from ptest.decorator import TestClass, Test
import config
from utils.api_helpers import get, post
from ptest.assertion import assert_equals
from utils.schema_validation import validate_schema
from test_data import schema


@TestClass()
class SpotifyApi:
    _auth_header_key = "Authorization"
    _auth_header_value = "Bearer {token}"
    _auth_header = {}
    _endpoint = ""
    _user_map = []
    _user_playlist_map = {}

    @Test()
    def test001_get_current_user(self):
        self.endpoint = config.base_url_spotify+"/me"
        self._auth_header[self._auth_header_key] = self._auth_header_value.format(token=config.spotify_token)
        response = get(self.endpoint, headers=self._auth_header)
        parsed_response = response.json()
        assert_equals(response.status_code, 200)
        self._user_map.append(parsed_response["id"])
        validate_schema(schema.my_details_schema,parsed_response)

       # validate_schema(schema.my_details_schema,parsed_response)


    @Test()
    def test002_create_playlist(self):
        self.endpoint = config.base_url_spotify+"/users/{user_id}/playlists".format(user_id=self._user_map[0])
        payload = {
            "name": "Test999 playlist",
            "public": False
        }
        response = post(self.endpoint, payload, headers=self._auth_header)
        parsed_response = response.json()
        print(parsed_response)
        assert_equals(self._user_map[0], parsed_response["owner"]["id"])
        self._user_playlist_map[self._user_map[0]] = parsed_response["id"]
        print(self._user_playlist_map)













