cookies={"탱커":"우유맛쿠키","딜러":"칠리맛쿠키","힐러":"천사맛쿠키","서포터":"석류맛쿠키"}
print("바꾸기 전 cookies : ",cookies)

if("탱커" in cookies):
    cookies["탱커"]="다크초코맛쿠키"

if("딜러" in cookies):
    cookies["딜러"]="라떼맛쿠키"

if("힐러" in cookies):
    cookies["힐러"]="허브맛쿠키"

print("바꾼 후 cookies : ",cookies)