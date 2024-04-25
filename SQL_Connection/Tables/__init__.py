"""Initialization of parent folder as python module"""

# from SQL_Connection.tables.tbl_acc_groupMembers import TblAccGroupMembers
# from SQL_Connection.tables.tbl_acc_groupRoles import TblAccGroupRoles
from SQL_Connection.tables.tbl_acc_groups import TblAccGroups, create_new_group
from SQL_Connection.tables.tbl_acc_roles import TblAccRoles, create_new_role
from SQL_Connection.tables.tbl_acc_userRoles import TblAccUserRoles
from SQL_Connection.tables.tbl_acc_users import TblAccUsers, create_new_user
from SQL_Connection.tables.tbl_acc_usersInvited import TblAccUsersInvited
from SQL_Connection.tables.tbl_cms_categories import (
    TblCMSCategories,
    create_new_category,
)
from SQL_Connection.tables.tbl_cms_contentAttachments import (
    TblCMSContentAttachments,
    create_new_attachment,
)
from SQL_Connection.tables.tbl_cms_contentDownloads import (
    TblCMSContentDownloads,
    create_new_download,
)
from SQL_Connection.tables.tbl_cms_contentFileComponentProperties import (
    TblCMSContentFileComponentProperties,
    create_new_property,
)
from SQL_Connection.tables.tbl_cms_contentFileComponents import (
    TblCMSContentFileComponents,
    create_new_component,
)
from SQL_Connection.tables.tbl_cms_contentFiles import (
    TblCMSContentFiles,
    create_new_file,
)
from SQL_Connection.tables.tbl_cms_contentLibraries import (
    TblCMSContentLibraries,
    create_new_content_library,
)
from SQL_Connection.tables.tbl_cms_contents import TblCMSContents, create_new_content
from SQL_Connection.tables.tbl_cms_libraries import TblCMSLibraries, create_new_library
from SQL_Connection.tables.tbl_cms_savedSearches import (
    TblCMSSavedSearches,
    create_new_saved_search,
)
from SQL_Connection.tables.tbl_cms_searches import TblCMSSearches, create_new_search
from SQL_Connection.tables.tbl_cms_tags import TblCMSTags, create_new_tag
from SQL_Connection.tables.tbl_core_refreshed import (
    TblCoreRefreshed,
    create_new_refreshed,
    get_last_refreshed,
)
from SQL_Connection.tables.tbl_csl_app_sessions import (
    TblCSLAppSessions,
    create_new_app_session,
)
from SQL_Connection.tables.tbl_csl_licenses import TblCSLLicenses, create_new_license
from SQL_Connection.tables.tbl_csl_products import TblCSLProducts, create_new_product
