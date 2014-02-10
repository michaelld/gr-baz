#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Borip Usrp Uhd
# Generated: Sat Feb  1 00:00:03 2014
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import baz
import time

class borip_usrp_uhd(gr.top_block):

    def __init__(self, addr=""):
        gr.top_block.__init__(self, "Borip Usrp Uhd")

        ##################################################
        # Parameters
        ##################################################
        self.addr = addr

        ##################################################
        # Variables
        ##################################################
        self.decim = decim = 256
        self.adc_freq = adc_freq = 64000000
        self.tune_tolerance = tune_tolerance = 1
        self.tr_to_list = tr_to_list = lambda req, tr: [req, tr.baseband_freq, tr.dxc_freq + tr.residual_freq, tr.dxc_freq]
        self.source_name = source_name = lambda: "USRP (" + self.source.get_usrp_info().get("mboard_id") + ")"
        self.serial = serial = lambda: self.source.get_usrp_info().get("mboard_serial")
        self.samp_rate = samp_rate = adc_freq/decim
        self.gain = gain = 0
        self.freq = freq = 0
        self.antenna_0 = antenna_0 = "TX/RX"
        self.antenna = antenna = "RX2"

        ##################################################
        # Blocks
        ##################################################
        self.source = uhd.usrp_source(
        	device_addr=addr,
        	stream_args=uhd.stream_args(
        		cpu_format="sc16",
        		channels=range(1),
        	),
        )
        self.source.set_samp_rate(samp_rate)
        self.source.set_center_freq(freq, 0)
        self.source.set_gain(gain, 0)
        self.source.set_antenna(antenna, 0)
        self.sink = baz.udp_sink(gr.sizeof_short*2, "192.168.1.52", 28888, 1472, False, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.source, 0), (self.sink, 0))


# QT sink close method reimplementation

    def get_addr(self):
        return self.addr

    def set_addr(self, addr):
        self.addr = addr

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_samp_rate(self.adc_freq/self.decim)

    def get_adc_freq(self):
        return self.adc_freq

    def set_adc_freq(self, adc_freq):
        self.adc_freq = adc_freq
        self.set_samp_rate(self.adc_freq/self.decim)

    def get_tune_tolerance(self):
        return self.tune_tolerance

    def set_tune_tolerance(self, tune_tolerance):
        self.tune_tolerance = tune_tolerance

    def get_tr_to_list(self):
        return self.tr_to_list

    def set_tr_to_list(self, tr_to_list):
        self.tr_to_list = tr_to_list

    def get_source_name(self):
        return self.source_name

    def set_source_name(self, source_name):
        self.source_name = source_name

    def get_serial(self):
        return self.serial

    def set_serial(self, serial):
        self.serial = serial

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.source.set_samp_rate(self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.source.set_gain(self.gain, 0)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.source.set_center_freq(self.freq, 0)

    def get_antenna_0(self):
        return self.antenna_0

    def set_antenna_0(self, antenna_0):
        self.antenna_0 = antenna_0

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna
        self.source.set_antenna(self.antenna, 0)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("-a", "--addr", dest="addr", type="string", default="",
        help="Set Address [default=%default]")
    (options, args) = parser.parse_args()
    tb = borip_usrp_uhd(addr=options.addr)
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()

