<link href="./IchigoJamFont.css" rel="stylesheet"></link>

<iyn>
ICHIGOJAM BASIC
イチゴジャムベーシック
</iyn>

## FILE0 INIT

<pre><code><iyn>
10 @ARUN:CLV:'2022.5.7
15 G=#800:L=#8BC:M=#8C5:P=#7FE:Q=#8CA
20 POKE#800,3,93,149,6,51,83,9,27,146,12,21,128,15,18,66,0,0,165,0,0,164,0,24,18,0,0,163,30,39,2,33,36,49,0,0,52,0,0,97,42,48,68,45,0,147,0,0,149,0,0,162
30 POKE#833,54,75,1,57,66,64,60,63,16,0,0,4,0,0,113,69,72,132,0,0,145,0,0,51,78,84,112,81,186,50,0,0,115,87,90,148,0,0,35,0,0,161,96,141,98,99,120,48
40 POKE#863,102,111,84,105,108,80,0,0,166,0,0,99,114,117,96,0,0,100,0,0,114,123,132,144,126,129,65,0,0,17,0,0,32,135,138,19,0,0,130,0,0,3,144,165,116
50 POKE#890,147,156,129,150,153,82,0,0,167,0,0,81,159,162,67,0,0,33,0,0,0,168,177,131,171,174,36,0,0,168,0,0,34,180,183,20,0,0,169,0,0,160,0,0,150
60 POKEL,0,#6B,#73,#74,#6E,#68,#6D,#79,#72
70 POKEM,#61,#69,#75,#65,#6F
80 COPY#700,#A6*8,8:COPY#708,#3F*8,8:COPY#710,#B0*8,8
90 A="horeto-ku ":GSB110
100 A="shokika kanryou simasita.":GSB110:GOTO200
110 B=I2CW(46,A,LEN(A))&(I2CW(46,13))
120 B=I2CR(46,#8CA,1):IFPEEK(#8CA)<>62CONTELSERTN
200 VIDEO3:?"HORE TALK START!"
210 LRUN1
</iyn></code></pre>


## FILE1 MAIN

<pre><code><iyn>
10 'ホレトークMAIN 2022.5.7
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
210 K=(I&lt7)*(I*5+J+#B1)+(I=7)*(#D4+J/2)+(I=8)*(#D7+J)+(I=9)*(#DC+J)+(I=10)*(#30+J):?" ";CHR$(K)
220 F=0
230 IFI&lt9POKEP,PEEK(L+I),PEEK(M+J)
240 IF(I=9)*((J=0)+(J=4))POKEP,#77,PEEK(M+J)
241 IF(I=9)*(J=1)POKEP,#6E,#6E
250 IF(I=9)*(J=2)N=PEEK(P):POKEP,(N=1)*#67+(N=2)*#7A+(N=3)*#64+(N=5)*#62
260 IF(I=9)*(J=3)POKEP,#70
270 IFI=10POKEP,J+48,0
280 O=I2CR(46,Q,1):IFPEEK(Q)<>62CONT
290 O=I2CW(46,P,2)&I2CW(46,13)
300 RTN
</iyn></code></pre>
