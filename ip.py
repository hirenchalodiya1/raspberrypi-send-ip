import netifaces as ni


def get_ip(interface_name):
    try:
        return ni.ifaddresses(interface_name)[ni.AF_INET][0]['addr']
    except Exception:
        return "None"
