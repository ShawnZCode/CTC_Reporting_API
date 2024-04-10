"""Entry point to the API Core application.
Allows fetching data in a structured class tuned for the CTC Reporting API."""

import APICore.result_models.accounts as ctc_accounts
import APICore.result_models.cms as ctc_cms
import APICore.result_models.csl as ctc_csl
import APICore.result_models.pal as ctc_pal
from APICore.api_get_functions import get_all_x, get_x_by_id
from APICore.connection_models.scopes import (
    API_SCOPES,
    account_scope,
    cms_scope,
    csl_scope,
    pal_scope,
)
