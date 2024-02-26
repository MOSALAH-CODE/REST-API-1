import datetime

from cfeapi.settings import SECRET_KEY

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication', #Oauth, JWT
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_PAGINATION_CLASS': 'cfeapi.restconf.pagination.CFEAPIPagination',
    'DEFAULT_FILTER_BACKENDS': (
            'rest_framework.filters.SearchFilter',
            'rest_framework.filters.OrderingFilter',
    ),
    'SEARCH_PARAM': 'q',
    'ORDERING_PARAM': 'ordering',
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("JWT",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "SLIDING_TOKEN_REFRESH_LIFETIME": datetime.timedelta(days=7),
    
    "TOKEN_OBTAIN_SERIALIZER": "accounts.api.utils.jwt_response_payload_handler",

    # "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

# JWT_AUTH = {
#     'JWT_ENCODE_HANDLER':
#     'rest_framework_jwt.utils.jwt_encode_handler',

#     'JWT_DECODE_HANDLER':
#     'rest_framework_jwt.utils.jwt_decode_handler',

#     'JWT_PAYLOAD_HANDLER':
#     'rest_framework_jwt.utils.jwt_payload_handler',

#     'JWT_PAYLOAD_GET_USER_ID_HANDLER':
#     'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

#     'JWT_RESPONSE_PAYLOAD_HANDLER':
#     #'rest_framework_jwt.utils.jwt_response_payload_handler'
#     'accounts.api.utils.jwt_response_payload_handler',

#     'JWT_ALLOW_REFRESH': True,
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

#     'JWT_AUTH_HEADER_PREFIX': 'JWT', # Authorization: JWT <token>
#     'JWT_AUTH_COOKIE': None,

# }
