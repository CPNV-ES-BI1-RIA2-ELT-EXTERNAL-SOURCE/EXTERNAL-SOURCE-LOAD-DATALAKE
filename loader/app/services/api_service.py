import requests

def api_service(url : str, method="GET", payload=None, params=None, headers=None, save_path=None):
    """
    A service function to handle both file downloads and standard API requests.

    :param url: str - The base URL for the API.
    :param method: str - The HTTP method (GET, POST, PUT, DELETE).
    :param payload: dict - The JSON payload for the request body.
    :param params: dict - The query parameters for the request.
    :param headers: dict - HTTP headers for the request.
    :param save_path: str - If provided, saves the response as a file.
    :return: dict or None - JSON response if applicable, or None if a file is downloaded or an error occurs.
    """
    try:
        url = f"{base_url}/{endpoint}"
        method = method.upper()
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=payload,
            params=params,
            stream=bool(save_path)  # Enable streaming for file downloads
        )
        response.raise_for_status()  # Check for HTTP errors

        if save_path:
            # Save the response content to a file
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"File successfully downloaded: {save_path}")
            return None
        else:
            # Return the JSON response if no file is being saved
            return response.json()
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
