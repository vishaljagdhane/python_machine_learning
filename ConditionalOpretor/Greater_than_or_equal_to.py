print("Greater Than or Equal To Operator चा उपयोग करणारा प्रोग्राम")

# वापरकर्त्याकडून दोन मूल्ये घ्या
value1 = int(input("पहिलं मूल्य टाका: "))
value2 = int(input("दुसरं मूल्य टाका: "))

# जर value1 > value2 असेल
if value1 > value2:
    print(f"{value1} हे {value2} पेक्षा मोठं आहे")  # Greater than

# जर दोन्ही मूल्ये समान असतील
elif value1 == value2:
    print(f"{value1} आणि {value2} ही दोन्ही मूल्ये समान आहेत")  # Equal

# जर value1 < value2 असेल
else:
    print(f"{value1} हे {value2} पेक्षा लहान आहे")  # Less than
