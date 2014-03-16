#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sun Mar 16 11:24:50 2014
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import histosink_gl
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0.002,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_histosink2_0 = histosink_gl.histo_sink_f(
        	self.GetWin(),
        	title="Histogram Plot",
        	num_bins=63,
        	frame_size=1000,
        )
        self.Add(self.wxgui_histosink2_0.win)
        self.gr_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(1, gr.GR_LSB_FIRST)
        self.gr_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.gr_multiply_const_vxx_0 = blocks.multiply_const_vff((1.0/128, ))
        self.gr_glfsr_source_x_0 = digital.glfsr_source_b(6+1, True, 0, 1)
        self.gr_char_to_float_0 = blocks.char_to_float(1, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.gr_throttle_0, 0), (self.wxgui_histosink2_0, 0))
        self.connect((self.gr_glfsr_source_x_0, 0), (self.gr_unpacked_to_packed_xx_0, 0))
        self.connect((self.gr_unpacked_to_packed_xx_0, 0), (self.gr_char_to_float_0, 0))
        self.connect((self.gr_char_to_float_0, 0), (self.gr_multiply_const_vxx_0, 0))
        self.connect((self.gr_multiply_const_vxx_0, 0), (self.gr_throttle_0, 0))
        self.connect((self.gr_throttle_0, 0), (self.wxgui_scopesink2_0, 0))


# QT sink close method reimplementation

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.gr_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()

