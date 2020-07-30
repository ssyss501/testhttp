import requests
import json
import time


def geturl():
    url = "https://api3-core-c-hl.amemv.com/aweme/v1/nearby/feed/?max_cursor=0&min_cursor=0&count=20&feed_style=1&filter_warn=0&city=210200&latitude&longitude&poi_class_code=0&pull_type=1&location_permission=1&nearby_distance=0&roam_city_name&insert_fresh_aweme_ids&insert_fresh_type=0&os_api=22&device_type=OPPO%20R11&ssmix=a&manifest_version_code=110901&dpi=160&uuid=866174014282715&app_name=aweme&version_name=11.9.0&ts=1595318127&cpu_support64=false&storage_type=0&app_type=normal&ac=wifi&host_abi=armeabi-v7a&update_version_code=11909900&channel=tengxun_new&_rticket=1595318126741&device_platform=android&iid=333845288721831&version_code=110900&mac_address=1C%3A1B%3A0D%3A88%3ACF%3AC9&cdid=da994551-50c1-4052-8780-10b4798ae323&openudid=741c1b0d88cfc947&device_id=68494640557&resolution=540*960&os_version=5.1.1&language=zh&device_brand=OPPO%20&aid=1128&mcc_mnc=46000"
    header = {
        "Host": "api3-core-c-hl.amemv.com",
        "Connection": "keep-alive",
        "Cookie": "install_id=333845288721831; ttreq=1$b57aca1655897e3f4cd650f233fec99ebe52f6c4; odin_tt=269c935412fd5c5fce9873783b092fb3184c24f5c269f2c3d42acbeaac384bade0ceab5087eb49d66b51e35b9ae53f72ff5f12ef4d1479bf1eaa20b3e3c2de18",
        "X-SS-REQ-TICKET": "1595318126731",
        "passport-sdk-version": "17",
        "sdk-version": "2",
        "X-SS-DP": "1128",
        "x-tt-trace-id": "00-705eca0d09ff29945adc19310a090468-705eca0d09ff2994-01",
        "User-Agent": "com.ss.android.ugc.aweme/110901 (Linux; U; Android 5.1.1; zh_CN; OPPO R11; Build/NMF26X; Cronet/TTNetVersion:71e8fd11 2020-06-10 QuicVersion:7aee791b 2020-06-05)",
        "Accept-Encoding": "gzip, deflate",
        "X-Gorgon": "0404d01f4001d7755b2e12fea288a76d09503f76493068e1491e",
        "X-Khronos": "1595318126"
    }

    print("aa")
    try:
        requests.keep_alive = False
        ret = requests.get(url, headers=header)

        user_dic = json.loads(ret.text)

        videoCount = len(user_dic['aweme_list'])
        aweme_list = user_dic['aweme_list']
        for i in range(0, videoCount):
            if aweme_list[i].__contains__('video'):
                videourl = aweme_list[i]['video']['download_addr']['url_list'][0]
                print(videourl)
                with open("d:\\url.txt", 'a+') as ff:
                    ff.write(videourl + '\n')
    except Exception as e:
        print(e)
        print("本次发生异常!")


if __name__ == '__main__':
    while True:
        geturl()
        time.sleep(5)

#按按