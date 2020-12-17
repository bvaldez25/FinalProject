""""
The Program is trying to determine which zodiac sign the user is.
Based on the input the user enters, it will determine the zodiac sign.
The user will first enter the day they were born.
Second the user will enter the month they were born.
Finally based on those inputs, the program will determine what zodiac sign the user is.

If the user is born in December the output will display Sagittarius if the day is before 22 else output will be Capricorn.
If the user is born in January the output will display Capricorn if the day is before 20 else output will be Aquarius.
If the user is born in February the output will display Aquarius if the day is before 19 else output will be Pisces.
If the user is born in March the output will display Pisces if the day is before 21 else output will be Aries.
If the user is born in April the output will display Aries if the day is before 20 else output will be Taurus.
If the user is born in May the output will display Taurus if the day is before 21 else output will be Gemini.
If the user is born in June the output will display Gemini if the day is before 21 else output will be Cancer.
If the user is born in July the output will display Cancer if the day is before 23 else output will be Leo.
If the user is born in August the ouput will display Leo if the day is before 23 else output will be Virgo.
If the user is born in September the output will display Virgo if the day is before 23 else output will be Libra.
If the user is born in October the output will display Libra if the day is before 23 else the output will be Scorpio.
If the user is born in November the output will display Scorpio if the day is before 22 else the output will be Sagittarius. 
"""

"""
day = input brithday
month = input month of birth

If month = December
    "Sagitarius" if day < 22 else "Capricorn"
elif month = January
    "Capricorn" if day < 20 else "Aquarius"
elif month = February
    "Aquarius" if day < 19 else "Pisces"
elif month = March
    "Pisces" if day < 21 else "Aries"
elif month = April
    "Aries" if day < 20 else "Taurus"
elif month = May
    "Taurus" if day < 21 else "Gemini"
elif month = June
    "Gemini" if day < 21 else "Cancer"
elif month = July
    "Cancer" if day < 23 else "Leo"
elif month = August
    "Leo" if day < 23 else "Virgo"
elif month = September
    "Virgo" if day < 23 else "Libra"
elif month = October
    "Libra" if day < 23 else "Scorpio"
elif month = November 
    "Scorpio" if day < 22 else "Sagittarius"

Print "Your Astrological sign is....."
"""

day = int(input("Input birthday: "))
month = input("Input month of birth: ")
if month == "December":
	astro_sign = "Sagittarius" if (day < 22) else "Capricorn"
elif month == "January":
	astro_sign = "Capricorn" if (day < 20) else "Aquarius"
elif month == "February":
	astro_sign = "Aquarius" if (day < 19) else "Pisces"
elif month == "March":
	astro_sign = "Pisces" if (day < 21) else "Aries"
elif month == "April":
	astro_sign = "Aries" if (day < 20) else "Taurus"
elif month == "May":
	astro_sign = "Taurus" if (day < 21) else "Gemini"
elif month == "June":
	astro_sign = "Gemini" if (day < 21) else "Cancer"
elif month == "July":
	astro_sign = "Cancer" if (day < 23) else "Leo"
elif month == "August":
	astro_sign = "Leo" if (day < 23) else "Virgo"
elif month == "September":
	astro_sign = 'Virgo' if (day < 23) else "Libra"
elif month == "October":
	astro_sign = "Libra" if (day < 23) else "Scorpio"
elif month == "November":
	astro_sign = "Scorpio" if (day < 22) else "Sagittarius"
print("Your Astrological sign is :",astro_sign)
