def Features(start="\033[1m", mid="\033[93m", end="\033[0;0m", arrow=" --> "):
    func_dict = {
        "Twitter account analysis": "!twitter @username",
        "URL scan": "!urlscan <URL-TO-SCAN>",
        "File scan": "!filescan <PATH-TO-FILE>",
        "Linux enumeration": "!linuxenum",
        "Linux privilege escalation checker": "!linuxprivchecker",
        "Shellshock": "!shellshock",
        "Mimipenguin (Tool to dump login credentials)": "!mimipenguin"
    }

    for item in func_dict.keys():
        print("{}{}{}{}{}{}".format(start, mid, item, arrow, end, func_dict[item]))
