"""
Name: byroncbr_11.py
Author: bangrenc
Time: 5/7/2020 3:39 PM
"""

def maxArea(height):
    length = len(height)
    f = 0
    l = length
    m_area = 0

    for i in range(length):
        if height[f] > height[l-1]:
            area = (length-i-1) * height[l-1]
            l = l - 1

        else:
            area = (length-i-1) * height[f]
            f = f + 1

        if area > m_area:
            m_area = area

    return m_area

if __name__ == '__main__':
    test = [1,8,6,2,5,4,8,3,7]
    result = maxArea(test)
    print(result)


