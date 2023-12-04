from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as patches
# CLASS

font_size = 12
small_font_size = 7

class SEQ:

    def __init__(self, total_row_num, cycletime):
        plt.rcParams.update({'mathtext.default': 'regular', 'font.size' : font_size})
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

        self.total_row_num = total_row_num
        self.pulse_height = 10
        self.cycletime = cycletime
        self.offset = 5
        self.ax.set_xlim(xmin=0, xmax=self.cycletime)
        self.ax.set_ylim(ymin=0, ymax=self.offset+2 *
                         self.total_row_num*self.pulse_height)
        self.ax.set_xlabel("seconds [sec]")
        #self.ax.set_xlabel("Process time [sec]")
        self.ax.set_xticklabels([])
        self.ax.set_yticks([])

    def draw_arrow(self, start, end, row_num):
        base_y = self.offset + self.pulse_height*row_num*2+self.pulse_height
        # self.ax.arrow(start, base_y+2.5, end-start, 0, width=0.1, head_width=2,head_length=0.2, length_includes_head=True, color='k')
        self.ax.text(x=(start+end)/2, y=base_y+2.5, s="{0} s".format("%.1f" % (end-start)), horizontalalignment='center')
        
        self.ax.annotate(text='', xy=(end, base_y),
                         xytext=(start, base_y), arrowprops=dict(arrowstyle='<->', color='black'))
        
    def draw_gapline(self, x):
        self.ax.vlines(x, self.offset, self.offset+2*self.total_row_num*self.pulse_height, 
                       color="black", linestyles='dotted', linewidth=0.5)
        
    def trigger(self, x, name):
        y = self.ax.get_ylim()[1]
        self.ax.annotate(text="", xy=(x, y),
                         xytext=(x, y+10), annotation_clip=False, arrowprops=dict(arrowstyle='->', color='black'))
        
        self.ax.text((x-2.5), y+5, s="{0} s\n{1}".format(x,name), fontsize=10.5, verticalalignment="center")
        #self.ax.text(x-5, y+5, s="{0} s\n{1}".format(x,name), fontsize=10.5, verticalalignment="center")
        #self.ax.text(x-4, y+5, s="{0} s\n{1}".format(x,name), fontsize=25, verticalalignment="center")

    def draw_freq_pulse(self, start, end, freq, row_num, name, color="black"):

        base_y = self.offset + self.pulse_height*row_num*2

        x=(start+end)/2
        y=base_y+self.pulse_height+3

        
        self.ax.text(x=x, y=y, s="{0} s".format(
            "%.1f" % (end-start)), horizontalalignment='center')
        
        #xdisplay, ydisplay = self.ax.transData.transform((0,base_y+self.pulse_height*0.5))
        #xdisplay_text = xdisplay - 50
        #ydisplay_text= ydisplay

        #self.ax.text(xdisplay_text, ydisplay_text, name, transform=self.fig.get_transform())
        self.ax.text(x=-self.cycletime*0.1, y=base_y+self.pulse_height*0.5, s=name, verticalalignment="center")

        self.ax.hlines(base_y, 0, self.cycletime, color="black", linewidth=0.5)

        for i in np.arange(start, end, 1/(freq*5)):
            # plt.plot([i, i], [base_y, base_y+self.pulse_height])
            #self.ax.plot([i, i], [base_y, base_y+self.pulse_height], color="black", linewidth=1)
            self.ax.vlines(i, base_y, base_y+self.pulse_height, color=color, linewidth=0.5)

    def draw_freq_pulse_notime(self, start, end, freq, row_num, name, color="black"):

        base_y = self.offset + self.pulse_height*row_num*2

        x=(start+end)/2
        y=base_y+self.pulse_height+3

        
        #self.ax.text(x=x, y=y, s="{0} s".format("%.1f" % (end-start)), horizontalalignment='center')
        
        #xdisplay, ydisplay = self.ax.transData.transform((0,base_y+self.pulse_height*0.5))
        #xdisplay_text = xdisplay - 50
        #ydisplay_text= ydisplay

        #self.ax.text(xdisplay_text, ydisplay_text, name, transform=self.fig.get_transform())
        self.ax.text(x=-self.cycletime*0.15, y=base_y+self.pulse_height*0.5, s=name, 
                     verticalalignment="center", size=small_font_size)

        self.ax.hlines(base_y, 0, self.cycletime, color="black", linewidth=0.5)

        for i in np.arange(start, end, 1/(freq*5)):
            # plt.plot([i, i], [base_y, base_y+self.pulse_height])
            #self.ax.plot([i, i], [base_y, base_y+self.pulse_height], color="black", linewidth=1)
            self.ax.vlines(i, base_y, base_y+self.pulse_height, color=color, linewidth=1)


    def draw_oxy_pulse(self, start, end, row_num, name):

        base_y = self.offset + self.pulse_height*row_num*2
        self.ax.text(x=(start+end)/2, y=base_y+self.pulse_height+3, s="{0} s".format("%.1f" % (end-start)), horizontalalignment='center')
        baseline_x = [0, self.cycletime]
        baseline_y = [base_y, base_y]

        self.ax.text(x=-self.cycletime*0.15, y=base_y+self.pulse_height*0.5, s=name, verticalalignment="center", size=small_font_size)

        self.ax.plot(baseline_x, baseline_y, color="black", linewidth=0.5)

        r = patches.Rectangle(xy=(
            start, base_y), width=end-start, height=self.pulse_height, color="red", fill=True)
        self.ax.add_patch(r)

    def draw_process_pulse(self, start, end, row_num, name):

        base_y = self.offset + self.pulse_height*row_num*2
        self.ax.text(x=(start+end)/2, y=base_y+self.pulse_height+3, s="{0} s".format("%.1f" % (end-start)), horizontalalignment='center')
        baseline_x = [0, self.cycletime]
        baseline_y = [base_y, base_y]

        x=(start+end)/2
        y=base_y+0.5*(self.pulse_height)-1

        self.ax.text(x=-self.cycletime*0.15, y=base_y+self.pulse_height*0.5, s=name, verticalalignment="center", size=small_font_size)

        self.ax.plot(baseline_x, baseline_y, color="black", linewidth=0.5)

        r = patches.Rectangle(xy=(
            start, base_y), width=end-start, height=self.pulse_height, fill=False, lw=1)
        self.ax.add_patch(r)

    def finalize(self, filename):
        plt.savefig(filename)
        plt.show()


