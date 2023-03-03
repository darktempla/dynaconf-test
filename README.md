# dynaconf-test

### Setup

1. `poetry install` - to pull in dependencies
2. In PyCharm IDE setup a python interpreter pointing to active poetry virtual env

### Issue

The dynaconf settings I want to be packaged up with the module.

As such the config and **settings.toml** and **secrets.toml** files have been moved into the package folder `dynaconf_test`. 

So in the `dynaconf_test/config.py` file I have set the root path to `root_path='./dynaconf_test/'`. 

When I run the tests from the terminal using the following command the dynaconf is picked up okay and the test passes.

```bash
poetry run python -m unittest discover -v
```

If I want to run the test from the IDE then it fails with the following error:

```commandline
/Users/darktempla/Library/Caches/pypoetry/virtualenvs/dynaconf-test-7APtyPOS-py3.10/bin/python /Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pycharm/_jb_unittest_runner.py --target test_main.TestMain 
Testing started at 3:45 am ...
Launching unittests with arguments python -m unittest test_main.TestMain in /Users/darktempla/Code/Projects/dynaconf-test/tests



Ran 1 test in 0.015s

FAILED (errors=1)

Error
Traceback (most recent call last):
  File "/Users/darktempla/Code/Projects/dynaconf-test/tests/test_main.py", line 9, in test_main
    settings.setenv('test')
  File "/Users/darktempla/Library/Caches/pypoetry/virtualenvs/dynaconf-test-7APtyPOS-py3.10/lib/python3.10/site-packages/dynaconf/base.py", line 115, in __getattr__
    self._setup()
  File "/Users/darktempla/Library/Caches/pypoetry/virtualenvs/dynaconf-test-7APtyPOS-py3.10/lib/python3.10/site-packages/dynaconf/base.py", line 174, in _setup
    self._wrapped = Settings(
  File "/Users/darktempla/Library/Caches/pypoetry/virtualenvs/dynaconf-test-7APtyPOS-py3.10/lib/python3.10/site-packages/dynaconf/base.py", line 253, in __init__
    self.execute_loaders()
  File "/Users/darktempla/Library/Caches/pypoetry/virtualenvs/dynaconf-test-7APtyPOS-py3.10/lib/python3.10/site-packages/dynaconf/base.py", line 1026, in execute_loaders
    settings_loader(
  File "/Users/darktempla/Library/Caches/pypoetry/virtualenvs/dynaconf-test-7APtyPOS-py3.10/lib/python3.10/site-packages/dynaconf/loaders/__init__.py", line 167, in settings_loader
    found = obj.find_file(item, project_root=p_root)
  File "/Users/darktempla/Library/Caches/pypoetry/virtualenvs/dynaconf-test-7APtyPOS-py3.10/lib/python3.10/site-packages/dynaconf/base.py", line 1156, in find_file
    return find_file(*args, **kwargs)
  File "/Users/darktempla/Library/Caches/pypoetry/virtualenvs/dynaconf-test-7APtyPOS-py3.10/lib/python3.10/site-packages/dynaconf/utils/files.py", line 63, in find_file
    search_tree.extend(_walk_to_root(project_root, break_at=work_dir))
  File "/Users/darktempla/Library/Caches/pypoetry/virtualenvs/dynaconf-test-7APtyPOS-py3.10/lib/python3.10/site-packages/dynaconf/utils/files.py", line 15, in _walk_to_root
    raise OSError("Starting path not found")
OSError: Starting path not found
```

