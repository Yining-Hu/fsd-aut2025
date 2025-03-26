class UserController:
    @staticmethod
    def save(user):
        handler = open("./log.txt","a+")
        handler.write(str(user))
        handler.write("\n")
        handler.close()

    @staticmethod
    def read():
        handler = open("./log.txt","r")
        data = handler.readlines()
        lines = []
        for line in data:
            if not(line.isspace()):
                filtered = line.replace("\n","")
                lines.append(filtered)
        return lines