'''
Library containing non-innertube related operations that are used by the various services

These operations do not go through the InnerTube API and are included for convenience

Usage:
    >>> from innertube import operations
    >>>
    >>> dir(operations)
    ...
    >>>
    >>> operations.complete_search
    <function complete_search at 0x7fd5476ec670>
    >>>
'''

import requests
import addict
import furl
import babel

from . import utils
from . import enums
from . import infos

from typing import \
(
    List,
)

def complete_search \
        (
            *,
            query:  str,
            client: str,
            locale: babel.Locale = None,
        ) -> List[str]:
    '''
    Dispatch a 'complete/search' request to suggestqueries.google.com

    Notes:
        * `client` refers to a ClientInfo.identifier string

    Reccomended devices for services:
        YouTube:      Tv
        YouTubeMusic: Android
        YouTubeKids:  Web
    '''

    response = requests.get \
    (
        url = furl.furl \
        (
            scheme = enums.Scheme.HTTPS.value,
            host   = 'suggestqueries.google.com',
            path   = 'complete/search',
        ),
        params = utils.filter_kwargs \
        (
            client = client,
            q      = query,
            hl     = locale and locale.language,
            gl     = locale and locale.territory,
            ds     = enums.DataSource.YOUTUBE,
            oe     = enums.Encoding.UTF_8,
            xhr    = enums.CharBool.TRUE,
            hjson  = enums.CharBool.TRUE,
        ),
        headers = \
        {
            enums.Header.USER_AGENT.value: infos.apps.get \
            (
                type = enums.AppType.YOUTUBE_WEB,
            ).product().user_agent(),
        },
    )

    return \
    [
        suggestion
        for suggestion, *_ in response.json()[1]
    ]
