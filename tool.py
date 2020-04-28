import requests


def file_read(file):
        urls = []
        with open(file) as f:

                for line in f:
                        urls.append(line)


                for i in range(0,len(urls)):
                    urls[i]=urls[i].rstrip('\n')




                    if not (urls[i].startswith('www.') or urls[i].startswith('http')):
                        urls[i]='http://'+urls[i]


                    try:
                        response=requests.get(urls[i])

                        if((response.status_code/100)==2 or (response.status_code/100)==3):
                            print('The website',urls[i],'is Active')
                        elif ((response.status_code/100)==4):
                            print('The website ',urls[i],' is Inactive')

                    except requests.ConnectionError:
                        print('The website ',urls[i],' is not Active')


file_read('website.txt')
