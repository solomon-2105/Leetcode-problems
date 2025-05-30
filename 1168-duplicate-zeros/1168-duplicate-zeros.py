class Solution:
    def duplicateZeros(self, arr):
        flag = 0
        zoffset = 10
        nzoffset = 100
        n = len(arr)
        zp = nzp = 0

        while zp < n:
            val = arr[nzp]
            if flag == 1:
                val = (arr[nzp] % nzoffset) // zoffset
            if val == 0:
                arr[zp] = (arr[nzp] % nzoffset) * nzoffset + arr[zp] * zoffset
                flag = 1
                zp += 1
            if flag == 1 and zp < n:
                arr[zp] = val * nzoffset + arr[zp] * zoffset
            zp += 1
            nzp += 1

        for i in range(n):
            if arr[i] >= zoffset:
                arr[i] = (arr[i] // nzoffset) % zoffset