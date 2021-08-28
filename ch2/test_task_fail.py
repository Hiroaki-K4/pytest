from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'], defaults=[None, None, False, None])

def test_task_equality():
	"""Different tasks should not be equal."""
	t1 = Task('sit there', 'brian')
	t2 = Task('do something', 'okken')
	assert t1 == t2

def test_dict_equality():
	"""Different tasks compared as dicts should not be equal."""
	t1 = Task('make sandwich', 'okken')
	t1_dict = t1._asdict()
	t2 = Task('make sandwich', 'okkem')
	t2_dict = t2._asdict()
	assert t1_dict == t2_dict
