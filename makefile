test:
	python main.py keyboards/colemak -r -o test --dir test_dir
	cat test_dir/test
gen_plugin:
	python main.py keyboards/colemak -r -o colemak --dir test_dir/colemak
	python main.py keyboards/dvorak -r -o dvorak --dir test_dir/dvorak
	python main.py keyboards/dvorak-right -r -o dvorak-right --dir test_dir/dvorak-right
	python main.py keyboards/dvorak-left -r -o dvorak-left --dir test_dir/dvorak-left
	python main.py keyboards/azerty -r -o azerty --dir test_dir/azerty
