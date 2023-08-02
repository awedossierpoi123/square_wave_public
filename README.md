# square_wave_public

## 初期設定
1. まず、Pythonをダウンロードしてください。 First, download Python from here: https://www.python.org/downloads/windows/
2. ダウンロードしたインストーラーの命令に沿って設定を進めますが、"ADD Python x.x to PATH"の所は絶対チェックするようにしてください。 Start the installer that you have downloaded, but make sure to click on a box that says "ADD Python x.x to PATH".
3. 終了したら、コマンドプロンプトを開始してください。 Click on command prompt.
4. コマンドプロンプトに "pip3 install matplotlib" と入力してライブラリをダウンロードしてください。 Enter "pip3 install matplotlib" on command prompt.
5. コマンドプロンプトに "python seq.py"と入力することで、パターンを出力することができます。 "python seq.py" would output pattern.

## 使用方法
seq.pyの
if __name__ == "__main__": より前の行は無視してください。

seq = SEQ(total_row_num=3, pulse_height=10, cycletime=5)
ここでは、何種類のパルスを使用するのか、パルスの高さ、サイクルタイムを設定します。
ターゲット1+ターゲット2+酸素であれば、total_row_numは3となります。

seq.draw_freq_pulse(start=0.8, end=1.8, freq=10, row_num=2, name="metal 1")
ここでは、周波数を表現したパルスを設定します。
startはパルス開始sec, endは終了sec, freqは周波数(kHz), row_numは何行目にパルスを置くかです。
row_numを0に設定した場合、y軸に対して一番下に置かれます。row_numはtotal_row_num-1を最大値にとるようにしてください。

seq.draw_pulse(start=4.3, end=5, row_num=0, name="$O_{2}$")
ここでは、通常のパルスを設定します。

seq.draw_arrow(start=0, end=0.8, row_num=2)
<->矢印を設定します。start秒からend秒までが長さとなります。
row_numは何行目に矢印を置くか設定できます。

seq.draw_gapline(0.8)
点線を引きます。0.8秒目にy軸に対して平行な線を引きます。

seq.finalize("pattern1.pdf")
最後に、ファイル出力とGUI出力を行います。
上の例だとpattern1.pdfにファイル出力されます。
