from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as patches
# CLASS

font_size = 13

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
        self.ax.set_yticks([])

    def draw_arrow(self, start, end, row_num):
        base_y = self.offset + self.pulse_height*row_num*2+self.pulse_height
        # self.ax.arrow(start, base_y+2.5, end-start, 0, width=0.1, head_width=2,head_length=0.2, length_includes_head=True, color='k')
        self.ax.text(x=(start+end)/2, y=base_y+2.5,
                     s="{0} s".format("%.1f" % (end-start)), horizontalalignment='center')
        self.ax.annotate(text='', xy=(end, base_y),
                         xytext=(start, base_y), arrowprops=dict(arrowstyle='<->', color='black'))
        
    def draw_gapline(self, x):
        self.ax.vlines(x, self.offset, self.offset+2*self.total_row_num*self.pulse_height, 
                       color="black", linestyles='dotted', linewidth=0.5)
        
    def trigger(self, x, name):
        y = self.ax.get_ylim()[1]
        self.ax.annotate(text="", xy=(x, y),
                         xytext=(x, y+10), annotation_clip=False, arrowprops=dict(arrowstyle='->', color='black'))
        
        self.ax.text(x+0.25, y+5, s="{0} s\n{1}".format(x,name), fontsize=10.5, verticalalignment="center")

    def draw_freq_pulse(self, start, end, freq, row_num, name):

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

        self.ax.hlines(base_y, 0, self.cycletime, color="black")

        for i in np.arange(start, end, 1/(freq*5)):
            # plt.plot([i, i], [base_y, base_y+self.pulse_height])
            #self.ax.plot([i, i], [base_y, base_y+self.pulse_height], color="black", linewidth=1)
            self.ax.vlines(i, base_y, base_y+self.pulse_height, color="black", linewidth=0.2)

    def draw_pulse(self, start, end, row_num, name):

        base_y = self.offset + self.pulse_height*row_num*2
        self.ax.text(x=(start+end)/2, y=base_y+self.pulse_height+3, s="{0} s".format(
            "%.1f" % (end-start)), horizontalalignment='center')
        baseline_x = [0, self.cycletime]
        baseline_y = [base_y, base_y]

        #xdisplay, ydisplay = self.ax.transData.transform((0,base_y+self.pulse_height*0.5))
        #xdisplay_text = xdisplay - 50
        #ydisplay_text= ydisplay
        self.ax.text(x=-self.cycletime*0.1, y=base_y+self.pulse_height*0.5, s=name, verticalalignment="center")
        #self.ax.text(xdisplay_text, ydisplay_text, name, transform=self.fig.get_transform())

        self.ax.plot(baseline_x, baseline_y, color="black")

        r = patches.Rectangle(xy=(
            start, base_y), width=end-start, height=self.pulse_height, color="black", fill=True)
        self.ax.add_patch(r)
        # plt.plot(baseline_x, baseline_y)

    def finalize(self, filename):
        plt.savefig(filename)
        plt.show()


if __name__ == "__main__":

    seq = SEQ(total_row_num=3, cycletime=5)
    seq.draw_freq_pulse(start=0.8, end=1.8, freq=10, row_num=2, name="Hf")
    seq.draw_pulse(start=1.8, end=2.5, row_num=0, name="$O_{2}$")
    seq.draw_freq_pulse(start=3.3, end=4.3, freq=10, row_num=1, name="Zr")
    seq.draw_pulse(start=4.3, end=5, row_num=0, name="$O_{2}$")
    seq.draw_arrow(start=0, end=0.8, row_num=2)
    seq.draw_arrow(start=2.5, end=3.3, row_num=1)
    seq.draw_gapline(0.8)
    seq.draw_gapline(2.5)
    seq.draw_gapline(3.3)
    seq.finalize("pattern1.pdf")

    """
    seq = SEQ(total_row_num=3, cycletime=10.4)
    seq.draw_freq_pulse(start=2.5, end=3, freq=10, row_num=2, name="Hf")
    seq.draw_freq_pulse(start=6.2, end=9.7, freq=10, row_num=1, name="Zr")
    seq.draw_pulse(start=3, end=3.7, row_num=0, name="$O_{2}$")
    seq.draw_pulse(start=9.7, end=10.4, row_num=0, name="$O_{2}$")
    seq.draw_arrow(start=0, end=2.5, row_num=2)
    seq.draw_arrow(start=3.7, end=6.2, row_num=1)
    seq.draw_gapline(2.5)
    seq.draw_gapline(3.7)
    seq.draw_gapline(6.2)
    seq.trigger(x=1, name="350 V->490 V")
    seq.trigger(x=3.5, name="490 V->350 V")
    seq.finalize("pattern2.pdf")
    """

    """
    seq = SEQ(total_row_num=3, cycletime=5.4)
    seq.draw_freq_pulse(start=1, end=2, freq=10, row_num=2, name="Hf")
    seq.draw_freq_pulse(start=3.7, end=4.7, freq=10, row_num=1, name="Zr")
    seq.draw_pulse(start=2, end=2.7, row_num=0, name="$O_{2}$")
    seq.draw_pulse(start=4.7, end=5.4, row_num=0, name="$O_{2}$")
    seq.draw_arrow(start=0, end=1, row_num=2)
    seq.draw_arrow(start=2.7, end=3.7, row_num=2)
    #seq.draw_gapline(0)
    seq.draw_gapline(1)
    seq.draw_gapline(2.7)
    seq.draw_gapline(3.7)
    seq.finalize("clean.pdf")
    """
