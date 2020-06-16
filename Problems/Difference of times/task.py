# put your python code here
hours_first = int(input())
minutes_first = int(input())
seconds_first = int(input())

hours_second = int(input())
minutes_second = int(input())
seconds_second = int(input())

result = abs(
        (hours_first * 3600 + minutes_first * 60 + seconds_first) - (
                hours_second * 3600 + minutes_second *60 + seconds_second
        ))
print(result)