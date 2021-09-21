def get_id(message):
    if(message.content[15]=='!'):
      id1 = message.content[16:len(message.content)-1]
    elif(message.content[14]=='@'):
      id1 = message.content[15:len(message.content)-1]
    return id1
