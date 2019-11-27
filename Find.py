#assignments - 14/09/19

#2)print all the names in the below data 
var=""" line 1
line 2
start
deepa
priya
sandy
end
line 3
line4
start
hema
guru
end
line5
start
krishna
vivek
end
line6"""

"""
search_start_pos=0              # searching 'start' word from zero index
search_end_pos=0                # searching 'end' word from zero index
data_start=0                    # taking the defaut 

while data_start != -1:
    data_start=var.find('start',search_start_pos,len(var))
    data_end=var.find('end',search_end_pos,len(var))
    if data_start == -1:
        break;
    data_start += 6
    data_end -= 1
    search_start_pos= data_start
    search_end_pos= data_end + 3
    print(var[data_start:data_end])

"""

c=var.count('start')
pos=0
while (c>0):
    start_pos=var.find('start',pos,len(var))
    end_pos=var.find('end',start_pos,len(var))
    print(var[start_pos+5:end_pos])
