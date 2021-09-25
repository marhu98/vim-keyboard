test:
	python main.py keyboards/colemak -r -o test --dir test_dir
	cat test_dir/test
gen_plugin:
	python main.py keyboards/colemak -r -o colemak.vim --dir test_dir/colemak
	python main.py keyboards/dvorak -r -o dvorak.vim --dir test_dir/dvorak
	python main.py keyboards/dvorak-right -r -o dvorak-right.vim --dir test_dir/dvorak-right
	python main.py keyboards/dvorak-left -r -o dvorak-left.vim --dir test_dir/dvorak-left
	python main.py keyboards/azerty -r -o azerty.vim --dir test_dir/azerty
