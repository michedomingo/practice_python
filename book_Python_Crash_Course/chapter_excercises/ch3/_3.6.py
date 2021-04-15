# Python Crash Course, p.42
print('\n')
guest_list = ['oprah winfrey', 'ekhart tolle', 'whitney cummings']
print(guest_list)
off_list = guest_list.pop()
guest_list.append('nikki glasier')
print(f"{off_list.title()} is unable to join us during that date. {guest_list[-1].title()} will join us instead.")
guest_list.insert(0, 'barack obama')
guest_list.insert(2, 'neil brennan')
guest_list.append('andie laguer')

print('\n')

message0 = f"You're invited to my mansion, {guest_list[0].title()}!"
print(message0)
message1 = f"You're invited to my mansion, {guest_list[1].title()}!"
print(message1)
message2 = f"You're invited to my mansion, {guest_list[2].title()}!"
print(message2)
message3 = f"You're invited to my mansion, {guest_list[3].title()}!"
print(message3)
message4 = f"You're invited to my mansion, {guest_list[4].title()}!"
print(message4)
message5 = f"You're invited to my mansion, {guest_list[5].title()}!"
print(message5)
