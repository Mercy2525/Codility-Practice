
msg='welcome to Python 101: Strings'
#1 Welcome Ring To Tyler

new=msg[18]+' '+msg[0:7]+''+msg[7:10]+msg[7:9]+msg[12]+msg[2]+msg[1]+msg[25]
print(new.title())
print(new[::-1].title())

print(msg.find('to'))


friends=['Mary','Abel','John']
#friends.sort(reverse=True)
# friends.reverse()
# friends.pop(1)
new_fr=friends.copy()

print(friends)