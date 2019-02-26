from ptest.decorator import TestClass, Test, BeforeMethod
from utils.api_helpers import get, post, delete
from config import base_url, url_access_type
from utils.common_assertions import assert_response_status
from ptest.assertion import assert_equals


@TestClass(description="Test api")
class ApiTest:
    _auth_header_key = "Authorization"
    _auth_header_value = "Bearer {token}"
    _auth_header = {}
    _primitive_to_value_map = {}
    _id_to_post_id_map = {}

    @BeforeMethod(group="user crud")
    def get_bearer_token(self):
        auth_endpoint = "http://localhost:3000/api/song"
        response = get(auth_endpoint)
        parsed_response = response.json()
        self._auth_header[self._auth_header_key] = self._auth_header_value.format(token=parsed_response["token"])

    @Test(group="user crud")
    def test001_get_all_users(self):
        endpoint = base_url + url_access_type + "/users"
        response = get(endpoint, headers=self._auth_header)
        parsed_response = response.json()
        print(self._auth_header)
        assert_response_status(response, 200)
        print(parsed_response["_meta"]["success"])
        assert_equals(parsed_response["_meta"]["success"], True)
        self._primitive_to_value_map["id"] = parsed_response["result"][0]["id"]
        print(self._primitive_to_value_map)

    @Test(group="user crud")
    def test002_create_new_user(self):
        endpoint = base_url + url_access_type + "/users"
        payload = {
            "email": "ranit.si111@gmail.com",
            "first_name": "ranit",
            "last_name": "dey",
            "gender": "male"
                }
        response = post(endpoint, payload, headers=self._auth_header)
        parsed_response = response.json()
        self._primitive_to_value_map["id"] = parsed_response["result"]["id"]
        print(self._primitive_to_value_map)
        assert_response_status(response, 200)
        assert_equals(payload["email"], parsed_response["result"]["email"])
        assert_equals(payload["first_name"]+" "+payload["last_name"], parsed_response["result"]["name"])

    @Test(group="user crud")
    def test003_get_created_user_details(self):
        endpoint = base_url + url_access_type + "/users" + "/" + self._primitive_to_value_map["id"]
        response = get(endpoint, headers=self._auth_header)
        parsed_response = response.json()
        print(parsed_response)
        assert_response_status(response, 200)

    @Test(group="user crud")
    def test004_create_post_for_user(self):
        endpoint = base_url + url_access_type + "/posts"
        payload = {
            "user_id": self._primitive_to_value_map["id"],
            "title": "this is the title",
            "body": "this is my post"
        }
        response = post(endpoint, request_json=payload, headers=self._auth_header)
        parsed_response = response.json()
        self._id_to_post_id_map[self._primitive_to_value_map["id"]] = parsed_response["result"]["id"]
        print(self._id_to_post_id_map)


    @Test(group="user crud")
    def test005_get_post_details(self):
        endpoint = base_url + url_access_type + "/posts" + "/"+self._id_to_post_id_map[self._primitive_to_value_map["id"]]
        response = get(endpoint, headers=self._auth_header)
        parsed_response = response.json()
        print(parsed_response)

    @Test(group="user crud")
    def test006_delete_created_user(self):
        endpoint = base_url + url_access_type + "/users" + "/" + self._primitive_to_value_map["id"]
        response = delete(endpoint, headers=self._auth_header)
        parsed_response = response.json()
        print(parsed_response)
        assert_response_status(response, 200)
