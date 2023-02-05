marks=0
red=['apple', 'strawberry', 'cherry', 'watermelon', 'pomogrenate', 'tomato']
green=['avacado', 'greenapple', 'custardapple', 'greengrapes','kiwi']
blue=['blueberry', 'blackberry', 'plum','bluetomato']
ans1 = str(input("Enter a fruit which is red in color: "))
for x in red:
    if(x==ans1.lower()):
        marks+=1
ans2 = str(input("Enter a fruit which is green in color: "))
for x in green:
    if(x==ans2.lower()):
        marks+=1
ans3 = str(input("Enter a fruit which is blue in color: "))
for x in blue:
    if(x==ans3.lower()):
        marks+=1
print("Your awarded marks are: ", marks)


