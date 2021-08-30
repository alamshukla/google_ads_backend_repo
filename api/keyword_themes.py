import os
import sys
import json

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

def get_keyword_themes_suggestions(refresh_token, keyword_text, country_code, language_code):

    try:

        # Configurations
        GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
        GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
        GOOGLE_DEVELOPER_TOKEN = os.environ.get("GOOGLE_DEVELOPER_TOKEN", None)
        GOOGLE_LOGIN_CUSTOMER_ID = os.environ.get("GOOGLE_LOGIN_CUSTOMER_ID", None)

        # Configure using dict (the refresh token will be a dynamic value)
        credentials = {
        "developer_token": GOOGLE_DEVELOPER_TOKEN,
        "refresh_token": refresh_token,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "login_customer_id": GOOGLE_LOGIN_CUSTOMER_ID}

        client = GoogleAdsClient.load_from_dict(credentials)

        """Retrieves KeywordThemeConstants for the given criteria.
        Args:
            client: an initialized GoogleAdsClient instance.
            keyword_text: a keyword used for generating keyword themes.
        Returns:
            a list of KeywordThemeConstants.
        """

        keyword_theme_constant_service = client.get_service(
        "KeywordThemeConstantService"
        )
        request = client.get_type("SuggestKeywordThemeConstantsRequest")
        request.query_text = keyword_text
        request.country_code = country_code
        request.language_code = language_code

        response = keyword_theme_constant_service.suggest_keyword_theme_constants(
            request=request
        )
    
        keyword_theme_constants = response.keyword_theme_constants

        data = []
        for i in keyword_theme_constants:

            test_keyword_theme_sugg = i.display_name
            data.append(test_keyword_theme_sugg)
            
        print("print data type: ", type(data))
        print("print data: ", data)

        json.dumps(data)

        return data
    
    except GoogleAdsException as ex:
        print(
            f'Request with ID "{ex.request_id}" failed with status '
            f'"{ex.error.code().name}" and includes the following errors:'
        )
        for error in ex.failure.errors:
            print(f'\tError with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
        sys.exit(1)