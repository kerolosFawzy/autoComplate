
def get_input(str):
    class_key = 'class'
    attr_key = 'attr'
    dict = {}

    if "." in str:
        getclass, getattr = str.strip('\r\n').split('.')
        # print type(getattr)
        dict[class_key] = getclass
        dict[attr_key] = getattr
    # if dict.has_key(class_key) and dict.has_key(attr_key) :
    #    print dict.get(class_key) + dict.get(attr_key)
    else:
        getclass = str
        dict[class_key] = getclass
        dict[attr_key] = "none"
    # if dict.has_key(class_key) and dict[attr_key]=="none":
    #     print dict.get(class_key)+dict.get(attr_key)
    return dict
