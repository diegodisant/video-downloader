from json import loads
from pym3u8downloader import M3U8Downloader

class Video:
  url: str = ''
  path: str = ''

  def __init__(self, url: str, path: str) -> None:
    if not url or not path:
      raise ValueError(f"Error: Invalid video url or path, please fill the videos.json correctly")

    self.url = url
    self.path = path

  def download(self) -> None:

    downloader = M3U8Downloader(
      input_file_path=self.url,
      output_file_path=self.path,
    )

    downloader.download_playlist()

class VideoDownloader:
  @staticmethod
  def download_all_videos(videos: list) -> None:
    current_video: Video = None

    for video in videos:
      current_video = Video(video.url, video.path)
      current_video.download()

if __name__ == "__main__":
  try:
    with open('./videos.json', 'r') as videos_data:
      videos = loads(videos_data)

      VideoDownloader.download_all_videos(videos)
  except Exception as ex:
    print(f"Exception caught: {type(ex)}, with: {ex}")
