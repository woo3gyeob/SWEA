'''
import sys
sys.stdin = open('input.txt', r)
하면 input.txt 파일의 내용을 불러올 수 있다
r : read mode (읽기 모드)

'''

for test_case_num in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    building_on_view = 0
    for i in range(len(building)):
        if i == 0:
            cnt1 = building[i] - building[i+1]
            cnt2 = building[i] - building[i+2]
            if cnt1 > 0 and cnt2 > 0:
                if cnt1 > cnt2:
                    building_on_view += cnt2
                else:
                    building_on_view += cnt1
        elif i == 1:
            cnt1 = building[i] - building[i-1]
            cnt2 = building[i] - building[i+1]
            cnt3 = building[i] - building[i+2]
            if cnt1 > 0 and cnt2 > 0 and cnt3 > 0:
                if cnt1 <= cnt2 and cnt1 <= cnt3:
                    building_on_view += cnt1
                elif cnt2 <= cnt1 and cnt2 <= cnt3:
                    building_on_view += cnt2
                else:
                    building_on_view += cnt3
        elif i == (len(building)-2):
            cnt1 = building[i] - building[i-2]
            cnt2 = building[i] - building[i-1]
            cnt3 = building[i] - building[i+1]
            if cnt1 > 0 and cnt2 > 0 and cnt3 > 0:
                if cnt1 <= cnt2 and cnt1 <= cnt3:
                    building_on_view += cnt1
                elif cnt2 <= cnt1 and cnt2 <= cnt3:
                    building_on_view += cnt2
                else:
                    building_on_view += cnt3
        elif i == (len(building)-1):
            cnt1 = building[i] - building[i-1]
            cnt2 = building[i] - building[i-2]
            if cnt1 > 0 and cnt2 > 0:
                if cnt1 > cnt2:
                    building_on_view += cnt2
                else:
                    building_on_view += cnt1
        else:
            cnt1 = building[i] - building[i-2]
            cnt2 = building[i] - building[i-1]
            cnt3 = building[i] - building[i+1]
            cnt4 = building[i] - building[i+2]
            if cnt1 > 0 and cnt2 > 0 and cnt3 > 0 and cnt4 > 0:
                if cnt1 <= cnt2 and cnt1 <= cnt3 and cnt1 <= cnt4:
                    building_on_view += cnt1
                elif cnt2 <= cnt1 and cnt2 <= cnt3 and cnt2 <= cnt4:
                    building_on_view += cnt2
                elif cnt3 <= cnt1 and cnt3 <= cnt2 and cnt3 <= cnt4:
                    building_on_view += cnt3
                else:
                    building_on_view += cnt4
    print('#%d'%test_case_num, building_on_view)