if __name__ == "__main__":

    
    seq = SEQ(total_row_num=7, cycletime=5)
    init = 1
    pur = 1
    oxy_time = 0.5
    freq = 5
    seq.draw_freq_pulse_notime(start=0, end=13, freq=freq, row_num=6, name="Er/Y\nBase Pulse", color="green")
    seq.draw_process_pulse(start=init, end=init+1, row_num=5, name="Er/Y\nProcess Pulse")
    seq.draw_freq_pulse_notime(start=init, end=init+1, freq=freq, row_num=4, name="Er/Y\nSputter Pulse", color="green")
    seq.draw_freq_pulse_notime(start=0, end=13, freq=freq, row_num=3, name="Zr\nBase Pulse", color="purple")
    seq.draw_process_pulse(start=3.5, end=4.5, row_num=2, name="Zr\nProcess Pulse")
    seq.draw_freq_pulse_notime(start=3.5, end=4.5, freq=freq, row_num=1, name="Zr\nSputter Pulse", color="purple")
    seq.draw_oxy_pulse(start=2, end=2+oxy_time, row_num=0, name="$O_2$\nGas Pulse")
    seq.draw_oxy_pulse(start=4.5, end=4.5+oxy_time, row_num=0, name="$O_2$\nGas Pulse")
    seq.draw_arrow(start=0, end=1, row_num=0)
    seq.draw_arrow(start=2.5, end=3.5, row_num=0)
    seq.draw_gapline(1)
    seq.draw_gapline(2)
    seq.draw_gapline(2.5)
    seq.draw_gapline(3.5)
    seq.draw_gapline(4.5)
    seq.finalize("eyzo_long.pdf")
    

    
    seq = SEQ(total_row_num=7, cycletime=13)
    init = 0
    pur = 3
    oxy_time = 1
    seq.draw_freq_pulse_notime(start=0, end=13, freq=3, row_num=6, name="Hf\nBase Pulse", color="green")
    seq.draw_process_pulse(start=init, end=init+1, row_num=5, name="Hf\nProcess Pulse")
    seq.draw_freq_pulse_notime(start=init, end=init+1, freq=3, row_num=4, name="Hf\nSputter Pulse", color="green")
    seq.draw_freq_pulse_notime(start=init, end=13, freq=3, row_num=3, name="Zr\nBase Pulse", color="purple")
    seq.draw_process_pulse(start=5.5, end=8.5, row_num=2, name="Zr\nProcess Pulse")
    seq.draw_freq_pulse_notime(start=5.5, end=8.5, freq=3, row_num=1, name="Zr\nSputter Pulse", color="purple")
    seq.draw_oxy_pulse(start=init+1, end=init+2, row_num=0, name="$O_2$\nGas Pulse")
    seq.draw_oxy_pulse(start=8.5, end=9.5, row_num=0, name="")
    seq.draw_arrow(start=2, end=5.5, row_num=0)
    seq.draw_arrow(start=9.5, end=13, row_num=0)
    seq.draw_gapline(1)
    seq.draw_gapline(2)
    seq.draw_gapline(5.5)
    seq.draw_gapline(8.5)
    seq.draw_gapline(9.5)
    seq.finalize("hzo_long.pdf")
    

    
    seq = SEQ(total_row_num=7, cycletime=15.9)
    init = 0
    pur = 3
    oxy_time = 1
    seq.draw_freq_pulse_notime(start=init, end=15.9, freq=3, row_num=6, name="Al:\nPlasma\nbase pulse", color="grey")
    seq.draw_process_pulse(start=init, end=init+6, row_num=5, name="Al:\nProcess\nduration")
    seq.draw_freq_pulse_notime(start=init, end=init+6, freq=3, row_num=4, name="Al:\nSputter Pulse", color="grey")
    seq.draw_freq_pulse_notime(start=init, end=15.9, freq=3, row_num=3, name="Cu:\nPlasma\nbase pulse", color="saddlebrown")
    seq.draw_process_pulse(start=10, end=11.9, row_num=2, name="Cu:\nProcess\nduration")
    seq.draw_freq_pulse_notime(start=10, end=11.9, freq=3, row_num=1, name="Cu:\nSputter Pulse", color="saddlebrown")
    seq.draw_oxy_pulse(start=6, end=7, row_num=0, name="$O_2$\nGas Pulse")
    seq.draw_oxy_pulse(start=11.9, end=12.9, row_num=0, name="")
    seq.draw_arrow(start=7, end=10, row_num=0)
    seq.draw_arrow(start=12.9, end=15.9, row_num=0)
    seq.draw_gapline(6)
    seq.draw_gapline(7)
    seq.draw_gapline(10)
    seq.draw_gapline(11.9)
    seq.draw_gapline(12.9)
    seq.finalize("cao_long.pdf")
   