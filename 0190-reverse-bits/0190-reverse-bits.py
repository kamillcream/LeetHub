class Solution:
    def reverseBits(self, n, bits=32):
        if bits == 1:
            return n
        
        left = n >> (bits // 2) # 왼쪽 추출, bits // 2만큼 오른쪽으로 이동하므로 오른쪽 절반이 사라짐.
        right = n & ((1 << (bits // 2)) - 1) # 오른쪽 추출, 해당 길이만큼 1을 생성 후 -1을 하면 모든 비트가 1이
        return (self.reverseBits(right, bits // 2) << (bits // 2) | self.reverseBits(left, bits // 2))