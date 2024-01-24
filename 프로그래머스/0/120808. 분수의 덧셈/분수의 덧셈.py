def solution(numer1, denom1, numer2, denom2):
    mul_numer = numer1*denom2 + numer2*denom1
    mul_denom = denom1*denom2

    common_mulple = []

    for i in range(1, min(mul_numer, mul_denom)+1):
        if mul_numer%i == 0 and mul_denom%i == 0:
            common_mulple.append(i)        
        else:
            i = i+1

    return [int(mul_numer/max(common_mulple)), int(mul_denom/max(common_mulple))]
# keyword = 최대 공배수