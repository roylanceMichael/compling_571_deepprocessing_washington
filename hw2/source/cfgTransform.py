import nltk
class CfgTransform:
	def __init__(self, cfg):
		this.grammar = nltk.parse_cfg(cfg)

	def 