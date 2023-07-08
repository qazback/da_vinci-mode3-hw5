import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe.*?src="(https?://(?:www\.)?youtube\.com/embed/.*?)".*?>'
    match = re.search(pattern, s)
    if match:
        youtube_url = match.group(1)
        youtu_be_url = youtube_url.replace("youtube.com", "youtu.be")
        return youtu_be_url
    return None


if __name__ == "__main__":
    main()
