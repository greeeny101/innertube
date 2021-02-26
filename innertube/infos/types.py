import enum

class DeviceType(enum.Enum):
    Web     = 'web'
    Android = 'android'
    Ios     = 'ios'
    Tv      = 'tv'

class ServiceType(enum.Enum):
    YouTube       = 'youtube'
    YouTubeMusic  = 'youtube.music'
    YouTubeKids   = 'youtube.kids'
    YouTubeStudio = 'youtube.creator'