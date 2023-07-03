N = str(input())
data = list()
for i in range(len(N)):
    data.append(N[i])

data.sort(reverse=True)
print(''.join(data))



# N = "1234"
# data = []
# for i in range(len(N)):
#     data.append(N[i])
# print(data)