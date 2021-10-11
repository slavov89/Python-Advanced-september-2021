# def numbers(args):
#     sum_pos = 0
#     sum_neg = 0
#     for el in args:
#         if int(el) > 0:
#             sum_pos += int(el)
#         else:
#             sum_neg += int(el)
#     print(f"{sum_neg}\n{sum_pos}")
#     if abs(sum_neg)>abs(sum_pos):
#         print("The negatives are stronger than the positives")
#     elif abs(sum_pos) > abs(sum_neg):
#         print("The positives are stronger than the negatives")
#
# numbers(input().split())
#

nums = [int(x) for x in input().split()]
sum_pos = sum(filter(lambda x: x > 0, nums))
sum_neg = sum(filter(lambda x: x < 0, nums))

print(f"{sum_neg}\n{sum_pos}")
if abs(sum_neg)>abs(sum_pos):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")






