# AIS3 2023 Project : Fuzzing N-day in MiniWeb HTTP Server 

## Author
- 組別 : 軟體安全第六組
    - 黃晴威
        - 逆向 MiniWeb、分析 crash 成因、追蹤原始碼、分析並修補漏洞、負責報告漏洞分析
    - 李玟毅
        - 製作簡報、報告
    - 陳彥凱
        - 製作簡報、報告
    - 林映辰
        - 製作簡報
## 檔案說明
Slides : [AIS3_2023_S6.pdf](https://github.com/qingwei4/AIS3_2023_Project/blob/main/AIS3_2023_S6.pdf)\
MiniWeb binary : [miniweb.exe](https://github.com/qingwei4/AIS3_2023_Project/blob/main/miniweb.exe)\
IDA database : [miniweb.idb](https://github.com/qingwei4/AIS3_2023_Project/blob/main/miniweb.idb)\
PoC : [poc.py](https://github.com/qingwei4/AIS3_2023_Project/blob/main/poc.py)\
fuzzing script : [fuzz.py](https://github.com/qingwei4/AIS3_2023_Project/blob/main/fuzz.py)

## Introduction

We use boofuzz to fuzz Miniweb, which is a HTTP server. After running the fuzzing script for a while, Miniweb crashes. We check the payload, reversed the binary, traced the source code, then found a heap overflow in _mwProcessReadSocket(). After searching some datas, we guess the reason why MiniWeb crashes is CVE-2020-29596. Since MiniWeb is no longer maintained, we make a PR to fix the bug.

## murmur
其他組員都不會 rev/pwn，我負責了所有的技術工作
頭好痛 QQ
