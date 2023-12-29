# Python Media Processor (PMP)

## What
Quick and simple little tool to help automate the following tasks when adding things to my Jellyfin library:

1. Change ownership of downloaded media to the user/group Jellyfin uses
2. Movie media file (movie) or directory (tv) to appropriate destination


## Why
Faster/easier than manually running `chown` and `mv`. Would like to eventually sort out a way for it to run mnamer against the file(s) and get the metainfo sorted, but ya know.

## How
`python3 pmp.py <relative/path/to/media> <media type>`

Media type being "tv", "TV", "t", "movie", "Movie", or "m"
