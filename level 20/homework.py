# n1 დავალება
a = 5
b = 10
sum_ab = a + b
print("The sum of", a, "and", b, "is", sum_ab)

# n2 დავალება
str1 = "Hello"
str2 = "World"

concatenated_str = str1 + " " + str2
print(concatenated_str)

#კონკატენაცია არის ორი სტრინგის ერთად მიერთების პროცესი

#n3 დავალება 
# შექმენით ორი int ტიპის ცვლადი
num1 = 7
num2 = 3

# გამოიტანეთ მათი განაყოფი
quotient = num1 / num2
print("განაყოფი:", quotient)

# ახსნა:
# Python-ში განაყოფის ოპერაციის (/) დროს შედეგი ყოველთვის float ტიპის იქნება.
# მიუხედავად იმისა, რომ ორივე operand არის int ტიპის, Python ავტომატურად ახდენს ტიპის გარდაქმნას.
# ეს ცნობილია როგორც implicit conversion (ავტომატური გარდაქმნა), რადგან Python თვითონ ცდილობს
# ოპერაციის შედეგს მიაწვდოს საჭირო ტიპი, რაც ამ შემთხვევაში არის float <3

# n4 დავალება
a = 5
b = 5
result = (a == b)  # True, რადგან a და b თანასწორია

a = 5
b = 3
result = (a != b)  # True, რადგან a და b არ არის თანასწორი

a = 7
b = 3
result = (a > b)  # True, რადგან a მეტია b-ზე

a = 3
b = 7
result = (a < b)  # True, რადგან a მცირეა b-ზე

