#learnt4
#must include : min(), max(), round(), sum(), all(), break, continue

numbers = [1,2,3,4,5]
print("\nnumbers_1 :", numbers)
print("최솟값 :", min(numbers))
print("최댓값 :", max(numbers))
print("모든 수의 합 :", sum(numbers))
print("모두 양수인가? :", all(numbers))

numbers = [5.1, 0.95, 0.3814, 4.1, -1, 2]
print("\nnumbers_2 : ", numbers, "\n")
for i in range(len(numbers)):
   print(">>Index : %d" %i)
   print("current number : ", numbers[i])
   if (numbers[i]<0):
      print("음수를 만나면 프로그램을 종료합니다.\n")
      break
   elif (round(numbers[i])==0):
      print("이 값은 소숫점 아래 값을 반올림하면 0이 됩니다.\n")
      continue
   else:
      print("소숫점 아래 값 반올림 : %d\n" %round(numbers[i]))


