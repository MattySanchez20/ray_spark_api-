import requests
from typing import Dict
import ray
import pandas as pd

@ray.remote
def _unbored_me(url: str) -> Dict:
    """Make a request to the unbored.me API and return the response.
        url: str: The URL to make the request to.

        return: Dict: The response from the API.
    """
    request = requests.get(url=url)

    response = request.json()

    return response

def _create_df_from_response(values: Dict) -> pd.DataFrame:
    """Create a DataFrame from the response values.
        values: Dict: The values to create the DataFrame from.

        return: pd.DataFrame: The DataFrame created from the values.
    """
    df = pd.DataFrame(values)

    return df

def get_unbored_me_df(n: int) -> pd.DataFrame:
    """Get a DataFrame of activities from the unbored.me API.
        n: int: The number of activities to get.

        return: pd.DataFrame: The DataFrame of activities.
    """
    responses = [
        _unbored_me.remote(url) for url in [
            "http://www.boredapi.com/api/activity/",
        ] * n
    ]

    values = ray.get(responses)

    df = _create_df_from_response(values)

    return df
