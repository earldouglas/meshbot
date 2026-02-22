{
  pkgs ? import <nixpkgs> { },
}:
let
  python = pkgs.python314;

  fortune-python-version = "1.1.2";

  fortune = python.pkgs.buildPythonPackage rec {
    pname = "fortune_python";
    version = fortune-python-version;
    pyproject = true;
    src = python.pkgs.fetchPypi {
      inherit pname version;
      hash = "sha256-i3LVtWJ105y6fAbMf4Tx7ant6vWjzv4LYZyJ7LGc+hE=";
    };
    propagatedBuildInputs = [
      python.pkgs.setuptools
    ];
  };
in
python.pkgs.buildPythonApplication rec {

  pname = "meshbot";
  version = "0.0.0";
  pyproject = true;
  src = ./.;

  # run-time dependencies
  propagatedBuildInputs = [
    python.pkgs.meshtastic
    fortune
  ];

  # test dependencies
  nativeCheckInputs = [
    python.pkgs.mypy
    python.pkgs.black
    python.pkgs.pytest
  ];

  preBuild = ''
    cat > pyproject.toml << EOF
    [project]
    name = "${pname}"
    version = "0.0.0"
    requires-python = "==3.14"
    dependencies = [
      "meshtastic==2.7.7",
      "fortune-python==${fortune-python-version}",
    ]
    [project.scripts]
    meshbot = "main:main"
    EOF
  '';

  checkPhase = ''
    mypy --ignore-missing-imports src
    black --check --diff src
    pytest tests/
  '';
}
