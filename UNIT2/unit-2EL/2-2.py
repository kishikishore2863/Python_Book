# A membership class keeps a standard discount for all members.
# A class method is used to revise this discount.
# you are asked to apply the new discount and show ts impact on two purchases.


# class Membership:
#     discount=10
#     def __init__(self,member_id,member_name):
#         self.member_id = member_id
#         self.member_name = member_name
#
#     @classmethod
#     def revise(cls,new_discount):
#         cls.discount = new_discount
#
#
# def final_price(amount):
#     return amount - (amount * Membership.discount/100)
#
#
# m1 = Membership(1,"kishore")
# m2 = Membership(2,"kane")
#
# print("Before revising discount:")
# print("Purchase 1 final :",final_price(1000))
# print("Purchase 1 final :",final_price(2000))
#
# Membership.revise(20)
#
# print("After revising discount:")
# print("Purchase 1 final :",final_price(1000))
# print("Purchase 1 final :",final_price(2000))



class Mebership:
    discount
