# # given an aray, rotate the array to the right by k steps , where k is a non negative. implement the rotation in place with O(1) extra space
# def rotate_right(lst, k):
#     k %= len(lst)              # handle k > len
#     return lst[-k:] + lst[:-k]
def rri(lst, k): #rotate_right_inplace
    n = len(lst)
    k %= n

    def reverse(l, r):
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

a = [1,2,3,4,5,6,7,8,9,0]
print(a)
rri(a, 5)
print(a)