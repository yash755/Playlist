import requests
from bs4 import BeautifulSoup
import csv

page = 1

while page <= 2201:


    url = "https://thyme.dbbee.com/u/BP05945QON/SPOTIFYPLAYLISTNOV2019qbdsl.wbsp"




    querystring = {"wb_mq":"F","WB_StartRec": str(page)}

    headers = {
        'sec-ch-ua': "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
        'sec-ch-ua-mobile': "?0",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "navigate",
        'sec-fetch-user': "?1",
        'sec-fetch-dest': "iframe",
        'cache-control': "no-cache",
        'postman-token': "10392510-19dc-7940-e732-ec6a6070f8ba"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    html1 = BeautifulSoup(response.content, 'html.parser')

    trs = html1.find_all('tr')

    print (len(trs))

    if len(trs) >= 1:

        for tr in trs:

            playlist_name = ''
            curator = ''
            followers = ''
            gen = ''
            description = ''
            role = ''
            person = ''

            email = ''
            twitter = ''
            website = ''
            profile =''
            facebook = ''
            instagram = ''

            tds= tr.find_all('td')

            try:
                playlist_name = tds[0].text.strip()
            except:
                flag = 1

            try:
                curator = tds[1].text.strip()
            except:
                flag = 1

            try:
                followers = tds[2].text.strip()
            except:
                flag = 1

            try:
                gen = tds[3].text.strip()
            except:
                flag = 1

            try:
                description = tds[4].text.strip()
            except:
                flag = 1

            try:
                role = tds[5].text.strip()
            except:
                flag = 1

            try:
                person = tds[6].text.strip()
            except:
                flag = 1


            try:
                if tr.get('onclick'):

                    url1 = tr.get('onclick')

                    url1 = url1.replace("document.location='//","")
                    url1 = url1.replace("';", "")

                    print (url1)



                    headers = {
                        'sec-ch-ua': "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
                        'sec-ch-ua-mobile': "?0",
                        'upgrade-insecure-requests': "1",
                        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
                        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        'sec-fetch-site': "same-origin",
                        'sec-fetch-mode': "navigate",
                        'sec-fetch-user': "?1",
                        'sec-fetch-dest': "iframe",
                        'cache-control': "no-cache",
                        'postman-token': "18083465-3156-6bfe-bf33-a376e0e4d224"
                    }

                    response1 = requests.request("GET", 'https://' + url1, headers=headers)

                    html2 = BeautifulSoup(response1.content, 'html.parser')

                    trs = html2.find_all('tr')

                    for tr in trs:
                        tr_str = tr.text.strip()

                        if email == '':
                            if 'Email' in tr_str and 'Submissions' not in tr_str:
                                email = tr_str
                                email = email.replace('Email','')
                                email = email.replace('\n', '')

                        if twitter == '':
                            if 'Twitter' in tr_str:
                                twitter = tr_str
                                twitter = twitter.replace('Twitter','')
                                twitter = twitter.replace('\n', '')

                        if website == '':
                            if 'Website' in tr_str:
                                website = tr_str
                                website = website.replace('Website','')
                                website = website.replace('\n', '')

                        if profile == '':
                            if 'Playlist Link' in tr_str:
                                profile = tr_str
                                profile = profile.replace('Playlist Link / Profile Link','')
                                profile = profile.replace('\n', '')

                        if facebook == '':
                            if 'Facebook' in tr_str:
                                facebook = tr_str
                                facebook = facebook.replace('Facebook','')
                                facebook = facebook.replace('\n', '')


                        if instagram == '':
                            if 'Instagram' in tr_str:
                                instagram = tr_str
                                instagram = instagram.replace('Instagram','')
                                instagram = instagram.replace('\n', '')




            except:
                flag =1


            temp = []
            temp.append(playlist_name)
            temp.append(curator)
            temp.append(followers)
            temp.append(gen)
            temp.append(description)
            temp.append(role)
            temp.append(person)

            temp.append(email)
            temp.append(twitter)
            temp.append(website)
            temp.append(profile)
            temp.append(facebook)
            temp.append(instagram)

            print (temp)


            if temp[0] != '':

                arr = []

                arr.append(temp)

                with open('playlist1.csv', 'a+') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerows(arr)

    else:
        file = open('data.txt','a+')
        file.write(str(page) + '\n')
        file.close()



    page = page + 100