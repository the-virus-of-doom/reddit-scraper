# Reddit Scraper [WIP NAME]

This project is to be used to export saved content from reddit and then provide sources to the content, grabbing higher resolutions if found.

## General Structure

### Input

Export data from a Reddit account to get the full list of saved posts from the `saved_posts.csv` file. Read this to generate a list of Reddit posts (or comments) to visit with the scraper. This file can be exported from the Reddit account settings once every 30 days from the following link: <https://www.reddit.com/settings/data-request>
We aren't using the Reddit API directly because it limits the user to 1000 posts and we want to be able to scrape all of the posts. Eventually we will want to use the API to get the most recent posts, but for now we will just use the exported data.

### Content Scraping

Check to see what the thing is then call the appropriate downloader function (if it varies by source).
Additionally, check the comments to see if they contain an original source linked.

### Content Tagging

Find the content on a source aggregation site (such as <https://safebooru.org/> or *other* alternatives) and return a list of tags to associate with the local content.

### Local Database

Note: I have no clue how this should be done.

Albums and galleries should be stored as a single entry in the database, with a list of the individual content IDs.

Should contain the following fields:

- Reddit ID (primary key) (string)
- Permalink (URL)
- Access date (last time it was checked)
- NSFW (boolean)
- Tags (list of strings)
- HQ source (if found) (URL)
- Has been downloaded (boolean)
- Download date (date)
- Download location (path)
- isAlbum (boolean)

If the content is an individual image or video, the following fields should also be included:

- Downloaded file name (string)
- Downloaded file type (string)
- Downloaded file size (int)
- Downloaded file hash (string)

If the content is an album or gallery, the following fields should also be included [WIP]:

- Album ID (if isAlbum) (string)
- Album size (if isAlbum) (int)
- Album hash (if isAlbum) (string)
- Album content (if isAlbum) (list of strings)
- Album content type (if isAlbum) (list of strings)

### Storage

Downloaded content should be stored in a folder structure based on the original subreddit the content was posted to. The folder structure should be as follows:
`<root folder>/<subreddit>/<content type>/<content ID>.<file extension>`
For example:
`/home/user/reddit-scraper/aww/images/1234567890.jpg`
For albums and galleries, the content type should be `albums` and the content ID should be the Reddit ID of the post. The content should be stored in a folder with the same name as the content ID. The folder structure should be as follows:
`<root folder>/<subreddit>/albums/<content ID>/<content ID>_<content number>.<file extension>`
For example:
`/home/user/reddit-scraper/aww/albums/1234567890/1234567890_1.jpg`

### Presentation

Display the local database in a web interface, with the ability to filter by tags and search for content. The web interface should also allow for the addition of tags to the local database and the ability to favorite content. 

## Content Sources

Each content source should have its own scraper function, but the general structure should be the same.
    1 - Check the content type (image, video))
    2 - Check the comments for a source
    3 - Download the content, using the original source if found
    4 - Add the content to the local database

A generic scraper function should be created that takes the content type and the URL as input and returns the content as a file. This function will be used by the content source specific scraper functions to download the raw content.

The following content sources may need custom scrapers to format the content for the generic scraper function:

### Reddit [High Priority]

Reddit hosts multiple types of content and can be directly linked to, which should make it easy to download the content.
Gallery/album posts will be need to be downloaded with additional logic.

### Imgur [High Priority]

Imgur hosts multiple types of content and can be directly linked to, which should make it easy to download the content.
Gallery/album posts will be need to be downloaded with additional logic.
I don't know if nsfw content will have the age gate warning page, but there should be a way around it, especially if we are using the API.

### Twitter [Medium Priority]

Twitter hosts multiple types of content and can be directly linked to, which should make it easy to download the content.
If the content is a video, it should be downloaded as a video file, not as a gif.
There may be an age gate, but that should be easy to bypass if we are using the API or an account. (Note: Twitter API changes may make this difficult so we may have to just scrape it.)

### Gfycat / Redgifs [Medium Priority]

Gfycat and Redgifs host videos and gifs and can be directly linked to, which should make it easy to download the content. However, there are different resolutions available (SD/HD), so we want to download the highest resolution available.
When Gfycat and Redgifs are linked to, they are usually linked to the page, not the file itself. This means that we need to scrape the page to find the link to the file.
NSFW Gfycat content moved to Redgifs in 2019 and the links are still valid, so we should be able to download the content from Redgifs.

### Pixiv [Medium Priority]

Pixiv hosts images and typically is the original source when directly linked to.

### *booru [Low Priority]

We might be able to get the tags here to save a step.

## Tagging

Content will be tagged based on the subreddit it was posted to and the tags found on the source aggregation site. The tags will be stored in a local database and will be used to filter the content in the web interface.

Specific tags will be added to the local database based on the content type (image, video, album, etc.), content source (Reddit, Imgur, etc.), content resolution (SD, HD, etc.), artist, and other tags found on the source aggregation site.

## Web Interface

The web interface should be a simple web page that displays the content in the local database. The content should be displayed as a gallery with the following information:

- Content (image or video)
- Artist
- Tags

The content should be able to be filtered by tags and searched for content. The content should also be able to be favorited and tagged by the user.

## Future Features

- Download content from the Reddit API
- Additional content source scrapers
- Additional tagging sources
- Additional content types (text, audio, etc.)
- Additional web interface features (sorting, etc.)
- Content deduplication

## Tech Stack

Things we are using [updated as we go]:

- PRAW (Python Reddit API Wrapper)
