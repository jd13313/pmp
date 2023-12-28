import os
import argparse
import shutil
import sys
from dotenv import load_dotenv

def parse_args():
    parser = argparse.ArgumentParser(description='Process args')
    parser.add_argument('path', metavar='p', type=str)
    parser.add_argument('media_type', metavar='m', type=str)

    return parser.parse_args()

# Grab args
args = parse_args()
media_file_path = args.path
media_type = args.media_type

load_dotenv()

# Change ownership of the file to jellyfin:jellyfin
print("Changing ownership of file to jellyfin...")
group_id = 1000
user_id = 1000
os.chown(media_file_path, user_id, group_id)

# Move files
destination_tv = os.getenv('TV_PATH')
destination_movies = os.getenv('MOVIES_PATH')
is_file = os.path.isfile(media_file_path)

valid_tv_args = ['tv', 'TV', 't', 'T']
valid_movie_args = ['movie', 'Movie', 'm', 'M']

if media_type in valid_tv_args:
    print("Moving file to TV folder...")

    if is_file:
        print("TV Shows should be a folder, not a single file! Exiting...")
        sys.exit(1)
    else:
        print("Moving TV show to TV folder...")
        shutil.move(media_file_path, destination_tv)
elif media_type in valid_movie_args:
    print("Moving file to Movies folder...")

    if is_file:
        print("Moving movie to Movies folder...")
        shutil.move(media_file_path, destination_movies)
    else:
        print("Movies should be a single file, not a folder! Exiting...")
        sys.exit(1)
else:
    print("Invalid media type, exiting...")
    sys.exit(1)


print("Done! Should probably run mnamer and a library scan in jellyfin next.")
sys.exit()
