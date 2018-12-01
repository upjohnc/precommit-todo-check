# TODO checker for precommit

can add arg `--skip`

```
  - repo: git://github.com/upjohnc/precommit-todo-check
    sha: 1.0.0
    hooks:
      - id: python-todo-check
        args: ['--skip=nifi/scripts/score_validation.py, stream-generator/stream_generator/qpp/submission_logs.py']
```
