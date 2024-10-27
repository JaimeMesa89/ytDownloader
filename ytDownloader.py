from pytubefix import YouTube
import argparse

def download_video_highest_resolution(url, output_path):
    try:
        yt = YouTube(url)

        ys = yt.streams.get_highest_resolution()

        print("Downloading video: %s" % yt.title)
        ys.download(output_path=output_path)
        print("Download complete!")
    
    except Exception as e:
        print(e)

def download_video_selected_resolution(url, resolution, output_path):
    try:
        yt = YouTube(url)

        ys = yt.streams.filter(resolution=resolution, file_extension='mp4').first()
        if not ys:
            print("Could not find a stream with resolution of %s" %resolution)
            print("Please select one of these:")

            for stream in yt.streams.filter(file_extension='mp4'):
                print(stream)
        else:
            print("Downloading video: %s" % yt.title)
            ys.download(output_path=output_path)
            print("Download complete!")
    
    except Exception as e:
        print(e)

def download_audio(url, output_path):
    try:
        yt = YouTube(url)

        ys = yt.streams.get_audio_only()

        print("Downloading audio: %s" % yt.title)
        ys.download(mp3=True, output_path=output_path)
        print("Download complete!")
    
    except Exception as e:
        print(e)

def main():
    try:
        parser = argparse.ArgumentParser(
            prog='YTDownloader',
            description='Simple YouTube downloader'
        )

        parser.add_argument('-a', '--audio', action='store_true', help='Only download audio')
        parser.add_argument('-r', '--resolution', type=str, help='Select resolution on download', required=False)
        parser.add_argument('-o', '--output', type=str, help='Select directory to download', required=False, default='.')
        parser.add_argument('url', type=str, nargs='?', help='URL of the video')

        args = parser.parse_args()

        url = args.url
        output_path = args.output

        if args.audio:
            download_audio(url, output_path)
        elif args.resolution:
            download_video_selected_resolution(url, args.resolution, output_path)
        else:
            download_video_highest_resolution(url, output_path)
    
    except Exception as e:
        parser.print_help()
        print(e)

if __name__ == "__main__":
    main()
