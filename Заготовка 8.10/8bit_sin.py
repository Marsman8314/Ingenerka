import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = r2r.R2R_DAC()

    start_time = time.time()

    while True:
        t = time.time() - start_time
        value = sg.get_sin_wave_amplitude(signal_frequency, t)
        dac.set_voltage(value * amplitude)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.destroy()