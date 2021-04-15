# Python Crash Course, p.43
print('\n')
guest_list = ['oprah winfrey', 'ekhart tolle', 'whitney cummings']
print(guest_list)
off_list = guest_list.pop()
guest_list.append('nikki glasier')
print(f"{off_list.title()} is unable to join us during that date. {guest_list[-1].title()} will join us instead.")
guest_list.insert(0, 'barack obama')
guest_list.insert(2, 'neil brennan')
guest_list.append('andie laguer')
print(guest_list)
print('\n')

print("Oops! I can only invite 2 people to dinner now!")

print(f"My bad {guest_list.pop(0).title()}, I'm sorry I can't invite you to dinner.")

print(f"My bad {guest_list.pop(1).title()}, I'm sorry I can't invite you to dinner.")
# guest_list.pop(5)
print(f"My bad {guest_list.pop(2).title()}, I'm sorry I can't invite you to dinner.")
# guest_list.pop()
print(f"My bad {guest_list.pop().title()}, I'm sorry I can't invite you to dinner.")
print('\n')

message0 = f"You're still invited to my mansion, {guest_list[0].title()}!"
print(message0)
message1 = f"You're still invited to my mansion, {guest_list[1].title()}!"
print(message1)
print('\n')

print(guest_list)
del guest_list[0]
del guest_list[0]
print(guest_list)
