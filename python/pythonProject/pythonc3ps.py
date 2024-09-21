numbers = [122, 121, 13, 18, 19, 22, 66, 21, 23, 25, 34]
counter = 0
while counter <len(numbers) :
    print("this are the list of number's going:")
    print(numbers[counter])
    counter = counter +1

numbers = [122, 121, 13, 18, 19, 22, 66, 21, 23, 25, 34]
counter = 0
sum_of_numbers = 0
while counter < len(numbers):
    sum_of_numbers = sum_of_numbers+ numbers[counter]
    print(sum_of_numbers)
    avg_no = sum_of_numbers/len(numbers)
    print(avg_no)
    counter = counter +1

    print([i.lower() for i in "HELLO"])

    name = list("GuviGeek")

    i = 0;

    temp = ''

    name1 = ''

    m = (len(name) // 2) - 1

    for j in range(len(name) - 1, m, -1):

    if (i < j):

    temp = name[i]

    name[i] = name[j]

    name[j] = temp

    i += 1

    name1 = "".join(name)

    print(name1[::-1])

list1=[1,0,1,0,0,1]

list2=[23,45,78,99,88,32]

j=0

for i in range(len(list1)):

  if(list1[i]==1):

    num=list2[j]

    sum=0

    rem=0

    while(num>0):

      rem=num%10

      sum=sum*10+rem

      num=num//10

    list2[i]=sum

  j=j+1

print(list2)








