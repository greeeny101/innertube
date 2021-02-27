# innertube
Python Client for Google's Private InnerTube API (works with YouTube, YouTube Music etc.)

### Installation
```shell
$ foo...
```

### But, what about the [YouTube Data API](https://developers.google.com/youtube/v3/)?
|                                       | This Library | YouTube Data API |
| ------------------------------------- | ------------ | ---------------- |
| No Google account required            | &check;      | &cross;          |
| No request limit                      | &check;      | &cross;          |
| Clean, reliable, well-structured data | &cross;      | &check;          |

#### Wait a sec! What do you mean it's not clean, reliable and well-structured??
Well, the private InnerTube API is not designed for consumption by users, it is used to render and operate the various YouTube services.

#### What does that mean?
Simply put, the data returned by the InnerTube API will need to be parsed and sanitised to extract the usable data as it will contain a lot of fluff that is unlikely to be of any use. These higher-level clients are in the works!

### Usage
```python
>>> import innertube
>>>
>>> # Create a client
>>> client = innertube.client \
(
    device  = innertube.devices.Web,      # Could also be Android etc.
    service = innertube.services.YouTube, # Could also be YouTubeMusic etc.
)
>>>
>>> # View the client
>>> client
<Client(device='Web', service='YouTube')>
>>>
>>> # Get some data!
>>> data = client.search(query = 'foo fighters')
>>>
```

### Clients
|         | YouTube | YouTubeMusic | YouTubeKids | YouTubeStudio |
| ------- | ------- | ------------ | ----------- | ------------- |
| Web     | &check; | &check;      | &check;     | &check;       |
| Android | &check; | &check;      | &check;     | &check;       |
| Ios     | &check; | &check;      | &check;     | &check;       |
| Tv      | &check; | &cross;      | &cross;     | &cross;       |

### Authentication
The InnerTube API uses OAuth2, however I have been unable to successfully implement authentication.
Therefore, this library currently only provides unauthenticated access to the API.
