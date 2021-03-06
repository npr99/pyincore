# Copyright (c) 2019 University of Illinois and others. All rights reserved.
#
# This program and the accompanying materials are made available under the
# terms of the Mozilla Public License v2.0 which accompanies this distribution,
# and is available at https://www.mozilla.org/en-US/MPL/2.0/

from logging import config as logging_config

import logging
import os

PACKAGE_VERSION = "0.5.4"

INCORE_API_PROD_URL = "https://incore.ncsa.illinois.edu"
INCORE_API_DEV_URL = "https://incore-dev-kube.ncsa.illinois.edu"

KONG_INCORE_API_PROD_URL = "https://incore2-services.ncsa.illinois.edu"
KONG_INCORE_API_DEV_URL = "https://incore2-services-dev.ncsa.illinois.edu"

KEYCLOAK_AUTH_PATH = "/auth/realms/In-core/protocol/openid-connect/token"
CLIENT_ID = "react-auth"
INCORE_LDAP_TEST_USER_INFO = "{\"preferred_username\": \"incrtest\"}"

PYINCORE_PACKAGE_HOME = os.path.dirname(__file__)
PYINCORE_ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
USER_HOME = os.path.expanduser('~')
USER_CACHE_DIR = ".incore"
PYINCORE_USER_CACHE = os.path.join(USER_HOME, USER_CACHE_DIR)

DATA_CACHE_FOLDER_NAME = "cache_data"
PYINCORE_USER_DATA_CACHE = os.path.join(PYINCORE_USER_CACHE, DATA_CACHE_FOLDER_NAME)

TOKEN_FILE_NAME = ".incoretoken"

LOGGING_CONFIG = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logging.ini'))
logging_config.fileConfig(LOGGING_CONFIG)
LOGGER = logging.getLogger('pyincore')

MAX_LOGIN_ATTEMPTS = 3
