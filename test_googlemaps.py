
def hey():
    url = "https://maps.googleapis.com/maps/api/directions/json?"

    origin_adress = "202 E White St Champaign IL"
    destination_address = "1010 W Springfield Ave Urbana IL"

    final_request = url+"mode=walking&alternatives=true&"+"origin="
    arr = origin_adress.split(' ')
    arr2 = destination_address.split(' ')



    i = 1
    final_request += arr[0]
    while i < len(arr):
        final_request += "+"+arr[i]
        i+=1

    print(final_request)

    final_request += "destination="

    i = 1
    final_request += arr2[0]
    while i < len(arr2):
        final_request += "+" + arr2[i]
        i += 1

    print(final_request)
    search_
    # i = 0
    # while i < len(origin_adress):
    #     c = origin_adress[i]
    #     if c == ' ':
    #         origin_adress[i] = '+'
    #
    #     i+=1
    #
    # #"202+E+White+St+Champaign+IL&destination=1010+W+Springfield+Ave+Urbana+IL&key=AIzaSyCUV9mE32gI0uU2CpKcYjPXJbXliyTWrKo"
    # print(origin_adress)


def clean_start(self):
    start = self.cleaned_data['start']
    if User.objects.filter(email=email).exists():
        raise ValidationError("Email already exists")

    return email



hey()
