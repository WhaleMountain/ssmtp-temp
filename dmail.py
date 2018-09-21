import base64

def setTo():
    return input("To:")

def setFrom():
    return input("From:")

def setSubject():
    return input("Subject:")

def setText():
    return input("Text:")

def setTemp():
    judge = input("Is there an attached file(yes or no):")
    if judge == "yes":
        filename = input("File name:")
        return tempEncode(filename)
    return ""

def tempEncode(filename):
    with open(filename,"rb") as f:
        origin = f.read()
        temp = base64.b64encode(origin)
    return temp

def setMail(To,From,Subject,Text,Temp):
    with open("dmail","w") as f:
        f.write("To:"+To+"\n")
        f.write("From:"+From+"\n")
        f.write("Subject:"+Subject+"\n")
        if Text != "":
            f.write(Text)
        if Temp != "":
            f.write("\n\n")
            f.write(str(Temp))


if __name__ == "__main__":
    while True:
        To = setTo()
        if To == "":
            print("'To:' has not been entered!!")
            continue
        else: break

    while True:
        From = setFrom()
        if From == "":
            print("'From:' has not been entered!!")
            continue
        else: break

    Subject = setSubject()
    Text = setText()
    Temp = setTemp()

    setMail(To,From,Subject,Text,Temp)