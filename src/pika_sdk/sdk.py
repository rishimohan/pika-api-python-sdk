import requests

from pika_sdk.exceptions import APIException, BadRequestException


class PikaApi:
    def __init__(self, api_key):
        self.api_key = api_key

    def _get_base_url(self, version='v1'):
        base_url = "https://api.pika.style"

        return f"{base_url}/{version}"
    
    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def generate_image_from_template(self, template_id, modifications, response_format="base64"):
        endpoint_url = f"{self._get_base_url()}/templates/{template_id}/images"

        data = {
            'response_format': response_format,
            'modifications': modifications
        }

        response = requests.post(endpoint_url, headers=self._get_headers(), json=data)

        if response.status_code == 200:
            if response_format == "base64":
                return response.json()
            else:    
                return response
        elif response.status_code == 400:
            error_response = response.json().get('error')

            raise BadRequestException(error_response)
        else:
            raise APIException(f"An error occurred while generating an image. Status code: {response.status_code}. Error: {response.json().get('error')}")
