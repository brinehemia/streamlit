import requests
from decouple import config
from services.cookies import cookiesManager

class ApiClient:
    def __init__(self, base_url=None, cookies_manager=None):
        self.base_url = base_url or config("BASE_URL")
        self.cookies_manager = cookies_manager or cookiesManager 
        self.token = self.get_token_from_cookie()

    def get_token_from_cookie(self):
        if self.cookies_manager.ready():
            return self.cookies_manager.get("jwt_token")
        return None

    def request(self, method, endpoint, data=None, files=None, auth_required=True):
        url = f"{self.base_url}{endpoint}"
        
        headers = { "Content-Type": "application/json" }
        if auth_required and self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=data, files=files)
            elif method.upper() == "PUT":
                response = requests.put(url, headers=headers, json=data)
            elif method.upper() == "DELETE":
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError(f"Metode HTTP tidak valid: {method}")

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status_code": response.status_code if response else None}

    def get(self, endpoint, auth_required=True):
        return self.request("GET", endpoint, auth_required=auth_required)

    def post(self, endpoint, data, auth_required=True):
        return self.request("POST", endpoint, data=data, auth_required=auth_required)

    def put(self, endpoint, data, auth_required=True):
        return self.request("PUT", endpoint, data=data, auth_required=auth_required)

    def delete(self, endpoint, auth_required=True):
        return self.request("DELETE", endpoint, auth_required=auth_required)

    def upload_file(self, endpoint, file_path, additional_data=None, auth_required=True):
        with open(file_path, 'rb') as file:
            files = {'file': file}
            data = additional_data or {}
            return self.request("POST", endpoint, data=data, files=files, auth_required=auth_required)