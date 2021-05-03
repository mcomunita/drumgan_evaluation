from os.path import dirname, join


# DEFAULT_PITCH_INCEPTION_MODEL = join(dirname(__file__), "instrument_inception_model_2020-01-17.pt")
# DEFAULT_INSTRUMENT_INCEPTION_MODEL = join(dirname(__file__), "pitch_inception_model_2020-01-16.pt")
DEFAULT_FOOTSTEPS_INCEPTION_MODEL = join(dirname(__file__), "footsteps_inception_model_best_2021-04-29.pt")

DEFAULT_INCEPTION_PREPROCESSING_CONFIG = dict(transform='specgrams',
												fade_out=True,
												fft_size=1024,
												win_size=1024,
												n_frames=64,
												hop_size=256,
						                      	n_bins=128,
						                        n_mel=256)