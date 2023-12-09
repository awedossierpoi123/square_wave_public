# square_wave_public
1. Pythonをダウンロードしてください。Install Python from here: https://www.python.org/downloads/windows/
2. Python.exeをパスを環境変数に設定してください。Make sure to add python.exe to PATH.
3. レポジトリ全体をCode->Download ZIPとクリックしダウンロードしてください。Download all files in this repository by clicking on Code->Download ZIP.
4. ダウンロードしたZIPフォルダを展開してください。Unzip the zip folder you downloaded.
5. 展開後のフォルダのディレクトリ上でコマンドプロンプトを起動してください。Open command prompt. Make sure the current path is under the directory of folder which was unzipped.
6. pip3 install matplotlibと入力し、matplotlibをインストールしてください。Input pip3 install matplotlib on command prompt. Matplotlib would be installed on your computer.
7. python seq.pyと入力すると、シーケンスが出力されます。Input python seq.py on command prompt. Sequence file would be exported to the current directory.

## seq.pyの使用方法

1. seq = SEQ(total_row_num, pulse_height, cycletime)でシーケンスの初期化を行います。total_row_numは何種類のパルスを使用するか指定します。cycletimeは1周期の時間です。
2. seq.draw_freq_pulse(start, end, freq, row_num, name)で高周波パルスを出力します。startは開始時間、endは終了時間、row_numはパルスを出力する位置、nameは名前です。freqは周波数をkHzで指定しますが、縦線の間隔を変えるのに使用してもOKです。
3. seq.draw_pulse()で通常のパルスを出力します。
4. seq.draw_arrow()で矢印を出力します。
5. seq.draw_gapline(x)で間隔を出力します。
6. seq.finalize(filename)でシーケンスの決定とGUIかつファイル出力を行います。filenameでファイル名を設定します。

## seq_precise.pyについて About seq_precise.py

seq_precise.pyはシーケンスの詳細構造を出力するpyファイルです。
https://doi.org/10.1063/5.0065975 に記載されているようなシーケンスを出力可能です。

seq_precise.py can output sequence data as well, but its output would be similar to https://doi.org/10.1063/5.0065975.
