def get_helloworld():
	return 'hello world'

if __name__ == '__main__':
	print(get_helloworld())


def test_get_helloworld():
	assert 'hello world' == get_helloworld()
