@font-face
{
    font-family: "ichigojam";
    font-style: normal;
    font-weight: 400;
    src: local('IchigoJam-1.4'), local('IchigoJam-1.4-Regular'),
         url("https://cdn.jsdelivr.net/gh/fu-sen/ichigojam-font@20190814/IchigoJam-1.4.woff") format('woff');
}

## FILE0 INIT

```"ichigojam"
1 'ｱﾝｺﾞｳｻｸｾｲ2022.5.7
20 SRND TICK():CLV:CLS
30 POKE #1003,1,34
40 INPUT "INPUT MESSAGE : ",A
50 IF LEN(A)<1 END
60 ? "ｱﾝｺﾞｳ : ";
70 FOR B=0 TO LEN(A)-1
80 C=RND(10)
90 D=PEEK(A+B)files
100 IF C+D>223 C=223-D
110 ? CHR$(C+D);C;
120 NEXT
130 ?
```

## FILE1 MAIN

```ichigojam
10 '���-�MAIN 2022.5.7
20 A=!IN(3)
30 C=C+A*B
40 IF(B=0)*(A=1)C=0:D=0:BEEP0:PLAY"O5A4"
50 IF(B=1)*(A=0)E=C>8:PLAY:?CHR$(165+E*11);:GSB100
60 D=D+(B=0)*(A=0)
70 IFD>30D=0:IFFGSB200
80 B=A
90 GOTO20
100 F=PEEK(E+F+G)
110 IFF=0?"ERROR"
120 RTN
200 H=PEEK(F+2+G):I=H/16:J=H&15
210 K=(I<7)*(I*5+J+#B1)+(I=7)*(#D4+J/2)+(I=8)*(#D7+J)+(I=9)*(#DC+J)+(I=10)*(#30+J):?" ";CHR$(K)
220 F=0
230 IFI<9POKEP,PEEK(L+I),PEEK(M+J)
240 IF(I=9)*((J=0)+(J=4))POKEP,#77,PEEK(M+J)
241 IF(I=9)*(J=1)POKEP,#6E,#6E
250 IF(I=9)*(J=2)N=PEEK(P):POKEP,(N=1)*#67+(N=2)*#7A+(N=3)*#64+(N=5)*#62
260 IF(I=9)*(J=3)POKEP,#70
270 IFI=10POKEP,J+48,0
280 O=I2CR(46,Q,1):IFPEEK(Q)<>62CONT
290 O=I2CW(46,P,2)&I2CW(46,13)
300 RTN
```
