```

autonomous-synthesis-planner/
│
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── Makefile
│
├── docs/
│   ├── architecture.md
│   ├── api.md
│   └── cli.md
│
├── examples/
│   ├── aspirin.py
│   ├── caffeine.py
│   └── ibuprofen.py
│
├── datasets/
│   ├── reactions/
│   └── templates/
│
├── models/
│
├── tests/
│   ├── test_api.py
│   ├── test_cli.py
│   ├── test_parser.py
│   ├── test_planner.py
│   ├── test_retrosynthesis.py
│   ├── test_scoring.py
│   └── test_visualization.py
│
├── scripts/
│   ├── download_data.py
│   └── build_templates.py
│
└── src/
    └── asp/
        │
        ├── __init__.py
        ├── cli.py
        ├── api.py
        ├── config.py
        ├── constants.py
        │
        ├── chemistry/
        │   ├── __init__.py
        │   ├── molecule.py
        │   ├── parser.py
        │   ├── reaction.py
        │   └── templates.py
        │
        ├── planning/
        │   ├── __init__.py
        │   ├── planner.py
        │   ├── retrosynthesis.py
        │   ├── search.py
        │   ├── scoring.py
        │   └── optimizer.py
        │
        ├── data/
        │   ├── __init__.py
        │   ├── loader.py
        │   └── repository.py
        │
        ├── visualization/
        │   ├── __init__.py
        │   └── routes.py
        │
        ├── io/
        │   ├── __init__.py
        │   ├── export.py
        │   └── importers.py
        │
        └── utils/
            ├── __init__.py
            ├── logging.py
            ├── validation.py
            └── helpers.py
