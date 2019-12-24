import requests
import re
import urllib

query = [False, '', False, False, False]

def get_page(link):
    response = requests.get(link)
    print (response.status_code)
    #print ( re.findall(".id=\"name\w+" ,response.content.decode('utf-8')) )
    for download_link in re.findall(".id=\"name\w+" ,response.content.decode('utf-8')):
        #testfile = urllib.urlopen()
        #testfile.retrieve('https://www.opensubtitles.org/en/subtitleserve/sub/'+re.findall('\d+', download_link )[0], "file.zip")
        page_link = 'https://www.opensubtitles.org/en/subtitles/'+re.findall('\d+', download_link )[0]
        response2 = requests.get(page_link, headers={'referer': page_link})
        link_id = re.findall(".download\/file\/(.*?)\"" ,response2.content.decode('utf-8'))[0]
        srt_link = 'http://dl.opensubtitles.org/en/download/file/' + link_id
        r = requests.get(srt_link, headers={'referer': page_link})
        print(srt_link)
        with open(query[1]+'-'+query[2]+'-'+query[3]+'-'+query[4]+'-'+link_id+'.srt', 'wb') as f:
            f.write(r.content)

def get_querylink():
    if query[0] == "movie":
        return 'https://www.opensubtitles.org/en/search2/sublanguageid-'+ query[4] +'/searchonlymovies-on/moviename-'+ query[1]
    elif query[0] == "serie":
        get_page('https://www.opensubtitles.org/en/search/sublanguageid-'+ query[4] +'/searchonlytvseries-on/season-'+ query[2] +'/episode-'+ query[3] +'/moviename-'+ query[1])
        return 'https://www.opensubtitles.org/en/search/sublanguageid-'+ query[4] +'/searchonlytvseries-on/season-'+ query[2] +'/episode-'+ query[3] +'/moviename-'+ query[1]
    else:
        print('defs')
        set_query()
        pass

def set_query(type,name,season,episode,lang):
    if type == "serie":
        query[0] = type
        query[1] = name.replace(' ', '+')
        query[2] = season
        query[3] = episode
        query[4] = lang
        get_querylink()
        pass
    else:
        query[0] = type
        query[1] = name.replace(' ', '+')
        query[2] = season
        query[3] = episode
        query[4] = lang
        get_querylink()
        pass



# .id=\"name\w+ https://www.opensubtitles.org/en/search/sublanguageid-tur/season-1/episode-1/moviename-young+justice
