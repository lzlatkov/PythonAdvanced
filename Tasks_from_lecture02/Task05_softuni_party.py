numbers_of_guests = int(input())
reservation_codes = set()

for _ in range(numbers_of_guests):
    reservation_code = input()
    reservation_codes.add(reservation_code)

guest = input()

while guest != "END":
    if guest in reservation_codes:
        reservation_codes.remove(guest)
    guest = input()

print(len(reservation_codes))

for guest in sorted(reservation_codes):
    print(guest)