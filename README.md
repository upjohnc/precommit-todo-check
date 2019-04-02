# TODO checker for precommit

can add arg `--skip`: the root directory will be added to the path given.  And all of the items should be inside the `'`.

```
  - repo: git://github.com/upjohnc/precommit-todo-check
    sha: 1.0.0
    hooks:
      - id: python-todo-check
        args: ['--skip=nifi/scripts/score_validation.py, stream-generator/stream_generator/qpp/submission_logs.py']
```
